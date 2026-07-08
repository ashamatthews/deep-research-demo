import os
import json
import requests
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

from google import genai
from langfuse import observe, get_client
from openinference.instrumentation.google_genai import GoogleGenAIInstrumentor


# -----------------------------
# Setup
# -----------------------------

GoogleGenAIInstrumentor().instrument()

langfuse = get_client()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY in .env")

if not JINA_API_KEY:
    raise ValueError("Missing JINA_API_KEY in .env")

client = genai.Client(api_key=GOOGLE_API_KEY)


# -----------------------------
# LLM Helper
# -----------------------------

@observe()
def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


# -----------------------------
# Search Tool
# -----------------------------

@observe()
def jina_search(query: str) -> str:
    query = query.replace('"', "").replace("'", "")
    url = f"https://s.jina.ai/{quote(query)}"

    headers = {
        "Authorization": f"Bearer {JINA_API_KEY}",
        "Accept": "text/plain",
    }

    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()

    return response.text[:12000]

# -----------------------------
# Agent 1: Planner Agent
# -----------------------------

@observe()
def planner_agent(question: str, previous_learnings: str = "") -> list[str]:
    prompt = f"""
You are the Planner Agent in a Deep Research system.

Your job is to create search queries for a research assistant.

Research question:
{question}

Previous learnings:
{previous_learnings if previous_learnings else "None yet."}

Generate 5 strong search queries.

Rules:
- Return only the queries.
- One query per line.
- Do not number them.
- Do not use quotation marks around phrases.
- Focus on academic papers, arXiv papers, research agents, multi-agent systems, query planning, iterative search, and deep research agents.
- Avoid repeating previous queries.
"""

    raw_queries = ask_gemini(prompt)

    queries = [
        q.strip("-• 1234567890. ")
        for q in raw_queries.splitlines()
        if q.strip()
    ]

    return queries[:5]


# -----------------------------
# Agent 2: Search Agent
# -----------------------------

@observe()
def search_agent(queries: list[str]) -> str:
    all_results = ""

    for query in queries:
        print(f"Searching: {query}")

        try:
            result = jina_search(query)
            all_results += f"\n\n## Search query: {query}\n{result}"
        except Exception as e:
            all_results += f"\n\n## Search query: {query}\nSearch failed: {e}"

    return all_results


# -----------------------------
# Agent 3: Reviewer Agent
# -----------------------------

@observe()
def reviewer_agent(question: str, search_results: str, previous_learnings: str = "") -> dict:
    prompt = f"""
You are the Reviewer Agent in a Deep Research system.

Your job is to review search results and extract useful research learnings.

Research question:
{question}

Previous learnings:
{previous_learnings if previous_learnings else "None yet."}

New search results:
{search_results}

Return your answer as valid JSON with this structure:

{{
  "learnings": [
    {{
      "title": "...",
      "authors_year": "...",
      "url": "...",
      "summary": "...",
      "relevance": "...",
      "confidence": "High / Medium / Low"
    }}
  ],
  "knowledge_gaps": [
    "..."
  ],
  "need_more_search": true
}}

Rules:
- Use only sources actually present in the search results.
- Do not invent titles, authors, years, or URLs.
- Prefer arXiv, conference papers, journal papers, official engineering blogs, and credible technical sources.
- Mark Medium or Low confidence for blogs, unclear sources, or partial matches.
- Set need_more_search to true if important parts of the question are still missing.
- Set need_more_search to false if there is enough information for a strong annotated reading list.
"""

    raw = ask_gemini(prompt)

    try:
        start = raw.find("{")
        end = raw.rfind("}") + 1
        json_text = raw[start:end]
        return json.loads(json_text)
    except Exception:
        return {
            "learnings": [],
            "knowledge_gaps": [
                "Reviewer output could not be parsed as JSON.",
                raw
            ],
            "need_more_search": False
        }


# -----------------------------
# Agent 4: Writer Agent
# -----------------------------

@observe()
def writer_agent(question: str, all_learnings: list[dict]) -> str:
    learnings_text = json.dumps(all_learnings, indent=2)

    prompt = f"""
You are the Writer Agent in a Deep Research system.

Create a polished annotated reading list for this research question:

{question}

Use ONLY these extracted learnings:
{learnings_text}

Rules:
- Do not invent sources.
- Include every URL.
- Include confidence level.
- Prefer academic sources first.
- Be honest when something is only partially relevant.
- Explain how each source connects to:
  planning, query generation, search execution, result evaluation, and iterative follow-up.

Format:

# Annotated Reading List

## 1. Title

**Authors/year:**  
**URL/source:**  
**Confidence:**  

**Summary:**  

**Why it matters for multi-agent research assistants:**  

**Connection to deep research workflow:**  
"""

    return ask_gemini(prompt)


# -----------------------------
# Main Deep Research Loop
# -----------------------------

@observe()
def deep_research(question: str, max_rounds: int = 3) -> str:
    all_learnings = []
    previous_learnings_text = ""

    for round_number in range(1, max_rounds + 1):
        print(f"\n===== ROUND {round_number} =====")
        print("Planner Agent: generating search queries...")

        queries = planner_agent(question, previous_learnings_text)

        print("Search Agent: searching with Jina...")
        search_results = search_agent(queries)

        print("Reviewer Agent: extracting learnings and checking gaps...")
        review = reviewer_agent(
            question=question,
            search_results=search_results,
            previous_learnings=previous_learnings_text
        )

        new_learnings = review.get("learnings", [])
        knowledge_gaps = review.get("knowledge_gaps", [])
        need_more_search = review.get("need_more_search", False)

        all_learnings.extend(new_learnings)

        previous_learnings_text = json.dumps(
            {
                "learnings_so_far": all_learnings,
                "remaining_gaps": knowledge_gaps
            },
            indent=2
        )

        print(f"New learnings found: {len(new_learnings)}")
        print(f"Knowledge gaps: {len(knowledge_gaps)}")
        print(f"Need more search? {need_more_search}")

        if not need_more_search:
            print("Reviewer Agent says enough information has been gathered.")
            break

    print("\nWriter Agent: writing final annotated reading list...")
    final_report = writer_agent(question, all_learnings)

    with open("annotated_reading_list.md", "w", encoding="utf-8") as f:
        f.write(final_report)

    langfuse.flush()

    return final_report


# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    question = """
Give me research papers that describe multi-agent systems that can answer a research question by developing a research plan, generating and executing the queries, considering the results, and potentially making more queries until they have enough information to answer the research question.
"""

    report = deep_research(question, max_rounds=3)

    print("\n\n===== FINAL REPORT =====\n")
    print(report)

    print("\nSaved report to annotated_reading_list.md")

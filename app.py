import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

from google import genai
from langfuse import observe, get_client
from openinference.instrumentation.google_genai import GoogleGenAIInstrumentor


GoogleGenAIInstrumentor().instrument()

langfuse = get_client()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY in .env")

if not JINA_API_KEY:
    raise ValueError("Missing JINA_API_KEY in .env")

client = genai.Client(api_key=GOOGLE_API_KEY)


@observe()
def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text


@observe()
def jina_search(query: str) -> str:
    url = f"https://s.jina.ai/{quote(query)}"

    headers = {
        "Authorization": f"Bearer {JINA_API_KEY}",
        "Accept": "text/plain",
    }

    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()

    return response.text[:10000]


@observe()
def generate_search_queries(question: str) -> list[str]:
    prompt = f"""
You are a research planning agent.

Given the research question below, generate exactly 8 focused search queries.

Research question:
{question}

Rules:
- Return only the search queries.
- One query per line.
- Do not include numbering.
- Focus on academic papers, multi-agent research assistants, iterative search, query planning, and deep research agents.
"""

    queries_text = ask_gemini(prompt)

    queries = [
        q.strip("-• 1234567890. ")
        for q in queries_text.splitlines()
        if q.strip()
    ]

    return queries[:8]


@observe()
def summarize_search_results(question: str, all_results: str) -> str:
    prompt = f"""
You are analyzing search results for an annotated academic reading list.

Original research question:
{question}

Search results:
{all_results}

Extract only sources that are actually present in the search results.

For each useful source, include:
- exact title
- author/year if available
- URL if available
- what the source is about
- why it relates to multi-agent research assistants
- whether it includes planning, query generation, search execution, result evaluation, or iterative follow-up

Rules:
- Do not invent papers.
- Do not invent authors.
- Do not invent URLs.
- If information is missing, write "not found".
"""

    return ask_gemini(prompt)


@observe()
def write_final_report(question: str, notes: str) -> str:
    prompt = f"""
Create a polished annotated reading list using ONLY the sources found in the research notes.

Research question:
{question}

Research notes:
{notes}

Rules:
- Do not invent paper titles.
- Include URL/source for every item.
- Prefer academic papers, arXiv papers, conference papers, or official engineering blogs.
- If author/year is missing, write "author/year not found".
- Be honest if a source only partially matches the research question.
- Each annotation should explain how the source relates to:
  planning, query generation, search execution, result evaluation, and iterative follow-up.

Format:

# Annotated Reading List

## 1. Title

**Authors/year:**  
**URL/source:**  

**Summary:**  

**Why it matters for multi-agent research assistants:**  

**Connection to deep research workflow:**  
"""

    return ask_gemini(prompt)


@observe()
def deep_research(question: str) -> str:
    print("Generating search queries...")
    queries = generate_search_queries(question)

    all_results = ""

    for query in queries:
        print(f"Searching: {query}")
        try:
            result = jina_search(query)
            all_results += f"\n\n## Search query: {query}\n{result}"
        except Exception as e:
            all_results += f"\n\n## Search query: {query}\nSearch failed: {e}"

    print("Summarizing results...")
    notes = summarize_search_results(question, all_results)

    print("Writing final report...")
    final_report = write_final_report(question, notes)

    langfuse.flush()

    return final_report


if __name__ == "__main__":
    question = """
Give me research papers that describe multi-agent systems that can answer a research question by developing a research plan, generating and executing the queries, considering the results, and potentially making more queries until they have enough information to answer the research question.
"""

    report = deep_research(question)

    print("\n\n===== FINAL REPORT =====\n")
    print(report)

# Annotated Reading List

## 1. Knowledge-Aware Iterative Retrieval for Multi-Agent Systems

**Authors/year:** Anon., 2025  
**URL/source:** https://arxiv.org/html/2503.13275v2  
**Confidence:** High  

**Summary:** This paper introduces an LLM-driven agent framework that iteratively refines queries and filters contextual evidence by leveraging dynamically evolving internal knowledge. It features a progressive update of an internal knowledge cache to guide query generation and evidence selection. The system supports multi-step open-domain question answering by following core stages: Query Planning (refining search queries and addressing sub-goals), Knowledge Extraction (distilling facts and identifying gaps), and Contextual Filtering. If information gaps persist, the cycle reiterates. Critically, it supports multi-agent configurations where agents can collaborate by sharing knowledge, demonstrating improved performance on complex tasks as difficulty increases, and showing emergent role differentiation in competitive settings.

**Why it matters for multi-agent research assistants:** This paper directly addresses the core requirements for multi-agent research assistants, specifically focusing on how agents can iteratively refine their understanding and approach to complex questions. Its emphasis on dynamically evolving knowledge and multi-agent collaboration provides a strong foundation for building sophisticated research systems.

**Connection to deep research workflow:**
*   **Planning:** The system includes a 'Query Planning' stage, where agents refine search queries and break down sub-goals, directly contributing to the research plan.
*   **Query Generation:** Query planning explicitly involves refining search queries, and the dynamically evolving internal knowledge guides the generation of subsequent, more targeted queries.
*   **Search Execution:** The agents perform iterative retrieval, which constitutes the execution of queries against external sources.
*   **Result Evaluation:** 'Knowledge Extraction' distills facts and identifies information gaps, which is a form of evaluating the retrieved results against the current knowledge state and research goals. 'Contextual Filtering' further refines results.
*   **Iterative Follow-up:** The system explicitly states that if information gaps persist, "the cycle reiterates," indicating an iterative feedback loop for making more queries until the question is answered.

## 2. Deep Research: A Survey of Autonomous Research Agents

**Authors/year:** Anon., 2025  
**URL/source:** https://arxiv.org/html/2508.12752v1  
**Confidence:** High  

**Summary:** This survey provides a systematic overview of the 'deep research' paradigm, where autonomous agents engage in planning, retrieval, and synthesis to generate comprehensive analytical reports grounded in web-based evidence. The process involves four core stages: Planning (decomposing a high-level research question into sub-goals and a roadmap), Question Developing (formulating diverse, contextualized retrieval queries), Web Exploration (iteratively collecting and filtering information from external sources), and Report Generation (integrating and structuring retrieved evidence). The survey highlights how agents can dynamically and iteratively interact with external knowledge sources to overcome LLM limitations, aligning with the concept of developing a research plan and executing it.

**Why it matters for multi-agent research assistants:** This survey provides a foundational conceptual framework for autonomous research agents, which can be implemented as multi-agent systems. It clearly outlines the necessary stages for an agent to perform "deep research," from initial planning to final report generation, all driven by iterative interaction with external information.

**Connection to deep research workflow:**
*   **Planning:** The 'Planning' stage is explicitly defined as decomposing a high-level research question into sub-goals and a roadmap.
*   **Query Generation:** 'Question Developing' involves formulating diverse, contextualized retrieval queries.
*   **Search Execution:** 'Web Exploration' describes iteratively collecting and filtering information from external sources.
*   **Result Evaluation:** The iterative collection and filtering in 'Web Exploration' implies ongoing evaluation of retrieved information.
*   **Iterative Follow-up:** The survey emphasizes dynamic and iterative interaction with external knowledge sources, inherently supporting making more queries until sufficient information is gathered.

## 3. AgenticSciML: collaborative multi-agent systems for emergent discovery in scientific machine learning

**Authors/year:** Anon., 2026  
**URL/source:** https://www.nature.com/articles/s44387-026-00102-5  
**Confidence:** High  

**Summary:** AgenticSciML introduces a collaborative multi-agent system comprising over 10 specialized AI agents that work together to propose, critique, and refine scientific machine learning (SciML) solutions. This system leverages structured reasoning, iterative evolution, retrieval-augmented method memory, and ensemble-guided evolutionary search. The agents generate and assess new hypotheses about architectures and optimization procedures, effectively performing a research process for scientific discovery. This iterative and collaborative approach leads to emergent methodological innovations and outperforms single-agent and human-designed baselines.

**Why it matters for multi-agent research assistants:** This paper presents a concrete example of a collaborative multi-agent system engaged in a research-like process (scientific discovery), which involves proposing, critiquing, and refining solutions. It highlights the benefits of specialized agents, structured reasoning, and iterative refinement, directly supporting the paradigm of multi-agent research.

**Connection to deep research workflow:**
*   **Planning:** The system implicitly plans by setting goals for proposing and refining SciML solutions, with agents collaboratively working towards these objectives.
*   **Query Generation:** Agents "generate and assess new hypotheses," which can be seen as an internal form of query generation, exploring different solution spaces or information needs. While not explicit external queries, it is analogous to searching for viable solutions.
*   **Search Execution:** The "retrieval-augmented method memory" indicates a form of information retrieval or search, and "ensemble-guided evolutionary search" can be seen as executing a search for optimal solutions.
*   **Result Evaluation:** Agents "propose, critique, and refine" solutions, which involves continuous evaluation of generated hypotheses and outcomes against specific criteria.
*   **Iterative Follow-up:** The system leverages "iterative evolution" and continuous refinement, indicating that agents repeatedly adjust their approach and generate new hypotheses based on previous assessments, analogous to making more queries until a solution is found.

## 4. Deep Research Agents: A Systematic Examination And Roadmap

**Authors/year:** Yihang Chen et al., 2025  
**URL/source:** https://arxiv.org/html/2506.18096v2  
**Confidence:** High  

**Summary:** This systematic survey defines 'Deep Research (DR) agents' as LLM-powered AI systems for complex, multi-turn informational research tasks, integrating dynamic reasoning, adaptive long-horizon planning, multi-hop information retrieval, iterative tool use, and structured report generation. It provides a taxonomy including multi-agent configurations, with a workflow illustrating user input through optional planning and intent clarification, to iterative tool utilization (offline/online retrieval) and comprehensive report generation. DR agents are noted for greater autonomy, continual reasoning, dynamic task planning, and adaptive real-time interaction compared to RAG or traditional Tool Use. The paper also highlights open challenges and future directions such as asynchronous parallel execution and optimizing multi-agent architectures.

**Why it matters for multi-agent research assistants:** This survey provides a comprehensive definition and overview of 'Deep Research Agents,' explicitly including multi-agent configurations. It outlines the key capabilities, such as adaptive planning and iterative retrieval, that are essential for systems answering complex research questions.

**Connection to deep research workflow:**
*   **Planning:** The survey highlights "adaptive long-horizon planning" and "dynamic task planning" as core capabilities of DR agents, which includes initial intent clarification and workflow generation.
*   **Query Generation:** "Multi-hop information retrieval" and "iterative tool use" necessitate the generation of context-aware queries for different stages of research.
*   **Search Execution:** "Iterative tool utilization (offline/online retrieval)" directly corresponds to executing queries to gather information.
*   **Result Evaluation:** The process of multi-turn informational research and continual reasoning implies an ongoing evaluation of retrieved information to refine understanding and identify further needs.
*   **Iterative Follow-up:** The definition emphasizes "multi-turn informational research tasks" and "iterative tool use," indicating that agents continuously generate and execute queries, evaluating results and adapting their approach until the research question is answered.

## 5. How we built our multi-agent research system

**Authors/year:** Anthropic, 2025  
**URL/source:** https://www.anthropic.com/engineering/multi-agent-research-system  
**Confidence:** High  

**Summary:** This engineering blog details Anthropic's multi-agent research system for Claude, built for open-ended, complex research tasks. It uses an orchestrator-worker pattern: a lead agent analyzes a user query, develops a research plan and strategy, and delegates to specialized subagents. These subagents operate in parallel, iteratively using search tools to gather information. The lead agent then synthesizes findings and decides if further research is required, potentially spawning more subagents or refining the overall strategy. The system includes a CitationAgent for proper attribution. Key to its success is prompt engineering for coordination, focusing on clear delegation, objective setting, task boundaries, and scaling effort based on query complexity. This architecture demonstrates how multi-agent systems can handle dynamic, path-dependent research, iteratively generating and executing queries, and considering results for self-correction and refinement.

**Why it matters for multi-agent research assistants:** This article provides a real-world, production-level example of a multi-agent system designed for complex, open-ended research. It concretely demonstrates the orchestrator-worker pattern and how agents collaborate to develop a plan, execute searches, and iteratively refine their strategy to answer a research question.

**Connection to deep research workflow:**
*   **Planning:** A lead agent "analyzes a user query, develops a research plan and strategy," and delegates tasks, directly fulfilling the planning requirement.
*   **Query Generation:** Specialized subagents "iteratively using search tools" generate queries as part of their delegated tasks. The lead agent can also refine the overall strategy, leading to new query directions.
*   **Search Execution:** Subagents "iteratively using search tools to gather information" directly perform the search execution.
*   **Result Evaluation:** The lead agent "synthesizes findings and decides if further research is required," which is a clear evaluation of the gathered results.
*   **Iterative Follow-up:** The system is designed for "dynamic, path-dependent research," and the lead agent's decision on "if further research is required" explicitly drives the iterative process of making more queries until the research question is answered.

## 6. Multi-Agent Deep Research Architecture

**Authors/year:** Trilogy AI, 2025  
**URL/source:** https://trilogyai.substack.com/p/multi-agent-deep-research-architecture  
**Confidence:** Medium  

**Summary:** This article proposes multi-agent architectures for 'deep research' that continuously build and refine a knowledge base. It outlines specialized agents for planning (Query Planner), parallel search, summarization, and higher-order reasoning, linked by a persistent Knowledge Base. Key concepts include Parallel Tree Search for subtopic decomposition, Cycling Summarization & Reasoning for refining strategy, and Iterative Feedback Loops. It details a pipeline (Planner -> Retriever -> Extractor -> Synthesizer) and a hierarchical 'Tree of Thoughts' approach for recursive problem breakdown and synthesis, enabling parallel search. The system emphasizes domain-specific agents and distinct roles like Researcher, Analyst, Writer, and Critic, which collaborate via shared memory or a supervisor, leveraging frameworks like Autogen. This addresses the iterative process of query generation, execution, considering results, and refining the plan.

**Why it matters for multi-agent research assistants:** This article provides a detailed architectural blueprint for multi-agent deep research systems, outlining specific agent roles and a structured workflow that directly supports developing a research plan, executing queries, evaluating results, and iterating. Its focus on parallel search and continuous knowledge refinement is particularly relevant.

**Connection to deep research workflow:**
*   **Planning:** The architecture includes a dedicated 'Query Planner' agent and concepts like 'Parallel Tree Search for subtopic decomposition' and a 'Planner -> Retriever -> Extractor -> Synthesizer' pipeline, all central to developing a research plan.
*   **Query Generation:** The 'Retriever' agent, guided by the 'Query Planner,' is responsible for generating and executing queries.
*   **Search Execution:** The 'Retriever' agent executes searches, and the architecture supports 'parallel search.'
*   **Result Evaluation:** The 'Extractor' and 'Summarization & Reasoning' components are responsible for processing retrieved information, evaluating its relevance, and identifying knowledge gaps. The 'Critic' agent also performs evaluation.
*   **Iterative Follow-up:** Concepts like 'Cycling Summarization & Reasoning' and 'Iterative Feedback Loops' explicitly describe the process of refining strategy and making more queries based on previous results until the research question is answered.

## 7. Navigating Multi-Agentic Workflows for Problem-Solving

**Authors/year:** Leslie Lim (via Tan Yan Chi), 2024  
**URL/source:** https://medium.com/d-classified/navigating-multi-agentic-workflows-for-problem-solving-fe3d9e3d5728  
**Confidence:** Medium  

**Summary:** This article explores multi-agent workflows using frameworks like AutoGen and LangGraph for complex problem-solving. It details two specific workflows: 'Plan-and-Execute' and 'Reasoning Without Observations (ReWOO)'. In Plan-and-Execute, a main planner devises a plan, an action agent iteratively executes subtasks, and a replanner continually reevaluates and refines the plan based on outputs. ReWOO, an optimized version, allows action agents to execute tasks more independently by providing in-context learning, feeding results to a solver agent for synthesis. Both workflows demonstrate iterative query execution, consideration of results, and dynamic plan refinement, directly applicable to answering research questions. It also highlights multi-agent coordination and loop mitigation strategies.

**Why it matters for multi-agent research assistants:** This article provides practical insights into multi-agent workflows (Plan-and-Execute, ReWOO) that are directly applicable to the research question. It demonstrates how different agents can collaborate through iterative task execution, result evaluation, and dynamic plan refinement, providing concrete patterns for designing research-answering systems.

**Connection to deep research workflow:**
*   **Planning:** The 'Plan-and-Execute' workflow starts with a main planner devising a plan, and a 'replanner' continually reevaluates and refines it, addressing the planning aspect.
*   **Query Generation:** Action agents iteratively execute subtasks, which involves generating specific actions or queries to fulfill those subtasks.
*   **Search Execution:** The action agents "iteratively executes subtasks," which includes performing information gathering or tool use, analogous to query execution.
*   **Result Evaluation:** The 'replanner' continually reevaluates and refines the plan "based on outputs," signifying evaluation of intermediate results. In ReWOO, a 'solver agent' synthesizes results from action agents.
*   **Iterative Follow-up:** Both workflows are inherently iterative; the replanner continuously refines the plan, and action agents continue execution until the problem is solved, directly supporting making more queries or taking more actions.

## 8. Let the Agent Search: Autonomous Exploration Beats Rigid Workflows in Temporal Question Answering

**Authors/year:** Xufei Lv et al., 2026  
**URL/source:** https://arxiv.org/html/2603.01853v1  
**Confidence:** High  

**Summary:** This paper proposes AT2QA, an autonomous, training-free agent for Temporal Knowledge Graph Question Answering (TKGQA). It empowers an LLM to act as a fully autonomous agent that iteratively interacts with a temporal knowledge graph via a general search tool for dynamic retrieval. The system implements an evidence-driven verification and rollback mechanism for self-correction, mitigating cascading errors in multi-hop reasoning. It emphasizes liberating the LLM's planning and reasoning capabilities from rigid, human-designed workflows, allowing it to dynamically verify evidence and self-correct its reasoning trajectory. While highly relevant to iterative query execution and self-correction, the core system described is based on a single autonomous agent rather than a multi-agent system.

**Why it matters for multi-agent research assistants:** While this paper focuses on a single autonomous agent, it offers valuable mechanisms for iterative query execution, dynamic planning, evidence-driven self-correction, and result consideration—all crucial components that can be adopted or adapted within a multi-agent system for robust research answering.

**Connection to deep research workflow:**
*   **Planning:** The system allows the LLM agent to dynamically verify evidence and self-correct its reasoning trajectory, which includes adaptive, non-rigid planning during the process.
*   **Query Generation:** The agent "iteratively interacts with a temporal knowledge graph via a general search tool," implying continuous generation of queries.
*   **Search Execution:** Interacting with the knowledge graph "via a general search tool for dynamic retrieval" directly means executing queries.
*   **Result Evaluation:** It features an "evidence-driven verification and rollback mechanism for self-correction," which is a strong form of evaluating results and identifying errors.
*   **Iterative Follow-up:** The core is an "autonomous agent that iteratively interacts" and "self-correct[s] its reasoning trajectory," demonstrating a strong iterative feedback loop of making more queries based on evaluations until the question is answered.
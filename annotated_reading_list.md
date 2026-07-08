# Annotated Reading List

## 1. Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution

**Authors/year:** Xing Zhang et al., 2026  
**URL/source:** https://arxiv.org/html/2603.11445v2  
**Confidence:** High  

**Summary:** This paper introduces Verified Multi-Agent Orchestration (VMAO), an LLM-based multi-agent framework designed for complex query resolution, particularly in market research. VMAO operates through an iterative Plan-Execute-Verify-Replan loop. It decomposes a complex query into a Directed Acyclic Graph (DAG) of sub-questions, assigns them to domain-specific agents, and executes them in parallel. A key feature is the LLM-based verifier which evaluates result completeness and triggers adaptive replanning (generating new sub-questions or retrying existing ones) to address identified gaps. The system employs configurable stop conditions to balance answer quality and resource usage, culminating in a synthesized answer with source attribution. The framework emphasizes orchestration-level verification as a critical mechanism for multi-agent quality assurance.

**Why it matters for multi-agent research assistants:** This paper directly presents a concrete multi-agent framework that encapsulates the entire iterative research process, from initial planning to final synthesis, with a strong emphasis on verification and adaptive replanning to ensure quality and completeness.

**Connection to deep research workflow:**
*   **Planning:** The system develops a research plan by decomposing a complex query into a DAG of sub-questions.
*   **Query Generation & Search Execution:** Domain-specific agents are assigned sub-questions, generate relevant queries, and execute them, often in parallel.
*   **Result Evaluation:** An LLM-based verifier critically evaluates the completeness and quality of the results obtained from executed queries.
*   **Iterative Follow-up:** The verification step triggers adaptive replanning, leading to the generation of new queries or retrying existing ones if gaps or inconsistencies are identified, repeating until stop conditions are met.

## 2. How we built our multi-agent research system

**Authors/year:** Anthropic, 2025  
**URL/source:** https://www.anthropic.com/engineering/multi-agent-research-system  
**Confidence:** High  

**Summary:** Anthropic's Research system employs an orchestrator-worker multi-agent architecture to enable Claude to perform complex, open-ended research. A lead agent analyzes the user's query, develops a research strategy, and spawns specialized subagents to explore different aspects simultaneously. These subagents iteratively use search tools, evaluate their findings using 'interleaved thinking', and return results to the lead agent. The lead agent synthesizes these results and decides if further research is necessary, which may involve refining its strategy or creating additional subagents. The system dynamically adapts based on discoveries, overcoming single context window limitations through parallelization. Internal evaluations showed this multi-agent system outperformed a single-agent by 90.2% on internal research evaluations, though it uses significantly more tokens (e.g., 15x more than chat interactions). Once enough information is collected, a CitationAgent ensures proper attribution before the final research report is returned to the user.

**Why it matters for multi-agent research assistants:** This provides a real-world example and architectural blueprint from a leading AI lab for a multi-agent system specifically designed for open-ended, complex research, mirroring the exact capabilities described in the research question.

**Connection to deep research workflow:**
*   **Planning:** A lead agent analyzes the initial query and develops an overarching research strategy, including spawning specialized subagents.
*   **Query Generation & Search Execution:** Subagents generate and execute queries using search tools to explore specific aspects of the research question.
*   **Result Evaluation:** Subagents evaluate their findings through "interleaved thinking," and the lead agent synthesizes these results.
*   **Iterative Follow-up:** The lead agent decides if further research is needed, dynamically adapting the strategy or creating more subagents based on prior discoveries, until sufficient information is collected.

## 3. Deep Research Agents: A Systematic Examination And Roadmap

**Authors/year:** Yihang Chen et al., 2025  
**URL/source:** https://arxiv.org/html/2506.18096v2  
**Confidence:** High  

**Summary:** This survey paper defines 'Deep Research (DR) agents' as LLM-powered AI systems designed for complex, multi-turn informational research tasks. These agents integrate dynamic reasoning, adaptive long-horizon planning, multi-hop information retrieval, and iterative tool use to acquire, aggregate, and analyze external information, ultimately generating structured analytical reports. The paper presents a taxonomy that includes multi-agent configurations, highlighting their ability to handle complex, evolving, and knowledge-intensive research scenarios with greater autonomy and continual reasoning compared to traditional RAG or tool-use systems. It provides a critical evaluation of current benchmarks for DR agents, identifying limitations such as restricted external knowledge access, sequential execution inefficiencies, and misaligned evaluation metrics, while outlining future directions for optimizing multi-agent architectures and asynchronous parallel execution.

**Why it matters for multi-agent research assistants:** This survey provides a foundational understanding and systematic overview of the very type of agents described, explicitly covering their multi-agent configurations, iterative nature, and capacity for generating comprehensive answers. It also highlights current challenges and future directions.

**Connection to deep research workflow:**
*   **Planning:** DR agents are characterized by adaptive long-horizon planning to tackle complex research tasks.
*   **Query Generation & Search Execution:** They engage in multi-hop information retrieval and iterative tool use to acquire external information, which involves generating and executing queries.
*   **Result Evaluation:** They aggregate and analyze acquired information, forming the basis for evaluating results.
*   **Iterative Follow-up:** The definition of DR agents includes iterative information acquisition and analysis until structured analytical reports can be generated, implying repeated cycles of querying and refinement.

## 4. Autonomous Agents for Scientific Discovery: Orchestrating Scientists, Language, Code, and Physics

**Authors/year:** Lianhao Zhou et al., 2025  
**URL/source:** https://arxiv.org/html/2510.09901v1  
**Confidence:** High  

**Summary:** This paper surveys LLM-based agents in the context of scientific discovery, covering the entire lifecycle from hypothesis generation and experimental design/execution to result analysis and refinement. It emphasizes that multi-agent systems can achieve collective intelligence surpassing single agents, emulating human research teams. The scientific discovery process, as facilitated by these agents, is inherently iterative, involving adaptive planning, data acquisition, analysis of results, and subsequent refinement or further experimentation based on findings. This iterative nature aligns with the concept of agents making more queries and refining their approach until a discovery is made or a research question is answered.

**Why it matters for multi-agent research assistants:** This survey highlights that the scientific discovery process, a prime example of complex research, is inherently iterative and greatly enhanced by multi-agent systems that emulate human research teams, directly supporting the core capabilities of the desired system.

**Connection to deep research workflow:**
*   **Planning:** The agents are involved in hypothesis generation and experimental design, which constitutes the initial research plan.
*   **Query Generation & Search Execution:** Data acquisition and experimental execution involve generating and executing queries against various tools or real-world systems.
*   **Result Evaluation:** The agents perform analysis of results obtained from experiments and data acquisition.
*   **Iterative Follow-up:** The process is described as inherently iterative, involving subsequent refinement or further experimentation based on findings, meaning agents make more queries and refine their approach until a research question is answered.

## 5. Multi-Agent Collaboration Mechanisms: A Survey of LLMs

**Authors/year:** Khanh-Tung Tran et al., 2025  
**URL/source:** https://arxiv.org/html/2501.06322v1  
**Confidence:** High  

**Summary:** This survey provides an extensive examination of LLM-based Multi-Agent Systems (MASs), focusing on their collaborative aspects and mechanisms. It introduces an extensible framework to characterize collaboration based on actors, types (e.g., cooperation, competition, coopetition), structures (e.g., peer-to-peer, centralized, distributed), strategies (e.g., role-based, model-based), and coordination protocols. The paper discusses various collaboration channels, including a 'debate' mechanism where agents critically evaluate each other's input to achieve collective intelligence in applications like question-answering. It highlights how MASs enhance capabilities like knowledge memorization, long-term planning, and interaction efficiency by distributing tasks and sharing knowledge.

**Why it matters for multi-agent research assistants:** This paper offers a comprehensive framework for understanding how agents in a multi-agent system coordinate and collaborate, which is crucial for orchestrating complex research tasks and handling potentially conflicting information during the iterative process.

**Connection to deep research workflow:**
*   **Planning:** MASs enhance long-term planning through distributed task management and knowledge sharing among collaborating agents.
*   **Query Generation & Search Execution:** Collaboration mechanisms facilitate efficient distribution of tasks, which includes generating and executing queries, potentially in parallel or through specialized agents.
*   **Result Evaluation:** Mechanisms like 'debate' allow agents to critically evaluate each other's input and findings, refining results and achieving collective intelligence.
*   **Iterative Follow-up:** The collaborative nature, especially through mechanisms like debate, inherently supports iterative refinement where agents continuously adjust their approach and queries based on shared and evaluated knowledge until a robust answer is formed.

## 6. Conflict Data Fusion in a Multi-Agent System Premised on the Base Basic Probability Assignment and Evidence Distance

**Authors/year:** 2021  
**URL/source:** https://www.mdpi.com/1099-4300/23/7/820  
**Confidence:** High  

**Summary:** This paper addresses the challenge of fusing conflicting information in Multi-Agent Information Fusion (MAIF) systems, where multiple agents may provide inconsistent conclusions due to differing reasoning models or uncertain environments. It focuses on the limitations of traditional Dempster\u2013Shafer (D-S) evidence theory when dealing with highly conflicting data and proposes a new conflict data fusion method. This method uses a new base basic probability assignment (bBPA) and evidence distance to construct and refine the initial belief degree of each agent, calculate information volume, modify reliability, and then apply the Dempster combination rule to obtain a more accurate fusion result. Numerical examples demonstrate the effectiveness of this approach in improving identification accuracy.

**Why it matters for multi-agent research assistants:** While not LLM-centric, this paper is highly relevant as it provides specific algorithmic methods for synthesizing potentially conflicting or inconsistent results from multiple agents, a common challenge in complex research where different agents might find contradictory information or interpret it differently.

**Connection to deep research workflow:**
*   **Planning:** While not directly about research planning, the framework implicitly supports a plan to handle data from various sources (agents) effectively.
*   **Query Generation & Search Execution:** Assumes data has been acquired by agents (through implicit queries or observations).
*   **Result Evaluation:** Directly addresses the evaluation of results from multiple agents, particularly when these results are conflicting or uncertain. The proposed method refines initial belief degrees and modifies reliability.
*   **Iterative Follow-up:** By providing a mechanism to fuse conflicting evidence and improve accuracy, it supports the ability to "consider results" from multiple agents and reach a more refined conclusion, potentially informing subsequent queries or adjustments to the overall research plan if inconsistencies persist.

## 7. What Is the AI Agent Loop? The Core Architecture Behind Autonomous AI Systems

**Authors/year:** Oracle Blog, 2026  
**URL/source:** https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems  
**Confidence:** High  

**Summary:** This article defines the 'AI Agent Loop' as the iterative execution cycle central to autonomous AI systems, distinct from single-pass chatbots. The loop consists of five stages: Perceive, Reason, Plan, Act, and Observe, repeating until a task is complete. It emphasizes that major AI companies have converged on this architecture, often leveraging frameworks like ReAct (Reason-Act). This architecture enables agents to handle multi-step tasks by dynamically adapting to intermediate results and recovering from failures, directly supporting the iterative nature of complex research. It notes that multi-agent systems, while offering enhanced capabilities, can consume significantly more tokens (up to 15x) compared to standard chat interactions.

**Why it matters for multi-agent research assistants:** This article defines the fundamental iterative architecture (the 'Agent Loop') that underpins all autonomous AI systems, including multi-agent research systems. It provides the core conceptual model for how agents develop plans, execute actions (queries), consider results, and iterate.

**Connection to deep research workflow:**
*   **Planning:** The 'Plan' stage of the agent loop directly involves developing a strategy for the next steps.
*   **Query Generation & Search Execution:** The 'Act' stage corresponds to agents taking actions, which in a research context includes generating and executing queries against tools or information sources.
*   **Result Evaluation:** The 'Perceive' and 'Observe' stages involve receiving and interpreting feedback or results from actions taken. The 'Reason' stage evaluates these observations in light of the overall goal.
*   **Iterative Follow-up:** The entire 'Agent Loop' is inherently iterative, repeating the Perceive-Reason-Plan-Act-Observe cycle until the research question is answered or the task is complete, allowing for dynamic adaptation and making more queries as needed.
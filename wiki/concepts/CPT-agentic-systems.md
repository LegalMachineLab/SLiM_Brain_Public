---
id: "CPT-agentic-systems"
label: "Agentic systems"
status: "anchor"
concept_type: "technique_class"
definition: "Autonomous or semi-autonomous AI agents that plan, act, negotiate, or transact on behalf of users."
aliases: []
broader: []
sources: ["SRC-0020", "SRC-0025", "SRC-0040", "SRC-0047", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Agentic systems

_Status: anchor; family: technique_class._

## Definition

Autonomous or semi-autonomous AI agents that plan, act, negotiate, or transact on behalf of users.

Conceptual claims on this concept, each with its source:
- Getir Yaman et al. (2023): By enabling the operationalisation of SLEEC requirements for autonomous agents, a formal specification, validation and verification framework complements the international efforts to define ethical principles for AI and autonomous systems (such as the UNESCO and OECD recommendations) and work that elicits SLEEC requirements from normative principles and stakeholder needs. [CLM-0025-017]
- Mandal and Sinha (2026): Traditional SaaS provides structured, rules-based digital tools that humans navigate manually to generate an output, whereas AI-native or AI-enabled systems act as autonomous or semi-autonomous collaborators that understand human intent, execute complex workflows independently and deliver outcomes; among the latter, AI-native systems built from scratch with AI at their core have an edge over AI-enabled legacy platforms that add AI features onto an existing codebase. [CLM-0040-002]
- Mandal and Sinha (2026): A vertical harness — an orchestrator custom-built around the vocabulary, artifacts and control flow of a specific industry, with specialised tools and integrations into legacy systems — is a medium moat: it is more valuable than a horizontal harness hosting a vertical workflow because it provides greater reliability, security and efficiency, and legacy-system integrations create significant durable value, but it is maintainable largely through engineering effort that a well-funded rival can match over time. [CLM-0040-009]
- Mandal and Sinha (2026): Embedded judgment — encoding the judgment, taste and experience of expert practitioners as business logic that guides decisions at critical points in complex multi-step workflows — is the highest moat: although very hard to codify today, it can be learned through a flywheel in which the system observes the decisions of the best practitioners and refines its own judgment, so the moat compounds with every additional customer and observed decision and becomes increasingly difficult for competitors to replicate. [CLM-0040-017]

## Claims about the concept

### Descriptive

**general**

- Getir Yaman et al. (2023) state that Although social, legal, ethical, empathetic and cultural (SLEEC) requirements for autonomous agents are recognised as increasingly important, there is currently very little support for their elicitation, specification, validation and verification; existing research is promising but covers only specific aspects of the problem. [CLM-0025-001]. — jurisdiction: general; basis: literature
- Getir Yaman et al. (2023) state that Existing formal verification approaches for autonomous systems mostly focus on the agents' safety requirements, and prior work on verifying ethical and legal constraints of robots does not address the operationalisation of such requirements and provides no notation dedicated to encoding SLEEC-related concerns as requirements; the SLEEC framework is distinctive in addressing the operationalisation of norms while leaving the identification of rules to complementary work. [CLM-0025-016]. — jurisdiction: general; basis: literature
- Getir Yaman et al. (2023) state that Many autonomous systems learn, adapt and evolve in operation, for example in response to changes in their environment, and therefore cannot be fully verified at development time; runtime verification of autonomous-agent decisions against SLEEC rules and online synthesis of SLEEC-compliant adaptation plans are needed to cover this evolution. [CLM-0025-018]. — jurisdiction: general; basis: argument
- Mandal and Sinha (2026) state that As matters stand today, human judgment and direction are still required to guide AI agents in complex, open-ended projects: humans must define what problems to address, what to research and where to narrow down, and large performance gaps remain when a model must itself choose goals for research focus and engineering. [CLM-0040-018]. — jurisdiction: general [jurisdiction inferred]; basis: literature

**undetermined**

- Mandal and Sinha (2026) state that In legal AI the moat is not the underlying model, since GPT, Claude or Gemini can often be used interchangeably; it lies partly in the harness — the layer that pulls matter context, applies legal-specific reasoning, calls trusted legal tools in order and writes work product back into the firm's systems under professional governance rules — and in the curated legal tools and document-management, research and content integrations that create a barrier to entry. [CLM-0040-010]. — jurisdiction: undetermined; basis: argument

### Normative

**general**

- Zhu et al. (2025) argue that Users should be careful when delegating business decisions to LLM agents, because although automating negotiations and transactions can enhance transactional efficiency, it also poses nontrivial risks to consumer markets. [CLM-0020-003]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

### Empirical

**general**

- Zhu et al. (2025) report that Dealmaking between LLM agents acting on behalf of consumers and merchants in consumer settings is an inherently imbalanced game: different LLM agents show large disparities in their ability to obtain the best deals for the users they represent. [CLM-0020-001]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Zhu et al. (2025) report that Behavioral anomalies of LLMs might lead to financial loss for the users they act for when LLM agents are deployed in real-world decision-making scenarios, for example through overspending or making unreasonable deals. [CLM-0020-002]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Getir Yaman et al. (2023) report that In the robotic assistive dressing (RAD) case study, the SLEEC framework found the four expert-defined rules to be free of conflict and redundancy and the RoboChart design to satisfy three of them, but detected a violation of the fourth rule: an extra design requirement to call support within one minute of a user fall is incompatible with the rule requiring a two-minute delay for a retry agreement before support is called when dressing is abandoned. [CLM-0025-014]. — jurisdiction: general; basis: dataset_or_experiment

**geographical_proxy:RU**

- Gridin (2026) report that Deploying deterministic linear agents to monitor and execute specific tasks is exponentially cheaper, faster and more secure than attempting to train a monolithic LLM to perform flawlessly across all domains, and multi-agent systems inherently provide the 'Explainable Monitoring Layer' regulators require because the interaction between discrete agents leaves a verifiable algorithmic trail. [CLM-0049-045]. — jurisdiction: geographical_proxy:RU [jurisdiction inferred]; basis: literature

### Conceptual

**general**

- Getir Yaman et al. (2023) argue that By enabling the operationalisation of SLEEC requirements for autonomous agents, a formal specification, validation and verification framework complements the international efforts to define ethical principles for AI and autonomous systems (such as the UNESCO and OECD recommendations) and work that elicits SLEEC requirements from normative principles and stakeholder needs. [CLM-0025-017]. — jurisdiction: general; basis: argument
- Mandal and Sinha (2026) argue that Traditional SaaS provides structured, rules-based digital tools that humans navigate manually to generate an output, whereas AI-native or AI-enabled systems act as autonomous or semi-autonomous collaborators that understand human intent, execute complex workflows independently and deliver outcomes; among the latter, AI-native systems built from scratch with AI at their core have an edge over AI-enabled legacy platforms that add AI features onto an existing codebase. [CLM-0040-002]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mandal and Sinha (2026) argue that A vertical harness — an orchestrator custom-built around the vocabulary, artifacts and control flow of a specific industry, with specialised tools and integrations into legacy systems — is a medium moat: it is more valuable than a horizontal harness hosting a vertical workflow because it provides greater reliability, security and efficiency, and legacy-system integrations create significant durable value, but it is maintainable largely through engineering effort that a well-funded rival can match over time. [CLM-0040-009]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Mandal and Sinha (2026) argue that Embedded judgment — encoding the judgment, taste and experience of expert practitioners as business logic that guides decisions at critical points in complex multi-step workflows — is the highest moat: although very hard to codify today, it can be learned through a flywheel in which the system observes the decisions of the best practitioners and refines its own judgment, so the moat compounds with every additional customer and observed decision and becomes increasingly difficult for competitors to replicate. [CLM-0040-017]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Predictive

**GB**

- Briggs of Westbourne (2026) argue that The arrival of agentic AI makes it by no means implausible that an AI platform could soon be tasked with the whole process of reaching a decision on a case and producing at least the first draft of the judgment; if the judge's only role were to approve the AI's plan of action and review the draft judgment, it is doubtful whether the public expectation that a human judge decides the case would really be fulfilled, and a judicial role reduced to reviewer rather than initiator would be poor at developing or maintaining judicial skills. [CLM-0047-015]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**general**

- Mandal and Sinha (2026) argue that With continued advancement of foundation models, vertical application solutions could next use their acquired judgment to solve open-ended problems without human direction — including recursively rebuilding the application to meet users' needs without human feedback — so that the application would rely on its own rather than human judgment to evolve and differentiate itself; this is not yet a reality but could be in the foreseeable future. [CLM-0040-019]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Methodological

**general**

- Getir Yaman et al. (2023) argue that SLEEC (social, legal, ethical, empathetic and cultural) rules for autonomous agents can be given end-to-end tool-supported formal treatment through a framework comprising a domain-specific language for specifying the rules and their defeaters, a formal semantics for that language in the process algebra tock-CSP, and methods for detecting conflicts and redundancy within a rule set and for verifying an agent's compliance with the rules. [CLM-0025-002]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that Compliance of an autonomous agent design with a SLEEC rule can be verified as traces refinement in tock-CSP, with the specification given by the process capturing the semantics of the rule: the events of the system under verification must occur in the order and time the rule specifies, projected onto the rule's alphabet and with matching values of the measures the rule reads, while the conforming system may engage in additional events and read additional measures. [CLM-0025-011]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that When a system design is found to violate a SLEEC rule, the SLEEC and requirements stakeholders have to be consulted to decide the outcome; possible resolutions include a domain expert relaxing an over-strict design deadline, or distinguishing capabilities so that different types of call to support are represented by distinct events. [CLM-0025-015]. — jurisdiction: general; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 5; claims: 19.

**By contribution type**

| value | sources |
|---|---|
| normative | 3 |
| technical | 3 |
| theoretical | 3 |
| doctrinal | 2 |
| empirical_qualitative | 2 |
| empirical_quantitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |
| US | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| GB | 1 |
| geographical_proxy:RU | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2026 | 3 |
| 2023 | 1 |
| 2025 | 1 |

## What the sources do not address

- No interpretive claim on CPT-agentic-systems. [ABS-1367] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.

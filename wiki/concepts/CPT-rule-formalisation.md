---
id: "CPT-rule-formalisation"
label: "Rule formalisation"
status: "anchor"
concept_type: "legal_task"
definition: "Translating legal rules or statutes into formal, machine-executable representations."
aliases: []
broader: []
sources: ["SRC-0003", "SRC-0009", "SRC-0014", "SRC-0025", "SRC-0032", "SRC-0037", "SRC-0049", "SRC-0050"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Rule formalisation

_Status: anchor; family: legal_task._

## Definition

Translating legal rules or statutes into formal, machine-executable representations.

Conceptual claims on this concept, each with its source:
- Holzenberger et al. (2020): In the broader context of computational statutory reasoning, a hand-built Prolog solver has three limitations: producing it requires domain experts while automatic generation remains an open question; translating natural language into facts requires semantic parsing capabilities; and small mistakes can lead to catastrophic failure. A machine-learning approach that replaces logical operators and explicit structure with learned dense representations can, by contrast, be adapted to new legislation and new domains automatically. [CLM-0003-007]
- Getir Yaman et al. (2023): A distinctive feature of the SLEEC language is that it can specify time constraints on normative rules: time budgets within which a required response must occur, and required alternative responses when a timeout occurs. [CLM-0025-004]
- Getir Yaman et al. (2023): By enabling the operationalisation of SLEEC requirements for autonomous agents, a formal specification, validation and verification framework complements the international efforts to define ethical principles for AI and autonomous systems (such as the UNESCO and OECD recommendations) and work that elicits SLEEC requirements from normative principles and stakeholder needs. [CLM-0025-017]
- Horner et al. (2025): Every formal encoding of a legal provision is an interpretation, and a true gold standard would have to correspond to the authentic interpretation, which only the judiciary can provide and only for provisions actually disputed in court; therefore in some jurisdictions a true gold standard for legal formalization cannot exist, and any gold standard further depends on the coders' understanding of legal intent, context and encoding style. [CLM-0032-012]
- Wang et al. (2026): Neuro-symbolic approaches that translate legal text into formal representations expose a key limitation: formal reasoning requires all relevant assumptions to be explicit, whereas legal text is inherently underspecified and legal reasoning depends on background assumptions and contextual interpretation (for example, contractual obligations are typically understood as excluding illegal conduct even when unstated), so such assumptions must be explicitly encoded in formal systems. [CLM-0037-012]
- Gridin (2026): Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006]

## Claims about the concept

### Descriptive

**general**

- Janatian et al. (2023) state that Encoding legislative text in a formal representation is a prerequisite for tasks in AI and Law such as rule-based legal expert systems, but understanding and encoding a legal rule is not easy, may require legal training and considerable time, and can therefore represent a bottleneck in the creation of legal decision support tools. [CLM-0009-001]. — jurisdiction: general; basis: literature
- Janatian et al. (2023) state that Using large language models to directly convert legislative text into a structured legal representation (a pathway of criteria and conclusions) is, to the authors' knowledge, the first attempt of its kind; earlier automatic structure-extraction work relied on linguistic, morphological, rule-based and parser approaches. [CLM-0009-002]. — jurisdiction: general; basis: literature
- Janatian et al. (2023) state that Structuring the pathway of criteria and conclusions is only one part of building a JusticeBot legal decision support tool; the work also requires simplifying the content, drafting layperson explanations of the individual criteria, and adding case-law summaries to the question blocks. [CLM-0009-014]. — jurisdiction: general; basis: literature
- T.Y.S.S. et al. (2024) state that Modern large language models help alleviate the knowledge acquisition bottleneck of knowledge-based legal domain models by enabling (semi-)automated construction of rule-based structures, but whether LLMs can systematize large complexes of legal source material into well-formed, legally correct representations remains an open question. [CLM-0014-008]. — jurisdiction: general; basis: literature
- Getir Yaman et al. (2023) state that Although social, legal, ethical, empathetic and cultural (SLEEC) requirements for autonomous agents are recognised as increasingly important, there is currently very little support for their elicitation, specification, validation and verification; existing research is promising but covers only specific aspects of the problem. [CLM-0025-001]. — jurisdiction: general; basis: literature
- Horner et al. (2025) state that Manual encoding of legal provisions into machine-readable form is a knowledge representation bottleneck: an experienced coder encodes only about 4 to 5 pages per day, encoding large regulatory frameworks raises burnout concerns, and parallel encoding by a team very likely produces mutually incompatible parts whose reconciliation carries considerable overhead, so there is a pressing need for tools that assist with encoding legal instruments. [CLM-0032-016]. — jurisdiction: general; basis: literature
- Horner et al. (2025) state that Few prior efforts have addressed the formalization of legal text with the granularity and formal logic representation of a full Defeasible Deontic Logic encoding: recent LLM-based work on legal formalization has been confined to very small scales, such as a single article of the European Arrest Warrant Framework Decision or four rules of the UK Highway Code translated into Prolog via Logical English. [CLM-0032-017]. — jurisdiction: general; basis: literature

### Interpretive

**US**

- Holzenberger et al. (2020) read Internal Revenue Code (IRC) as follows: The US Internal Revenue Code can be framed as a set of predicates formulated in human language; because the language of the law has an open texture, determining whether a subsection applies and identifying and filling the slots it mentions is particularly challenging for a computer-based system, which makes the Code an excellent corpus for building systems that reason with rules specified in natural language and have good language understanding capabilities. [CLM-0003-004]. — jurisdiction: US; basis: argument

### Normative

**general**

- Neumann et al. (2026) argue that Governing generative AI by natural language should be approached cautiously, because writing rules that govern machines requires different approaches than writing rules that govern humans. [CLM-0050-011]. — jurisdiction: general; basis: argument

### Empirical

**general**

- Wang et al. (2026) report that The central challenge for faithful legal reasoning, by humans and LLMs alike, is that it is fundamentally unclear which assumptions are permissible: the boundary between valid inference and unjustified assumption is ambiguous. LLMs resolve this ambiguity by injecting ungrounded assumptions, while formal methods expose it through conservative reasoning. [CLM-0037-011]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment

**geographical_proxy:AU**

- Horner et al. (2025) report that With suitable prompting and architectural configurations, large language models can produce Defeasible Deontic Logic formalizations of legal norms that align closely with expert-crafted representations, so that they can assist in extracting semantically valid and logically coherent deontic rules from unstructured legal text. [CLM-0032-001]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that On metrics recalculated to reflect the actual number of rules and atoms in the gold standard, LLM-based formalization of the TCP Code into Defeasible Deontic Logic outperforms the manually supervised NLP pipeline of Dragoni et al. (2017) across nearly all evaluation settings; the only exception is precision in the term identification task, where Dragoni et al. score higher. [CLM-0032-002]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that The reported evaluation figures of Dragoni et al. (2017) are internally inconsistent and their gold-standard counts are understated: on the numbers they report (49 correct of 65 terms) recall is 75.38% rather than the claimed 90.78% and F1 is 79.03% rather than 86.74%, and the gold standard for Sections 8.2.1(a)-(c) of the TCP Code contains 69 terms and 52 rules rather than the reported 65 terms and 36 rules. [CLM-0032-003]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that Among prompting and training strategies for formalizing legal text into Defeasible Deontic Logic, prompt engineering combining few-shot learning with Chain-of-Instructions prompting on single law snippets yields the most promising results; formalizing all law snippets in a single step and fine-tuning bring no measurable gains, a two-step pipeline of atom extraction followed by rule generation degrades output quality, and only a two-step pipeline with a refinement stage after rule generation yields a modest improvement. [CLM-0032-004]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that Providing multiple law snippets to the LLM simultaneously does not improve formalization into Defeasible Deontic Logic over single-snippet prompting: including the full formalization history yields marginally lower success scores and no better atom reuse, supplying lists of previously used atom names increases reuse but produces more hallucinations, and formalizing all snippets in one interaction yields less detailed formalizations in which distinct facts are merged into single rules. [CLM-0032-005]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that Fine-tuning GPT-4o and GPT-4.1 on a limited set of annotated law-snippet formalizations does not reliably improve formalization into Defeasible Deontic Logic: GPT-4o improved only slightly after a single epoch and then declined with further epochs, indicating overfitting, while fine-tuned GPT-4.1 performed worse than the base model. [CLM-0032-006]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that A two-stage pipeline that first extracts atom names with a separate LLM and then generates Defeasible Deontic Logic rules from them performs significantly worse than single-stage Chain-of-Instructions prompting with newer models, and the primary source of its errors lies in the atom extraction stage, which frequently generates superfluous atoms. [CLM-0032-007]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that A refinement step in which Claude Sonnet 4 jointly re-processes all generated Defeasible Deontic Logic rules to consolidate duplicate or inconsistent atom names into a unified vocabulary modestly improves formalization quality and increases consistency of atom names across law snippets; other models (o3, GPT-4.1, GPT-4o, DeepSeek-R1) used for the same refinement step gave unsatisfactory results, returning partial output or excessively long atom names. [CLM-0032-008]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment
- Horner et al. (2025) report that Newly released LLMs generally outperform their predecessors at formalizing legal text into Defeasible Deontic Logic: GPT-4.1 outperforms GPT-4o and DeepSeek-R1 (0528) outperforms the earlier DeepSeek-R1, though the trend does not extend to DeepSeek-V3; Claude Sonnet 4 performs excellently with Extended Thinking enabled but notably poorly without it. [CLM-0032-009]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment

**geographical_proxy:CA-QC**

- Janatian et al. (2023) report that GPT-4-generated pathways from 40 articles of the Civil Code of Quebec were rated by annotators as textually accurate in 92.5% of cases, complete in 72.5% and free of hallucinated criteria or conclusions in 87.5%; 40% were rated directly usable, a further 50% as needing only slight adjustment, and none as useless. [CLM-0009-004]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment
- Janatian et al. (2023) report that In a blind comparison, annotators' overall preference was evenly split between GPT-4-generated and manually created pathways: 60% of generated pathways were rated equivalent to or better than manual ones overall and on logical structure, and on reflecting the textual content of the law only 25% of ratings preferred the manual pathway. [CLM-0009-005]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment
- Janatian et al. (2023) report that The quality of LLM-generated pathways decreases with the difficulty of the legislative article: articles rated difficult by annotators generally received lower scores, and the model's ability compares favourably to human annotators especially for easy articles, while for difficult articles it sometimes misses important elements or bases its analysis on assumptions not in the text. [CLM-0009-006]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment
- Janatian et al. (2023) report that Part of the variation in the quality of generated pathways stems from the ambiguity of the legal articles themselves: statutory language is not always clear enough to yield an unambiguous interpretation, doctrine, court cases and domain expertise may be needed to settle it, and when an article was ambiguous the model occasionally relied on reasonable assumptions not contained in the article. [CLM-0009-007]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment
- Janatian et al. (2023) report that Even for clear articles there is often no single right way to split criteria and conclusions into pathway elements; such non-erroneous structural differences explain the low exact correspondence between manually and automatically created pathways without necessarily reducing the usefulness of the generated pathway. [CLM-0009-008]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment
- Janatian et al. (2023) report that When extracting pathways from legislation, GPT-4 occasionally commits the logical error of denying the antecedent (inferring conclusions not in the article) despite prompt instructions to avoid it, which succeeded only partially; simpler errors such as misunderstanding an article's structure or producing pathways with multiple starting points or disconnected blocks also occur but are rare. [CLM-0009-009]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment
- Janatian et al. (2023) report that In some instances the LLM captures nuances or logical particularities of a legislative article that human annotators missed: generated pathways were rated better than human-made ones in 37.5% of blind comparisons, and in five instances annotators discovered logical errors in their own reasoning after reading the automatically generated pathway. [CLM-0009-011]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment

**geographical_proxy:US**

- Holzenberger et al. (2020) report that A hand-constructed Prolog-based system, in which the statutes are manually translated into Prolog rules and the cases into Prolog facts, achieves 100% accuracy on the SARA examples, which serves as proof that a carefully crafted reasoning engine with perfect natural language understanding can solve the dataset and reaffirms that subsets of statutes can be expressed in first-order logic. [CLM-0003-006]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

**undetermined**

- Wang et al. (2026) report that Autoformalization of legal text into executable Z3 Python code involves a non-trivial program synthesis challenge: the quality of LLM-generated Z3 code varies substantially across models, with Claude Sonnet 4.6 performing best (errors in roughly 25.5% of cases, mainly sort mismatches) and Llama 3.1-8B performing poorly (often mixing SMT-LIB with Python or failing to produce executable code), and models differ widely in their ability to fix their own code when fed back the error message over three iterations. [CLM-0037-007]. — jurisdiction: undetermined; basis: dataset_or_experiment
- Wang et al. (2026) report that Autoformalization is the primary bottleneck in neuro-symbolic legal reasoning systems. Even with structured prompting and explicit instructions to surface assumptions, LLM-generated formalizations remain incomplete or incorrect, actively introducing hallucinated axioms (such as survival obligations or harm assumptions) that are not grounded in the source text, and LLMs fail to consistently recover the minimal assumptions required for faithful reasoning. [CLM-0037-008]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Conceptual

**general**

- Holzenberger et al. (2020) argue that In the broader context of computational statutory reasoning, a hand-built Prolog solver has three limitations: producing it requires domain experts while automatic generation remains an open question; translating natural language into facts requires semantic parsing capabilities; and small mistakes can lead to catastrophic failure. A machine-learning approach that replaces logical operators and explicit structure with learned dense representations can, by contrast, be adapted to new legislation and new domains automatically. [CLM-0003-007]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that A distinctive feature of the SLEEC language is that it can specify time constraints on normative rules: time budgets within which a required response must occur, and required alternative responses when a timeout occurs. [CLM-0025-004]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that By enabling the operationalisation of SLEEC requirements for autonomous agents, a formal specification, validation and verification framework complements the international efforts to define ethical principles for AI and autonomous systems (such as the UNESCO and OECD recommendations) and work that elicits SLEEC requirements from normative principles and stakeholder needs. [CLM-0025-017]. — jurisdiction: general; basis: argument
- Horner et al. (2025) argue that Every formal encoding of a legal provision is an interpretation, and a true gold standard would have to correspond to the authentic interpretation, which only the judiciary can provide and only for provisions actually disputed in court; therefore in some jurisdictions a true gold standard for legal formalization cannot exist, and any gold standard further depends on the coders' understanding of legal intent, context and encoding style. [CLM-0032-012]. — jurisdiction: general; basis: argument
- Wang et al. (2026) argue that Neuro-symbolic approaches that translate legal text into formal representations expose a key limitation: formal reasoning requires all relevant assumptions to be explicit, whereas legal text is inherently underspecified and legal reasoning depends on background assumptions and contextual interpretation (for example, contractual obligations are typically understood as excluding illegal conduct even when unstated), so such assumptions must be explicitly encoded in formal systems. [CLM-0037-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006]. — jurisdiction: general; basis: argument

### Predictive

**general**

- Janatian et al. (2023) argue that The results on LLM pathway extraction may not generalise: they rest on Civil Code of Quebec articles, drafted in a civil-code tradition that aims at lay readability, so they may not translate to jurisdictions without that aim, and they may not replicate for very complex articles or articles that can only be read in conjunction with other articles. [CLM-0009-013]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that The number of SLEEC rules for an autonomous agent is expected to be in the tens rather than the hundreds, and a single rule is unlikely to have a very long or deep list of defeaters, so pairwise checks for conflicts and redundancy within a SLEEC specification are expected to remain tractable and model checking feasible; the treatment of more complex data types in measures, however, is likely to pose a challenge. [CLM-0025-010]. — jurisdiction: general; basis: argument

**geographical_proxy:CA-QC**

- Janatian et al. (2023) argue that An LLM pathway generator used in conjunction with a human expert (augmented intelligence) has the potential to support annotators with a strong draft, making annotation more efficient and even yielding more logically correct pathways; LLMs can thus potentially support humans in creating predictable and safe legal expert systems more efficiently, with possible beneficial impacts on access to justice. [CLM-0009-012]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment

### Methodological

**general**

- Holzenberger et al. (2020) argue that Given the poor out-of-the-box performance of powerful models on the small SARA dataset, at least three research strategies are open to the community for statutory reasoning: automatic extraction of knowledge graphs from text with the same accuracy as a hand-built Prolog solver; improvements in machine reading to make training significantly more data-efficient; or new mechanisms for the efficient creation of training data based on pre-existing legal cases. [CLM-0003-015]. — jurisdiction: general; basis: argument
- Janatian et al. (2023) argue that A legislative article or paragraph can be converted into a JusticeBot pathway by prompting GPT-4 with the legislation as the user message and a system message instructing it to extract requirements and legal conclusions and link them; the model's JSON output of logic blocks and connections is converted to JusticeCreator format, where legal experts verify and adjust the pathway as a starting point for a decision support tool. [CLM-0009-003]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that SLEEC (social, legal, ethical, empathetic and cultural) rules for autonomous agents can be given end-to-end tool-supported formal treatment through a framework comprising a domain-specific language for specifying the rules and their defeaters, a formal semantics for that language in the process algebra tock-CSP, and methods for detecting conflicts and redundancy within a rule set and for verifying an agent's compliance with the rules. [CLM-0025-002]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that Because the environment in which an autonomous agent is deployed is generally highly complex and the assumptions underpinning SLEEC rules may be invalid under certain conditions, a SLEEC rule language should support defeasible reasoning, allowing normative rules to be modified in light of additional information obtained from the agent's measures; the SLEEC language does so through unless clauses (defeaters). [CLM-0025-003]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that SLEEC rule sets should be checked for conflicting and redundant rules before they are used for verification: mistakes are likely because the rules may be provided by stakeholders with different expertise (lawyers, ethicists, sociologists) and comprise complex defeaters; conflicting rules mean that no implementation can satisfy them all and must be flagged and resolved, while redundant rules are unnecessary for verification and should be flagged. [CLM-0025-005]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that The usual approach to specifying properties in CSP, in which a rule is defined over the overall alphabet of events and imposes no restrictions outside its own alphabet, is convenient for verification by refinement but does not easily support checks for conflicts and redundancy; a semantics for SLEEC rules should therefore depart from it, supporting validation directly and adopting a more elaborate notion of correctness (refinement with priorities) for verification. [CLM-0025-006]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that Conflict between SLEEC rules need only be checked for pairs of rules whose alphabets of events overlap: rules without such overlap cannot interfere with each other, and overlap in the alphabet of measures is irrelevant because rules do not need to agree on the reading of measures. [CLM-0025-007]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that A SLEEC rule r2 is redundant with respect to a conflict-free rule r1 when every behaviour allowed by r1 is also allowed by r1 and r2 together, so that r2 imposes no additional restrictions; this check is mechanised directly as CSP trace refinement, using the hiding operator to ignore events outside the rules' alphabets. [CLM-0025-009]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that The close relationship between the definition of the tock-CSP semantics for SLEEC and its mechanisation in the SLEEC tool (implemented in Eclipse with approximately 120 lines of Xtext and 700 lines of Xtend) validates the semantics, by providing evidence that the definitions are sufficient and that they produce valid tock-CSP processes. [CLM-0025-013]. — jurisdiction: general; basis: argument
- Horner et al. (2025) argue that The quality of LLM-generated Defeasible Deontic Logic formalizations should be measured by a success score that multiplies attempted coverage of the gold-standard rules per law snippet (Q1, a proportion) by the average of five sequential binary per-rule checks (syntactic validity, semantic correctness, deontic modality accuracy, precondition appropriateness, and atom-name meaningfulness/reuse) evaluated with short-circuiting, so that a model cannot score highly merely by formalizing only the simplest aspects of a snippet. [CLM-0032-010]. — jurisdiction: general; basis: argument
- Horner et al. (2025) argue that Precision-and-recall evaluation of rule extraction against a gold standard, as used by Dragoni et al. (2017), is limited because its one-to-one rule mapping penalizes semantically correct rules when an LLM produces several valid rules jointly equivalent to one gold-standard rule, and because valid atoms and rules that formalize additional information from the law text but are absent from the gold standard count as false positives, so the metric cannot distinguish semantically valid additions from hallucinated ones. [CLM-0032-011]. — jurisdiction: general; basis: argument
- Horner et al. (2025) argue that For legal texts with long articles, segmenting the text into law snippets before formalization helps the LLM analyze each component without overlooking details, and snippet length must be balanced: overly long snippets risk losing information during formalization, while overly short ones hinder atom reuse; enumerations with more than two elements should be split into separate snippets. [CLM-0032-014]. — jurisdiction: general; basis: argument

**geographical_proxy:AU**

- Horner et al. (2025) argue that Prompt engineering alone is insufficient to resolve inter-paragraph references when formalizing legal text into Defeasible Deontic Logic; reference resolution requires additional procedural components in the methodology, such as a post-generation refinement phase designed to ensure semantic coherence across references. [CLM-0032-013]. — jurisdiction: geographical_proxy:AU; basis: dataset_or_experiment

**geographical_proxy:CA-QC**

- Janatian et al. (2023) argue that Instructing the model in the prompt to stick to the legislative text, and providing that text in the prompt, seems to be a viable method for constraining the textual output of an LLM to the targeted legislative text. [CLM-0009-010]. — jurisdiction: geographical_proxy:CA-QC; basis: dataset_or_experiment

**undetermined**

- Wang et al. (2026) argue that The core challenge in faithful neuro-symbolic legal reasoning is suggested to lie not in the choice of formalism but in constructing representations that capture all relevant assumptions: since LLMs fail to reliably recover the implicit knowledge required for correct reasoning even under first-order logic, improving assumption and ambiguity handling is a prerequisite for moving to more expressive logical systems such as deontic logic. [CLM-0037-018]. — jurisdiction: undetermined; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Instructing the model in the prompt to stick to the legislative text, and providing that text in the prompt, seems to be a viable method for constraining the textual output of an LLM to the targeted legislative text. [CLM-0009-010] is in tension with the claim that GPT-3 makes clear errors in statutory reasoning on SARA, in particular mistakenly referring to the wrong part of a statute (confusing one subparagraph with a neighbouring one), and this tendency persists even when the text of the statute is included in the prompt. [CLM-0008-005] (inferred, low). Note: One finds that supplying the legislative text in the prompt viably constrains the model's textual output to that text; the other finds GPT-3 still refers to the wrong part of a statute when the statute is in the prompt — the tension dissolves if textual fidelity and correct cross-reference are distinct.
- The claim that Future work on legal AI must strive to integrate legal expertise with data-derived models; there is great value in combining knowledge-based and data-driven systems rather than continuing to assume that deep legal expertise will reliably emerge given large enough amounts of data and computation. [CLM-0014-001] is in tension with the claim that In the broader context of computational statutory reasoning, a hand-built Prolog solver has three limitations: producing it requires domain experts while automatic generation remains an open question; translating natural language into facts requires semantic parsing capabilities; and small mistakes can lead to catastrophic failure. A machine-learning approach that replaces logical operators and explicit structure with learned dense representations can, by contrast, be adapted to new legislation and new domains automatically. [CLM-0003-007] (inferred, low). Note: One warns against assuming legal expertise will emerge from data alone and urges integrating expert knowledge; the other presents learned dense representations replacing explicit logical structure as the adaptable alternative to hand-built solvers.
- The claim that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006] is in tension with the claim that Legal reasoning is defeasible rather than monotonic: rules applicable on their face can be trumped by special exceptions, conflicting superior rules, or by distinguishing the precedent from which the rule derives, and legal argumentation is an exercise in competitive theory formation before an arbitrator in which each side constructs arguments from evidence, written law, cases and other authority. [CLM-0014-018] (inferred, high). Note: One holds that jurisprudence is at its operational core binary and deterministic; the other characterises legal reasoning as defeasible, ambiguous and discretionary.
- The claim that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006] is in tension with the claim that Every formal encoding of a legal provision is an interpretation, and a true gold standard would have to correspond to the authentic interpretation, which only the judiciary can provide and only for provisions actually disputed in court; therefore in some jurisdictions a true gold standard for legal formalization cannot exist, and any gold standard further depends on the coders' understanding of legal intent, context and encoding style. [CLM-0032-012] (inferred, medium). Note: One treats legal rules as deterministic and machine-checkable; the other holds that every formal encoding of a provision is an interpretation on which experts disagree.
- The claim that Jurisprudence at its operational core is binary and deterministic (a statute is active or repealed, a deadline met or missed, jurisdiction present or absent), whereas an LLM represents knowledge as a continuous latent space in which a hallucinated case name sits close to a real one; the Rule of Law and deterministic AI architecture are therefore convergent, and the Neuro-Symbolic Sandwich reveals the logic the law has always demanded rather than imposing an alien one. [CLM-0049-006] is in tension with the claim that The central challenge for faithful legal reasoning, by humans and LLMs alike, is that it is fundamentally unclear which assumptions are permissible: the boundary between valid inference and unjustified assumption is ambiguous. LLMs resolve this ambiguity by injecting ungrounded assumptions, while formal methods expose it through conservative reasoning. [CLM-0037-011] (inferred, medium). Note: One asserts the determinacy of law's operational core; the other finds the boundary of permissible assumptions in legal entailment fundamentally unclear even for humans.

## Distribution

Sources with claims on this concept: 8; claims: 53.

**By contribution type**

| value | sources |
|---|---|
| technical | 6 |
| empirical_quantitative | 4 |
| theoretical | 4 |
| normative | 3 |
| empirical_qualitative | 2 |
| survey | 2 |
| doctrinal | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 5 |
| US | 2 |
| CA-QC | 1 |
| CoE | 1 |
| EU | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 8 |
| US | 1 |
| geographical_proxy:AU | 1 |
| geographical_proxy:CA-QC | 1 |
| geographical_proxy:US | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2026 | 3 |
| 2023 | 2 |
| 2020 | 1 |
| 2024 | 1 |
| 2025 | 1 |

## What the sources do not address


## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.

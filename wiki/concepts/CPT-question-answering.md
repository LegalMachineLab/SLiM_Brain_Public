---
id: "CPT-question-answering"
label: "Question answering"
status: "anchor"
concept_type: "legal_task"
definition: "Answering legal questions posed in natural language, including entailment over statutory text."
aliases: []
broader: []
sources: ["SRC-0003", "SRC-0008", "SRC-0011", "SRC-0016", "SRC-0019", "SRC-0024", "SRC-0026", "SRC-0029", "SRC-0030"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Question answering

_Status: anchor; family: legal_task._

## Definition

Answering legal questions posed in natural language, including entailment over statutory text.

Conceptual claims on this concept, each with its source:
- Holzenberger et al. (2020): Computational statutory reasoning is distinct from most existing work in machine reading: much of the information needed to decide a case is declared exactly once, in a law, whereas the information needed in most machine reading tends to be learned through distributional language statistics. [CLM-0003-001]
- Holzenberger et al. (2020): Statutory reasoning is an exceptionally pure instance of a reasoner needing to understand prescriptive language, because legal rules are true by virtue of being written down and agreed to rather than discovered through evidence and a scientific process; it is therefore a real-world task that can motivate the development of models able to use prescriptive rules specified in natural language. [CLM-0003-002]
- Blair-Stanek et al. (2023): Statutory reasoning is the task of reasoning with facts and statutes, where statutes are rules written in natural language by a legislature; it is a basic legal skill and one of the most basic tasks required of lawyers. [CLM-0008-001]
- Nay et al. (2023): Although the experiments are limited to U.S. tax law, the capabilities they investigate, finding relevant legal authorities and applying them to specific factual scenarios, are at the heart of legal work and could be generalised to other areas of legal practice. [CLM-0024-012]
- Guha et al. (2023): Legal reasoning, for the purpose of evaluating LLMs, can be organised into six types: issue-spotting, rule-recall, rule-application and rule-conclusion (drawn from the IRAC framework), plus interpretation and rhetorical-understanding; this typology draws heavily on American legal thought but may be extended to non-American bodies of law, and gives lawyers and LLM developers a common vocabulary. [CLM-0026-007]

## Claims about the concept

### Descriptive

**general**

- Holzenberger et al. (2020) state that Although tools exist to help lawyers retrieve documents relevant to a case, no strong capabilities in automatic statutory reasoning (systems that suggest legal opinions by applying rules to a case) are known to exist. [CLM-0003-003]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated
- Ribary et al. (2023) state that Although conversational LLMs such as ChatGPT and gpt-4 have shown notable success in the legal field, for instance by passing the multistate part of the US bar exam, some of the legal advice such systems provide has, on closer analysis, proven unsound, erroneous and sometimes even absurd, and real-life legal cases tend to be more complicated than the bar exam. [CLM-0011-003]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Khadloya et al. (2025) state that Existing legal question-answering and retrieval benchmarks operate at the document level, returning entire cases rather than pinpointed spans, and are not designed for judge-facing interaction loops; most legal QA and summarization systems return text without a user interface that enforces verification. [CLM-0019-003]. — jurisdiction: general [jurisdiction inferred]; basis: literature

### Interpretive

**US**

- Holzenberger et al. (2020) read Internal Revenue Code (IRC) as follows: The US Internal Revenue Code can be framed as a set of predicates formulated in human language; because the language of the law has an open texture, determining whether a subsection applies and identifying and filling the slots it mentions is particularly challenging for a computer-based system, which makes the Code an excellent corpus for building systems that reason with rules specified in natural language and have good language understanding capabilities. [CLM-0003-004]. — jurisdiction: US; basis: argument

### Normative

**general**

- Blair-Stanek et al. (2023) argue that Statutory reasoning should be treated as an area of interest for new AI research and as a challenge to motivate future improvements in large language models. [CLM-0008-021]. — jurisdiction: general; basis: dataset_or_experiment

### Empirical

**CN**

- Hu et al. (2024) report that In a user study, roughly 30% of the Chinese judicial interpretations displayed alongside LLM legal advice served to clarify specific legal terminology or special cases, while for the remaining 70% users were already familiar with their content; users nonetheless asserted that judicial interpretations help them comprehend responses when interpretation is required, make accurate judgments about their situations, and pursue further tailored consultation. [CLM-0029-012]. — jurisdiction: CN [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2024) report that At present, LLMs cannot effectively solve legal problems under the Chinese legal system and are unable to provide effective legal assistance, even the high-performing GPT-4 included. [CLM-0030-023]. — jurisdiction: CN; basis: dataset_or_experiment

**US**

- Blair-Stanek et al. (2023) report that GPT-3 has some, but imperfect and partly incorrect, prior knowledge of the U.S. tax code: in zero-shot SARA prompts with no statutory text it performs at chance or worse, yet its step-by-step reasoning cites and paraphrases provisions of the Internal Revenue Code, and that recalled content is wrong. [CLM-0008-006]. — jurisdiction: US; basis: dataset_or_experiment

**general**

- Blair-Stanek et al. (2023) report that In a zero-shot setting, GPT-3 performs poorly at answering whether a subsection of a very simple synthetic statute applies to a person given a single fact: accuracy is around 78% even for the simplest 2-wide, 2-deep statutes, which involve no negation or ambiguity, and it declines further as the statutes get wider or deeper. [CLM-0008-015]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that GPT-3's difficulty with simple synthetic statutes is not specific to the statutory format or to the choice of made-up terms: accuracy is comparable between statute versions and semantically-identical numbered-sentence versions of the same definitions (6537 versus 6562 correct of 9000), and comparable between nonce terms and random-id terms. [CLM-0008-016]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that GPT-3's zero-shot errors on synthetic statutes are overwhelmingly false positives, that is, it concludes that a section or sentence applies when it actually does not (2204 false positives against 61 false negatives among 2272 errors in the nonce runs). [CLM-0008-017]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that How the applicability question is phrased affects GPT-3's accuracy on synthetic statutes: phrasings that mention the statute's top-level defined term (for example "Is N a T because of S?") uniformly perform worse (52-58%) than the two phrasings that do not ("Is S applicable to N?" at 77% and "Does S apply to N?" at 74%). [CLM-0008-018]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that Providing two correct worked examples (two-shot prompting) uniformly improves GPT-3 over zero-shot on synthetic statutes, reaching 100% on 2-wide, 2-deep statutes, but accuracy still decreases as depth and width increase and remains only 81% on 3-wide, 3-deep statutes, which are far less complex than many sections of the U.S. Code. [CLM-0008-019]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that GPT-3's 78% zero-shot accuracy on a very simple 2-wide, 2-deep synthetic statute paired with a single fact and a single question raises doubts about GPT-3's ability to handle basic legal work, and this poor performance on synthetic statutory reasoning explains why its SARA results, though better than the prior state of the art, leave significant room for improvement. [CLM-0008-020]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that Legal terminology embedded in LLM-generated legal advice without sufficient explanation may pose understanding difficulties for users without domain knowledge; special cases lacking a clear definition in legal articles are likewise hard for non-professional users to understand. [CLM-0029-004]. — jurisdiction: general [jurisdiction inferred]; basis: literature
- Hu et al. (2024) report that For simple legal queries, legal-domain LLMs can provide correct responses in most cases; interactive legal-basis, article-selection and case-retrieval support is primarily needed for complex legal consultation queries. [CLM-0029-014]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated

**geographical_proxy:CN**

- Hu et al. (2024) report that Current legal article retrieval models used with legal-domain LLMs cannot ensure that all relevant legal articles are retrieved and all irrelevant ones excluded; missed articles reduce the completeness of the LLM's response, while irrelevant retrieved articles introduce noise that leads the LLM to produce incomplete, incorrect or inconsistent advice. [CLM-0029-001]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: argument
- Hu et al. (2024) report that Legal-domain LLMs may be sensitive to input perturbation: responses can be contradictory when inputs differ only slightly, or even when an identical question is asked in a new chat, and this inconsistency can confuse users and lower the quality of the consultation. [CLM-0029-002]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: argument
- Hu et al. (2024) report that In a user study on complex marriage consultation queries, the top three automatically retrieved legal articles were found not entirely correct for an average of 83% of queries (about 20% of responses incorrect because of noise from irrelevant articles, 25% incomplete because relevant articles were missing, 38% containing irrelevant information), whereas in 80% of cases users obtained correct responses by selecting the relevant legal articles and having the LLM regenerate its answer. [CLM-0029-010]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that In a user study, users reported that the legal article basis of the LLM's response was accurately identified for approximately 95% of queries, that cross-referencing responses with the identified articles let them swiftly determine whether a response was reliable, and that in about 73% of queries the response already contained parts of the legal article but not a full rephrasing, so that the displayed basis gave convenient access to the complete article. [CLM-0029-011]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Hu et al. (2024) report that In a user study, retrieving relevant legal cases proved beneficial for 77% of consultation queries on average: although the retrieved cases might not exactly match the user's situation, they provide a reference point to gauge possible outcomes, and highlighting the sentences of a case relevant to the query significantly streamlines reading and improves reading efficiency. [CLM-0029-013]. — jurisdiction: geographical_proxy:CN [jurisdiction inferred]; basis: dataset_or_experiment
- Li et al. (2024) report that On a comprehensive Chinese legal benchmark, the closed-source model GPT-4 achieves the best overall performance and open-source models perform slightly worse, but GPT-4 remains far from perfect on many tasks owing to its lack of knowledge related to the Chinese legal system, indicating significant room for improvement of LLMs in the legal domain. [CLM-0030-009]. — jurisdiction: geographical_proxy:CN; basis: dataset_or_experiment
- Li et al. (2024) report that Most LLMs perform best at the Understanding and Logic Inference levels of legal cognitive ability: within a given context or when provided with the relevant legal provisions, LLMs can effectively use their inherent reasoning abilities to provide reasonable answers, although complex tasks such as multi-hop reasoning remain challenging. [CLM-0030-018]. — jurisdiction: geographical_proxy:CN; basis: dataset_or_experiment

**geographical_proxy:GB**

- Ribary et al. (2023) report that Adding a curated, domain-specific knowledge base (statutes, HMRC forms and case law retrieved into the prompt) to an LLM produces statistically more accurate answers to insolvency-law evaluation questions than the unmodified LLM: on an unseen test set of twelve questions marked with a law-school-style scheme, the knowledge-base-enhanced gpt-3.5-turbo scored 29-30% against 20% for raw gpt-3.5-turbo, and the enhanced gpt-4 scored 47% against 21% for raw gpt-4, both differences being significant under a two-sided paired t-test. [CLM-0011-001]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

**geographical_proxy:US**

- Holzenberger et al. (2020) report that A hand-constructed Prolog-based system, in which the statutes are manually translated into Prolog rules and the cases into Prolog facts, achieves 100% accuracy on the SARA examples, which serves as proof that a carefully crafted reasoning engine with perfect natural language understanding can solve the dataset and reaffirms that subsets of statutes can be expressed in first-order logic. [CLM-0003-006]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Holzenberger et al. (2020) report that On the SARA statutory reasoning tasks, straightforward application of contemporary machine reading models (BERT-based and feedforward models) performs comparably to a majority or constant baseline regardless of the underlying method, and performance remains mostly unchanged when the statutes, or the statutes and the context, are removed from the input, meaning that the models are not utilising the statutes. [CLM-0003-008]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Holzenberger et al. (2020) report that Adapting BERT or word vectors to the legal domain (Legal BERT further trained on case law; tax-specific word2vec vectors) has no noticeable effect on performance on the SARA statutory reasoning tasks. [CLM-0003-009]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that GPT-3's statutory-reasoning performance on SARA is quite sensitive to the prompt setting, with large variations across settings; appending "Let's think step by step." occasionally improves performance but not systematically. [CLM-0008-003]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that On SARA, GPT-3 performs at least as well on cases involving no numbers as on cases involving numbers in nine of ten experimental setups, which is expected given GPT-3's known limitation in doing calculations with large numbers. [CLM-0008-004]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that GPT-3 makes clear errors in statutory reasoning on SARA, in particular mistakenly referring to the wrong part of a statute (confusing one subparagraph with a neighbouring one), and this tendency persists even when the text of the statute is included in the prompt. [CLM-0008-005]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek et al. (2023) report that GPT-3 shows no recognition of the SARA dataset when asked about it: it describes SARA as a non-existent multiple-choice test for legal professionals, and when shown SARA cases and asked where the text comes from it never implicates SARA (most often answering the IRS website); this addresses the possibility that SARA, available online since 2020, was in GPT-3's training data and biased the results. [CLM-0008-007]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek and Van Durme (2025) report that Leading large language models (gpt-4o, claude-3.5 and gemini-1.5) are unstable when answering hard legal questions: even with temperature set to 0 and every other available parameter set for determinism, the identical question sometimes yields the answer that one party should prevail and sometimes the answer that the other party should prevail. Each of the three models is unstable on some share of the 500 questions tested, from 10.6% for claude-3.5 up to 50.4% for gemini-1.5. [CLM-0016-001]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Blair-Stanek and Van Durme (2025) report that LLM instability on legal questions does not arise from unsound legal analysis: when the same model reaches opposite conclusions on the same question in different runs, the legal analysis in each run is sound and the runs simply weigh the arguments or interests differently, as where an ambiguous standard (such as whether a restriction is no more extensive than necessary to serve the state interest) is found met in one run and not met in another. [CLM-0016-010]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that Across multiple-choice exams on U.S. tax law (one based on the Code of Federal Regulations, one on the U.S. Code), answer accuracy increases with each subsequently released OpenAI model (davinci, text-davinci-002, gpt-3.5-turbo, GPT-4); the underlying model is the primary experimental factor producing consistent accuracy gains when averaged across retrieval and prompting factors, which evidences emerging legal understanding capabilities in LLMs. [CLM-0024-001]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that Few-shot prompting (supplying three question-answer examples of the same question type, without source documents) strongly improves GPT-4's accuracy on tax law questions but is less consistently useful for weaker models. [CLM-0024-002]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that Chain-of-thought prompting does not consistently improve tax-law answer accuracy across all models and retrieval methods, but it does boost GPT-4's performance; this suggests an LLM might need a certain capability level before additional step-by-step reasoning improves its performance. [CLM-0024-003]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that Giving an LLM more legal text, and legal text more relevant to the specific tax question asked (moving from no source material, through similarity-search retrieval, to the correct 'gold truth' source), weakly increases answer accuracy for most models. [CLM-0024-004]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that LLMs, particularly GPT-4 combined with the correct legal texts, few-shot and chain-of-thought prompting, can answer tax law questions at high levels of accuracy but not yet at expert tax lawyer level; a professional tax lawyer would be expected to answer such questions with near-perfect accuracy. [CLM-0024-005]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) report that Legal understanding (specifically tax law understanding) could be an emergent ability of LLMs: it appears once the model has sufficient underlying general capability and is adequately prompted to elicit reasoning behaviour, in the same way that other complex reasoning abilities emerge nonlinearly with model size. [CLM-0024-006]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Guha et al. (2023) report that Within an LLM family, larger models usually outperform smaller models on legal reasoning tasks, although the margin varies across families and reasoning categories, and the largest model evaluated (GPT-4) outperforms virtually all other models. [CLM-0026-012]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Guha et al. (2023) report that GPT-4 outperforms GPT-3.5 and Claude-1 on legal reasoning tasks, and the largest average performance difference between GPT-4 and GPT-3.5/Claude-1 occurs on rule-application tasks, where GPT-4 is significantly better on both correctness and analysis (p < 0.01). [CLM-0026-016]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Guha et al. (2023) report that Variation in LLM performance across rule-application tasks is consistent with lawyers' subjective impressions of task difficulty, and LLM explanations fail in identifiable ways: incorrect arithmetic or numerical comparisons, citing the wrong portion of a rule, hallucinating facts not in the fact pattern, giving a bare prediction without explanation, or merely restating the facts and rule without explaining how the outcome is reached. [CLM-0026-019]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Guha et al. (2023) report that Organising rule-conclusion samples into slices of similar fact patterns offers a heuristic for characterising which legal inferences LLMs can perform and which they struggle with; on the hearsay task some slices (non-assertive conduct) are comfortably within model capabilities while others (statements not introduced to prove the truth of the matter asserted) still pose a considerable challenge, and GPT-4's improvement over GPT-3.5 is mainly attributable to the non-verbal hearsay and in-court statement slices. [CLM-0026-020]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment
- Guha et al. (2023) report that Whether an LLM can rely on its latent knowledge of a legal rule for rule-conclusion tasks varies considerably by task: for some rules, describing the rule explicitly in the prompt has negligible effect, while for others (e.g. Abercrombie, UCC v. common law, some diversity tasks) it significantly improves performance; a possible explanation is that legal rules are described to varying extents in pretraining corpora, so legal prompting may require practitioners to supply additional background information. [CLM-0026-023]. — jurisdiction: geographical_proxy:US [jurisdiction inferred]; basis: dataset_or_experiment

### Conceptual

**general**

- Holzenberger et al. (2020) argue that Computational statutory reasoning is distinct from most existing work in machine reading: much of the information needed to decide a case is declared exactly once, in a law, whereas the information needed in most machine reading tends to be learned through distributional language statistics. [CLM-0003-001]. — jurisdiction: general; basis: argument
- Holzenberger et al. (2020) argue that Statutory reasoning is an exceptionally pure instance of a reasoner needing to understand prescriptive language, because legal rules are true by virtue of being written down and agreed to rather than discovered through evidence and a scientific process; it is therefore a real-world task that can motivate the development of models able to use prescriptive rules specified in natural language. [CLM-0003-002]. — jurisdiction: general; basis: argument
- Blair-Stanek et al. (2023) argue that Statutory reasoning is the task of reasoning with facts and statutes, where statutes are rules written in natural language by a legislature; it is a basic legal skill and one of the most basic tasks required of lawyers. [CLM-0008-001]. — jurisdiction: general; basis: argument
- Nay et al. (2023) argue that Although the experiments are limited to U.S. tax law, the capabilities they investigate, finding relevant legal authorities and applying them to specific factual scenarios, are at the heart of legal work and could be generalised to other areas of legal practice. [CLM-0024-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:US**

- Guha et al. (2023) argue that Legal reasoning, for the purpose of evaluating LLMs, can be organised into six types: issue-spotting, rule-recall, rule-application and rule-conclusion (drawn from the IRAC framework), plus interpretation and rhetorical-understanding; this typology draws heavily on American legal thought but may be extended to non-American bodies of law, and gives lawyers and LLM developers a common vocabulary. [CLM-0026-007]. — jurisdiction: geographical_proxy:US; basis: literature

### Predictive

**GB**

- Ribary et al. (2023) argue that An LLM-based system that triages potential insolvency cases for stakeholders of micro, small and medium enterprises at a competency comparable to a Level 6 or 7 law student could, if successful enough, help solo practitioners and smaller law firms, which often lack sufficient expertise in this area of law, to expand the scope of their services. [CLM-0011-004]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

**general**

- Ribary et al. (2023) argue that A knowledge-base-enhanced LLM system for insolvency queries has the potential to be expanded to other jurisdictions and to cross-jurisdictional queries, and can be further improved by matching on-point legal information to user queries. [CLM-0011-011]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated
- Ribary et al. (2023) argue that Because insolvency law is a fairly stable area of law in which legislative changes are rare, implementing a curated-knowledge-base system of the Insolvency Bot kind may be more challenging in areas of law subject to more rapid legislative change, such as immigration law. [CLM-0011-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:US**

- Holzenberger et al. (2020) argue that Performance on the SARA statutory reasoning dataset will not be improved through straightforward application of a large-scale language model, unlike on other datasets such as COPA, SQuAD 2.0 and SWAG where large pre-trained models produced large gains. [CLM-0003-010]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment
- Nay et al. (2023) argue that Because LLM legal understanding improves with each model release, superhuman AI legal skills may emerge as the state of the art continues to advance rapidly. [CLM-0024-007]. — jurisdiction: geographical_proxy:US; basis: dataset_or_experiment

### Methodological

**CN**

- Hu et al. (2024) argue that Training data for matching each sentence of an LLM's legal advice to its legal basis can be constructed automatically, without human annotation, by having the legal LLM answer sampled consultation queries with individual retrieved legal articles and using BM25 to pick the highest-scoring sentence as a positive pair and the least similar sentences as negatives; legal articles alone suffice for this construction because judicial interpretations share their language style and content and all their terminology appears in legal articles. [CLM-0029-008]. — jurisdiction: CN [jurisdiction inferred]; basis: argument

**US**

- Holzenberger et al. (2020) argue that SARA (StAtutory Reasoning Assessment) is a novel dataset for statutory reasoning: a set of rules extracted from the US Internal Revenue Code together with natural-language cases and questions that can only be answered correctly by referring to the rules; earlier projects that formalised statutes into expert systems did not include a dataset or task the programs were applied to. [CLM-0003-005]. — jurisdiction: US; basis: literature
- Blair-Stanek and Van Durme (2025) argue that U.S. federal Courts of Appeals decisions in which the three-judge panel split 2-1 typically present a difficult legal question with two well-written opinions that disagree on the proper resolution, and can therefore be distilled into difficult binary legal questions (which of two parties should prevail) for testing LLMs; cases under 10,000 characters tend to hinge on simple procedural matters and cases over 50,000 characters tend to involve issues too complex to summarise, and diversity-jurisdiction cases are excluded because state law diverges across the 50 states whereas federal law is largely uniform. [CLM-0016-006]. — jurisdiction: US; basis: argument
- Nay et al. (2023) argue that Tax law is a suitable domain for automated, large-scale validation of LLM legal capabilities because its legal authority is principally concentrated in two sources (the Treasury Regulations under the CFR and Title 26 of the U.S. Code), many tax rules allow definitive answers, answering tax questions requires logical reasoning and maths beyond reading the authority, and tax law is highly significant to the economic lives of nearly every citizen and company. [CLM-0024-009]. — jurisdiction: US; basis: argument

**general**

- Holzenberger et al. (2020) argue that Given the poor out-of-the-box performance of powerful models on the small SARA dataset, at least three research strategies are open to the community for statutory reasoning: automatic extraction of knowledge graphs from text with the same accuracy as a hand-built Prolog solver; improvements in machine reading to make training significantly more data-efficient; or new mechanisms for the efficient creation of training data based on pre-existing legal cases. [CLM-0003-015]. — jurisdiction: general; basis: argument
- Blair-Stanek et al. (2023) argue that Because no technique is known to determine how much GPT-3's flawed knowledge of the U.S. Code affects its performance on SARA, GPT-3's statutory-reasoning ability can be isolated by testing it on entirely synthetic statutes, written in the U.S. Code's numbering style with nonce or random-id terms, which GPT-3 is guaranteed never to have seen during training. [CLM-0008-014]. — jurisdiction: general; basis: argument
- Ribary et al. (2023) argue that Marking of LLM answers against a mark scheme can be automated by feeding each answer together with each yes-no mark-scheme question to gpt-4 and parsing the generated reply for words such as 'yes', 'no' or 'however', mapped to 100%, 0% or 50% of the points available, so that gpt-4 simulates a human examiner. [CLM-0011-009]. — jurisdiction: general [jurisdiction inferred]; basis: dataset_or_experiment
- Guha et al. (2023) argue that Rule-application by an LLM should be evaluated on the generated explanation along two dimensions, correctness (no misstatement of rule, facts or outcome, and no logic or arithmetic error) and analysis (the explanation contains the inferences from the facts that are relevant under the rule), because an explanation that merely restates rule, facts and a correct outcome is error-free yet conclusory and unsatisfactory in legal work. [CLM-0026-008]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hu et al. (2024) argue that Visually presenting, for each sentence of an LLM's legal advice, the legal article that serves as its basis (found by similarity matching with a legal-domain fine-tuned embedding model) lets users verify the reliability of the response and trust the advice; a sentence for which no legal basis is found can be viewed as a warning that the sentence may be incorrect. [CLM-0029-005]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Hu et al. (2024) argue that Allowing users to participate in legal article retrieval by interactively selecting, from the top retrieved articles, those that fit their situation increases the consistency between the user's situation and the legal articles the LLM refers to, enabling the LLM to generate more complete and accurate responses while avoiding noise from irrelevant articles. [CLM-0029-006]. — jurisdiction: general [jurisdiction inferred]; basis: argument

**geographical_proxy:GB**

- Ribary et al. (2023) argue that Assessing LLM answers to legal queries with a law-school-style mark scheme, written by an independent domain expert and weighted so that omitting key information or giving unsound or incomplete legal advice is penalised more heavily than failing to cite the applicable statute or binding precedent, allows raw LLMs and enhanced systems to be evaluated as if they were university-level (Level 6 or 7) law exam candidates. [CLM-0011-008]. — jurisdiction: geographical_proxy:GB; basis: dataset_or_experiment

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002] is in tension with the claim that Performance on the SARA statutory reasoning dataset will not be improved through straightforward application of a large-scale language model, unlike on other datasets such as COPA, SQuAD 2.0 and SWAG where large pre-trained models produced large gains. [CLM-0003-010] (inferred, high). Note: One predicts that straightforward application of a large-scale language model will not improve SARA performance; the other reports that straightforward GPT-3 prompting beats the previous BERT-based state of the art on SARA. The later source cites the earlier one only for the dataset, not on this prediction, so the edge is inferred.
- The claim that Instructing the model in the prompt to stick to the legislative text, and providing that text in the prompt, seems to be a viable method for constraining the textual output of an LLM to the targeted legislative text. [CLM-0009-010] is in tension with the claim that GPT-3 makes clear errors in statutory reasoning on SARA, in particular mistakenly referring to the wrong part of a statute (confusing one subparagraph with a neighbouring one), and this tendency persists even when the text of the statute is included in the prompt. [CLM-0008-005] (inferred, low). Note: One finds that supplying the legislative text in the prompt viably constrains the model's textual output to that text; the other finds GPT-3 still refers to the wrong part of a statute when the statute is in the prompt — the tension dissolves if textual fidelity and correct cross-reference are distinct.
- The claim that Fine-tuned transformer models outperform zero-shot and few-shot large language models on the UK Employment Tribunal four-class case outcome prediction task, with fine-tuned T5 as the best-performing model, and all tested models significantly outperform a random-guess baseline. [CLM-0013-005] is in tension with the claim that Straightforward prompting of GPT-3 (text-davinci-003) on the SARA statutory-reasoning benchmark yields accuracy better than the previous best published, BERT-based results, with far less human input: the best setting (zero-shot with the statute included) reaches 71% aggregate accuracy on the 100 entailment test cases, significantly better than the BERT-based state of the art (p approximately 0.038) and the majority baseline. [CLM-0008-002] (inferred, medium). Note: One finds fine-tuned transformers beating prompted GPT models on outcome prediction; the other finds prompted GPT-3 beating the fine-tuned BERT-based state of the art on statutory reasoning — opposite rankings on different tasks.
- The claim that Leading large language models (gpt-4o, claude-3.5 and gemini-1.5) are unstable when answering hard legal questions: even with temperature set to 0 and every other available parameter set for determinism, the identical question sometimes yields the answer that one party should prevail and sometimes the answer that the other party should prevail. Each of the three models is unstable on some share of the 500 questions tested, from 10.6% for claude-3.5 up to 50.4% for gemini-1.5. [CLM-0016-001] is in tension with the claim that Setting GPT-3's temperature to 0.0 and top_P to 1.0 in all experiments serves to maximize reproducibility and to minimize the risk that GPT-3 wanders off topic or hallucinates. [CLM-0008-013] (inferred, medium). Note: One treats temperature 0 as securing reproducibility; the other finds leading models unstable on identical inputs even at temperature 0 with every determinism parameter set.
- The claim that Across multiple-choice exams on U.S. tax law (one based on the Code of Federal Regulations, one on the U.S. Code), answer accuracy increases with each subsequently released OpenAI model (davinci, text-davinci-002, gpt-3.5-turbo, GPT-4); the underlying model is the primary experimental factor producing consistent accuracy gains when averaged across retrieval and prompting factors, which evidences emerging legal understanding capabilities in LLMs. [CLM-0024-001] is in tension with the claim that Performance on the SARA statutory reasoning dataset will not be improved through straightforward application of a large-scale language model, unlike on other datasets such as COPA, SQuAD 2.0 and SWAG where large pre-trained models produced large gains. [CLM-0003-010] (inferred, medium). Note: One predicts that scaling language models will not straightforwardly improve statutory reasoning; the other reports accuracy on tax-law questions rising with each model release.
- The claim that Because LLM legal understanding improves with each model release, superhuman AI legal skills may emerge as the state of the art continues to advance rapidly. [CLM-0024-007] is in tension with the claim that GPT-3's 78% zero-shot accuracy on a very simple 2-wide, 2-deep synthetic statute paired with a single fact and a single question raises doubts about GPT-3's ability to handle basic legal work, and this poor performance on synthetic statutory reasoning explains why its SARA results, though better than the prior state of the art, leave significant room for improvement. [CLM-0008-020] (inferred, medium). Note: One expects superhuman legal skills to emerge as models advance; the other doubts GPT-3's ability to handle even basic legal work — a difference of outlook on the same trajectory.
- The claim that Under a few-shot setting, most LLMs show only slight and usually unstable performance improvements on legal tasks; the effect of few-shot examples varies across models, with some (such as GPT-4) improving and others (such as Qwen-14B-Chat) degrading, possibly because few-shot inputs become overly lengthy for certain models. [CLM-0030-014] is in tension with the claim that Few-shot prompting (supplying three question-answer examples of the same question type, without source documents) strongly improves GPT-4's accuracy on tax law questions but is less consistently useful for weaker models. [CLM-0024-002] (inferred, medium). Note: One finds few-shot prompting strongly improves GPT-4 on tax questions; the other finds few-shot gains slight and unstable across models on a Chinese legal benchmark.
- The claim that Under a few-shot setting, most LLMs show only slight and usually unstable performance improvements on legal tasks; the effect of few-shot examples varies across models, with some (such as GPT-4) improving and others (such as Qwen-14B-Chat) degrading, possibly because few-shot inputs become overly lengthy for certain models. [CLM-0030-014] is in tension with the claim that Providing two correct worked examples (two-shot prompting) uniformly improves GPT-3 over zero-shot on synthetic statutes, reaching 100% on 2-wide, 2-deep statutes, but accuracy still decreases as depth and width increase and remains only 81% on 3-wide, 3-deep statutes, which are far less complex than many sections of the U.S. Code. [CLM-0008-019] (inferred, medium). Note: One finds two-shot prompting uniformly improves GPT-3 on synthetic statutes; the other finds few-shot improvements slight and unstable on legal tasks.
- The claim that Legal-oriented pre-trained language models (Legal-BERT and CaseLaw-BERT) perform overall better than models pre-trained on generic corpora (BERT, RoBERTa, DeBERTa, Longformer, BigBird) across the seven LexGLUE legal NLU tasks, consistently offering performance improvements across multiple tasks. [CLM-0048-002] is in tension with the claim that Adapting BERT or word vectors to the legal domain (Legal BERT further trained on case law; tax-specific word2vec vectors) has no noticeable effect on performance on the SARA statutory reasoning tasks. [CLM-0003-009] (inferred, medium). Note: One finds legal-oriented pre-training helps on legal NLU benchmarks; the other finds domain adaptation of BERT has no effect on statutory reasoning.

## Distribution

Sources with claims on this concept: 9; claims: 66.

**By contribution type**

| value | sources |
|---|---|
| empirical_quantitative | 9 |
| technical | 9 |
| theoretical | 2 |
| doctrinal | 1 |
| empirical_qualitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 5 |
| CN | 2 |
| GB | 1 |
| IN | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 7 |
| geographical_proxy:US | 5 |
| US | 4 |
| CN | 2 |
| geographical_proxy:CN | 2 |
| GB | 1 |
| geographical_proxy:GB | 1 |

**By year**

| value | sources |
|---|---|
| 2023 | 4 |
| 2024 | 2 |
| 2025 | 2 |
| 2020 | 1 |

## What the sources do not address


Explicit questions occurring verbatim in claim or premise text and answered by no claim on this concept:
- "A direct question about SARA and 20 randomly selected SARA cases followed by 'Where does the text above come from?" — raised in [CLM-0008-007] [ABS-1439] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- "How the applicability question is phrased affects GPT-3's accuracy on synthetic statutes: phrasings that mention the statute's top-level defined term (for example "Is N a T because of S?" — raised in [CLM-0008-018] [ABS-1440] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- "") uniformly perform worse (52-58%) than the two phrasings that do not ("Is S applicable to N?" — raised in [CLM-0008-018] [ABS-1441] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- "" at 77% and "Does S apply to N?" — raised in [CLM-0008-018] [ABS-1442] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

The explicit questions listed above are candidates for the register (query-graph skill); no hypothesis has been entered yet.

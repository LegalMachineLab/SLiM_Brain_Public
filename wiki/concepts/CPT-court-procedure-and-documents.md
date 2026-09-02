---
id: "CPT-court-procedure-and-documents"
label: "Court procedure and decision documents"
status: "emergent"
concept_type: "other"
definition: "How courts and tribunals structure their proceedings and decision documents — multi-step and preliminary decisions, prescribed judgment elements, procedural against substantive decisions, document length — as it bears on legal AI (motivating claims: CLM-0013-023, CLM-0013-024, CLM-0013-027)."
aliases: ["multi-step proceedings", "judgment structure"]
broader: []
sources: ["SRC-0001", "SRC-0007", "SRC-0013", "SRC-0019", "SRC-0034", "SRC-0041", "SRC-0043", "SRC-0045", "SRC-0047"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Court procedure and decision documents

_Status: emergent; family: other._

## Definition

How courts and tribunals structure their proceedings and decision documents — multi-step and preliminary decisions, prescribed judgment elements, procedural against substantive decisions, document length — as it bears on legal AI (motivating claims: CLM-0013-023, CLM-0013-024, CLM-0013-027).

Aliases: multi-step proceedings, judgment structure.

## Claims about the concept

### Descriptive

**BR**

- Briggs of Westbourne (2026) state that Brazil regulates judges' use of AI through Resolution No. 615 of 11 March 2025 (Articles 19-21), enacted by an administrative or quasi-judicial body: a dual-track approach strongly prefers court-provided AI tools, judges who use subscription LLMs are personally and entirely responsible for the resulting decisions, judges must undertake mandatory AI training before using AI products, data protection rules generally prohibit processing confidential material in private LLMs, and disclosure of AI use in written decisions is optional but the court's internal system must automatically register such use. [CLM-0047-019]. — jurisdiction: BR; basis: legislation; positive form: existence
- Briggs of Westbourne (2026) state that Brazil has struggled for some years with a staggering backlog of approximately 80 million cases, so it is no surprise that AI has gained traction there as an attractive tool for speeding up court processes. [CLM-0047-020]. — jurisdiction: BR; basis: literature

**CA**

- Mokanov (2019) state that In Canada, administrative tribunal decisions are very factual and do not usually contain many references to other cases, in contrast to judicial decisions, which cite other decisions abundantly; because of this drafting pattern, citation-parsing algorithms are of little use for identifying other cases of interest from administrative decisions. [CLM-0001-008]. — jurisdiction: CA; basis: argument; positive form: general_rule

**CoE**

- Medvedeva et al. (2021) state that Communicated cases of the European Court of Human Rights, which contain a summary of the facts and the Court's questions to the respondent government and are often published years before the case is judged, provide a unique opportunity to forecast the judgements of pending applications; the questions often reflect the Court's legal characterisation of the complaint. [CLM-0045-008]. — jurisdiction: CoE; basis: argument; positive form: general_rule

**GB**

- Xie et al. (2024) state that In contrast with typical UK judgments, UK Employment Tribunal decisions are relatively clearly structured, because there are no dissenting opinions and specific rules set out which elements a judgment must contain; nevertheless UKET judgments are not always consistent, since there are no formal rules on drafting style. [CLM-0013-023]. — jurisdiction: GB; basis: legislation; positive form: general_rule
- Xie et al. (2024) state that The resolution of a UK Employment Tribunal dispute may not be covered by one judgment only but may be determined by iterative multiple decisions resulting in various case documents, because procedural and substantive requirements may be decided at different stages, there may be multiple final hearings on liability, remedy and costs, and a party may request reconsideration. [CLM-0013-024]. — jurisdiction: GB; basis: legislation; positive form: general_rule
- Janeček (2023) state that Although court judgments in England and Wales are official public records under section 8 of the Public Records Act 1958, there is no comprehensive public database of digitised court judgments, and the centralised judgments database launched by The National Archives in 2022 does not change that. [CLM-0041-003]. — jurisdiction: GB; basis: literature
- Janeček (2023) state that Because judgments in England and Wales do not emerge from any standardised production pipeline with a transparent audit trail, a gap has arisen that is filled by commercial legal publishers, who have secured privileged access to judgments (through transcription agencies, court administrators, or early access to scattered copies) and now commercially exploit that access; research suggests these publishers already control access to a vast majority of recorded judgments. [CLM-0041-004]. — jurisdiction: GB; basis: literature
- Janeček (2023) state that In England and Wales, judgments are to be available to the public for inspection and copying under section 5(3) of the Public Records Act 1958, and under The National Archives' Open Justice Licence everyone is free to copy, publish, distribute, transmit and even commercially exploit judgments; by contrast, computational analysis of judgments is not permitted under the Open Justice Licence. [CLM-0041-015]. — jurisdiction: GB; basis: legislation
- Briggs of Westbourne (2026) state that In England and Wales the procedural groundwork for digitisation was not carried out in advance: although investment was secured, primary legislation for an Online Rules Committee was passed only in 2022, six years after the 2016 Civil Courts Structure Review recommended one, so procedural rules to accommodate digitisation were developed piecemeal and ad hoc under the Civil Procedure Rule Committee, mainly through pilot scheme practice directions under CPR Part 51. [CLM-0047-002]. — jurisdiction: GB; basis: legislation; temporal reference: 2016 to May 2026
- Briggs of Westbourne (2026) state that The 2016 Civil Courts Structure Review identified the principal weakness of the civil justice system in England and Wales as very poor access to justice for small to moderate civil claims, caused by the disproportionate cost of instructing lawyers and the risk of paying the opponent's costs, and advised that it might be remedied by a digital online court with built-in automated triage for litigants without lawyers. [CLM-0047-024]. — jurisdiction: GB; basis: literature; temporal reference: 2016

**IN**

- Khadloya et al. (2025) state that High-volume courts in India routinely face long filings and crowded dockets that lead to massive case delays, and despite near-universal digitization through e-Courts the core problem of how a judge can interrogate a voluminous record quickly and faithfully remains unsolved. [CLM-0019-002]. — jurisdiction: IN [jurisdiction inferred]; basis: literature

**IN, CN**

- Ali et al. (2021) state that An evidence information extraction approach designed for Chinese court records, which follow a relatively structured representation, may suit those records well but does not suit Indian court records, which contain descriptive and varied formats of the court proceedings. [CLM-0043-017]. — jurisdiction: IN, CN (comparative); basis: argument

**general**

- Medvedeva et al. (2021) state that Because courts provide little access to documents that exist before a judgement is made, forecasting future judgements is impossible for many online available datasets, and for this reason the large majority of machine learning systems for legal data classify court judgements rather than forecast them. [CLM-0045-012]. — jurisdiction: general; basis: argument

### Interpretive

**CoE**

- Medvedeva et al. (2021) read Outcome prediction as follows: Applications to the European Court of Human Rights found inadmissible on the merits can, from a legal point of view, be characterised as clearer 'non-violation' cases, similar to cases judged as showing no violation, because the Court has decided similar applications many times before and they do not merit a full judgement. [CLM-0045-018]. — jurisdiction: CoE; basis: argument

**GB**

- Xie et al. (2024) read Outcome prediction as follows: The possibility of multi-step UK Employment Tribunal proceedings, in which a judgment may decide only a preliminary issue (such as disability or employee status) rather than finally resolving the claim, increases the complexity of outcome prediction and has likely had a negative effect on the scores of both models and human predictors. [CLM-0013-018]. — jurisdiction: GB; basis: argument
- Xie et al. (2024) read Outcome prediction as follows: Where the UK Employment Tribunal renders a procedural decision instead of deciding the substance of a claim (labelled 'other'), both models and human annotators may predict a substantive outcome instead, a complexity that may have contributed to low evaluation scores for the 'claimant partly wins' and 'other' categories. [CLM-0013-019]. — jurisdiction: GB; basis: argument
- Briggs of Westbourne (2026) read Court procedure and decision documents as follows: The deficiency of the way procedural rules were made for digitisation in England and Wales was not the pace at which successive pilot practice directions were produced, but that the process proceeded in a vacuum of governing objectives and principles, driven by the detail of technological developments as they arrived, and that the committees supervising those developments deliberated in private, whereas the rule-making process is and should be essentially public. [CLM-0047-004]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

### Normative

**GB**

- Briggs of Westbourne (2026) argue that Procedural rules and regulation to accommodate AI in civil justice ought to be developed in advance, by defining the objectives and principles behind the rules prospectively and in a transparent environment open to public scrutiny, rather than by responding piecemeal to technological developments as they occur, as happened with digitisation. This does not require having all the answers upfront. [CLM-0047-001]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that Although pilot practice directions under CPR rule 51.2 can usefully be made and amended more simply than rules while the underlying technology is still developing, it is not desirable for a practice direction to remain in force for as long as ten years on grounds of convenience, as PD 51O did, and clear and predictable rules are to be preferred wherever possible. [CLM-0047-003]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that The courts cannot and should not try to control the tsunami of AI-enabled civil claims by increasing court fees to stem the tide. [CLM-0047-011]. — jurisdiction: GB [jurisdiction inferred]; basis: case_law (unclear)
- Briggs of Westbourne (2026) argue that To begin designing procedural rules for the AI-based innovations that will be absorbed into the civil justice system, thinking should start now about the probable applications of AI by litigants and courts and how the known risks of AI might be addressed, including whether procedural rules should mandate disclosure of AI use by litigants in person and counsel, whether counsel's expected checking of AI input should become a firm rule, and whether and how far judges' use of AI in drafting judgments must be disclosed or restricted. [CLM-0047-018]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that Given the pace of AI development, it is necessary to consider whether the current system for producing rules of civil procedure in England and Wales is sufficiently agile to keep up with the technological advances in civil process that AI is likely to produce; the system struggled to keep up with digitisation, and AI is developing much faster. [CLM-0047-022]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

### Empirical

**GB**

- Xie et al. (2024) report that The majority (approximately 62.8%) of the 52,339 UK Employment Tribunal decisions in the Cambridge Law Corpus have a decision document of just one page, many of which are short procedural decisions (such as withdrawn claims or non-responding respondents) that provide no substantial information on facts and substantive reasoning. [CLM-0013-027]. — jurisdiction: GB; basis: dataset_or_experiment

**geographical_proxy:IN**

- Malik et al. (2022) report that Annotators agree most on judgments that are written with explicit indicators before each rhetorical role, follow a consistent order of roles, and are relatively short, whereas judgments that lack such indicators, move back and forth between roles, discuss precedents in detail, or blur whether the judge is reiterating counsel's arguments or stating a view leave scope for individual discretion and subjective interpretation. [CLM-0007-020]. — jurisdiction: geographical_proxy:IN; basis: dataset_or_experiment

**undetermined**

- Hou et al. (2025) report that In a large corpus of legal case documents, approximately 10% of documents contain errors in the standardized indicative phrases that delineate sections (fact description, reasoning, decision), so rule-based segmentation with regular expressions often yields incomplete or fragmented structures; the problem is most pronounced in earlier documents and may stem from poor-quality digitization. [CLM-0034-016]. — jurisdiction: undetermined; basis: dataset_or_experiment

### Predictive

**CoE**

- Medvedeva et al. (2021) argue that Forecasting judgements from communicated cases does not allow forecasting for every future case, since not all applications are communicated to the State; forecasting from other data available before the judgement may likely be even harder, because the uniform documents the Court creates for communicated cases are likely beneficial. [CLM-0045-019]. — jurisdiction: CoE; basis: argument

**GB**

- Briggs of Westbourne (2026) argue that The AI-enabled increase in the number of civil claims will produce better access to justice only if the courts, staff and judges have the capacity to manage and adjudicate them within a reasonable time rather than adding them to a backlog; because an AI platform drafts a claim in seconds while court managers and judges take orders of magnitude longer to read and respond to it, and the taxpayer is unlikely to fund a big increase in civil court staff and judges, that capacity cannot be expected to come from more human resources. [CLM-0047-008]. — jurisdiction: GB [jurisdiction inferred]; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 9; claims: 28.

**By contribution type**

| value | sources |
|---|---|
| technical | 6 |
| empirical_quantitative | 5 |
| theoretical | 4 |
| normative | 3 |
| doctrinal | 2 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| GB | 3 |
| IN | 3 |
| CA | 1 |
| CoE | 1 |
| general | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| GB | 3 |
| IN | 2 |
| BR | 1 |
| CA | 1 |
| CN | 1 |
| CoE | 1 |
| general | 1 |
| geographical_proxy:IN | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2021 | 2 |
| 2025 | 2 |
| 2019 | 1 |
| 2022 | 1 |
| 2023 | 1 |
| 2024 | 1 |
| 2026 | 1 |

## What the sources do not address

- No conceptual claim on CPT-court-procedure-and-documents. [ABS-1387] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No methodological claim on CPT-court-procedure-and-documents. [ABS-1388] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.

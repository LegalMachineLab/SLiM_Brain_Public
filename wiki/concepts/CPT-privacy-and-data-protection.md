---
id: "CPT-privacy-and-data-protection"
label: "Privacy and data protection"
status: "anchor"
concept_type: "normative_concern"
definition: "Personal data, confidentiality, and data-protection law in legal AI."
aliases: []
broader: []
sources: ["SRC-0019", "SRC-0024", "SRC-0030", "SRC-0034", "SRC-0040", "SRC-0041", "SRC-0046", "SRC-0048", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Privacy and data protection

_Status: anchor; family: normative_concern._

## Definition

Personal data, confidentiality, and data-protection law in legal AI.

Conceptual claims on this concept, each with its source:
- Mandal and Sinha (2026): Compliance requirements facing a vertical application fall on a spectrum of three tiers — a strict liability tier of rules requiring absolute adherence on pain of criminal liability or catastrophic fines (such as GDPR, HIPAA or the EU AI Act's prohibited and high-risk categories), a tolerable penalty tier where non-compliance is a manageable business cost, and a cautionary or advisory tier with opportunities to correct and minimal penalties — and verticals and workflows in the more stringent tiers can create much deeper moats through specialised solutions. [CLM-0040-013]
- Janeček (2023): Concerns relating to judgments in the 'factual' sense (such as the sensitivity of personal information that can be mined from their text) are mistakenly treated as a reason to limit both public access to judgments and data-driven analysis of judgments as bulk data. The public interest in free access to law does not apply, at least not directly, to judgments in the factual sense, and conversely the fact that sensitive information can be mined from judgments does not imply that they should be unavailable as a jurisprudential category. [CLM-0041-002]
- Janeček (2023): Just as jurisprudential analysis of judgments is unconcerned with sensitive information about specific individuals, statistical bulk analysis of judgments is also unconcerned with individual-level insights: it reveals insights about the dataset as a whole, going beyond individual judgments, and there is no a priori reason to be concerned about such insights, which may in fact be in the public benefit. The public's concerns about the availability of judgments for bulk analysis therefore rest on reasons that are not attributable to that analysis. [CLM-0041-011]
- Gridin (2026): A legal distinction must be drawn between human surveillance and algorithmic processing: continuous facial and keystroke biometrics do not violate workplace privacy where the raw data is processed locally by the AI, never transmitted to the cloud or viewed by any human, and only a binary cryptographic confirmation token reaches the supervisor, in adherence to data minimisation. [CLM-0049-031]

## Claims about the concept

### Descriptive

**GB**

- Janeček (2023) state that There is a wide gap between the reality of court data control and processing and the public's awareness and attitudes about the use of such data: in a representative survey of 2164 adults in Great Britain, half of respondents felt uncomfortable about technology companies being able to access and use information from court records, almost two-thirds felt the government keeps the public poorly informed about current uses of court record information, and the public would prefer judgments to be bulk-analysed only if the analysis is to some extent in the public interest. [CLM-0041-006]. — jurisdiction: GB; basis: literature
- Janeček (2023) state that The public's concerns about the sensitivity of information contained in judgments play into the hands of commercial legal publishers, because it is not in the publishers' economic interest for more judgments to become available: wider availability would set back their competitive advantage and open the legal research services market to new entrants. [CLM-0041-007]. — jurisdiction: GB; basis: argument

**undetermined**

- Hou et al. (2025) state that Courts tend to be conservative about opening judicial data and legal documents in order to prevent leakage of legal data, which limits the availability of legal documents and means some data cannot be learned by LLM-related methods. [CLM-0034-015]. — jurisdiction: undetermined; basis: literature; positive form: general_rule
- Mahoney et al. (2019) state that In real-world legal matters where minimizing the time or cost of classifying a data set is paramount, for reasons such as monetary costs, sensitivity of data, or time to classify a population, the heavy human review of Continuous Active Learning is often less than ideal for lawyers classifying a population for production to an opposing party or for attorney-client privilege, and the strategy is instead to minimize human review effort and classify the population with minimal human intervention. [CLM-0046-014]. — jurisdiction: undetermined; basis: argument
- Chalkidis et al. (2021) state that Legal restrictions currently inhibit the creation of more legal NLP datasets: important document types such as contracts and scholarly publications are protected by copyright or considered trade secrets, so their owners are concerned with data leakage when the documents are used for model training and evaluation; access to court decisions is also hindered by bureaucratic inertia, outdated technology and data protection concerns, which collectively result in otherwise public decisions not being publicly available. [CLM-0048-012]. — jurisdiction: undetermined; basis: argument

### Interpretive

**US**

- Gridin (2026) read ABA Model Rules of Professional Conduct, Rule 1.1 cmt. 8 as follows: Unconstrained LLMs place attorneys in an ethical paradox between ABA Model Rule 1.1 (technological competence, under which refusing to use AI for tasks such as e-discovery could arguably constitute incompetence) and Rule 1.6 (confidentiality, violated by uploading client material to a public LLM); the Neuro-Symbolic Sandwich, operating on localised memory vaults, is currently the only structural framework that allows a practitioner to fulfil Rule 1.1 without violating Rule 1.6. [CLM-0049-012]. — jurisdiction: US; basis: legislation
- Gridin (2026) read Defend Trade Secrets Act of 2016, 18 U.S.C. § 1839(3)(A) as follows: Pasting confidential contracts, financial data, or legal arguments into a public, open-domain LLM arguably fails the 'reasonable measures' requirement of the Defend Trade Secrets Act and permanently voids federal trade secret protection, since such inputs are typically ingested by the host's servers and may train future models; strict data localisation ('LLM-in-a-Box' with on-premises or zero-retention models) and a Linear AI outbound filter preserve DTSA protection. [CLM-0049-029]. — jurisdiction: US; basis: legislation

**US, EU**

- Gridin (2026) read Fed. R. Civ. P. 45 as follows: Existing legal instruments are structurally inadequate to govern access to a cryptographically sealed, locally stored biometric telemetry vault that is at once potential evidence of insider misconduct and a repository of employees' intimate data: a FRCP Rule 45 subpoena was designed for static documentary evidence, a Fourth Amendment warrant requires probable cause and binds only government actors, and FRCP Rule 37(e) imposes a preservation duty without any access mechanism, leaving corporations a choice between spoliation sanctions and violating BIPA, GDPR Article 9 and the AI Act's biometric restrictions. [CLM-0049-033]. — jurisdiction: US, EU (cumulative); basis: legislation

**US-IL**

- Gridin (2026) read Biometric Information Privacy Act, 740 ILCS 14/15(b) as follows: Implementing continuous dual-camera authentication by streaming and storing raw employee facial video on centralised servers would constitute a systemic violation of the Illinois Biometric Information Privacy Act; processing biometric input entirely on the local edge device, transmitting only a binary zero-knowledge token, and sealing the raw telemetry behind a Digital Warrant inherently minimises BIPA exposure while preserving the evidentiary chain of custody. [CLM-0049-030]. — jurisdiction: US-IL; basis: legislation

### Normative

**US, EU, CoE**

- Gridin (2026) argue that Access to sealed biometric evidentiary vaults should be governed by a 'Digital Warrant': a multi-signature cryptographic authorisation instrument synthesising the warrant doctrine (Fourth Amendment / ECHR Article 8), data minimisation (GDPR Article 5(1)(c) / AI Act Article 10), and chain-of-custody doctrine (FRE Rules 901-902), executed in five stages - algorithmic triggering, multi-signature authorisation by an Internal Compliance Tribunal including a Data Protection Officer, temporally scoped decryption, judicial override, and an immutable audit trail - and deployable within existing corporate governance without new primary legislation. [CLM-0049-034]. — jurisdiction: US, EU, CoE (cumulative); basis: argument

**general**

- Nay et al. (2023) argue that Rigorous safeguards should be put in place as LLMs are deployed for legal services, given the sensitive nature of legal work: increasing data privacy, minimising bias, maintaining accountability for decisions made with the models' help, and evaluating the suitability of the LLM for each use case, which makes systematic evaluations necessary. [CLM-0024-018]. — jurisdiction: general; basis: argument
- Janeček (2023) argue that The risks stemming from nefarious computational analyses of judgments should not be confused with the risks of making judgment data available or of analysing judgments as 'factual' data; nefarious uses of the insights produced by computational analysis of judgments as bulk data may be regulated, but that does not mean the analysis itself should be banned, let alone that public access to judgments should be limited. [CLM-0041-012]. — jurisdiction: general; basis: argument

### Empirical

**geographical_proxy:CN**

- Li et al. (2024) report that At the Ethic level of legal cognitive ability, even GPT-4, which shows relatively good performance, remains far from satisfactory, and the unsatisfactory performance of LLMs on ethics-related legal tasks poses serious challenges to their safe application in real-life scenarios. [CLM-0030-021]. — jurisdiction: geographical_proxy:CN; basis: dataset_or_experiment

### Conceptual

**general**

- Mandal and Sinha (2026) argue that Compliance requirements facing a vertical application fall on a spectrum of three tiers — a strict liability tier of rules requiring absolute adherence on pain of criminal liability or catastrophic fines (such as GDPR, HIPAA or the EU AI Act's prohibited and high-risk categories), a tolerable penalty tier where non-compliance is a manageable business cost, and a cautionary or advisory tier with opportunities to correct and minimal penalties — and verticals and workflows in the more stringent tiers can create much deeper moats through specialised solutions. [CLM-0040-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Janeček (2023) argue that Concerns relating to judgments in the 'factual' sense (such as the sensitivity of personal information that can be mined from their text) are mistakenly treated as a reason to limit both public access to judgments and data-driven analysis of judgments as bulk data. The public interest in free access to law does not apply, at least not directly, to judgments in the factual sense, and conversely the fact that sensitive information can be mined from judgments does not imply that they should be unavailable as a jurisprudential category. [CLM-0041-002]. — jurisdiction: general; basis: argument
- Janeček (2023) argue that Just as jurisprudential analysis of judgments is unconcerned with sensitive information about specific individuals, statistical bulk analysis of judgments is also unconcerned with individual-level insights: it reveals insights about the dataset as a whole, going beyond individual judgments, and there is no a priori reason to be concerned about such insights, which may in fact be in the public benefit. The public's concerns about the availability of judgments for bulk analysis therefore rest on reasons that are not attributable to that analysis. [CLM-0041-011]. — jurisdiction: general; basis: argument
- Gridin (2026) argue that A legal distinction must be drawn between human surveillance and algorithmic processing: continuous facial and keystroke biometrics do not violate workplace privacy where the raw data is processed locally by the AI, never transmitted to the cloud or viewed by any human, and only a binary cryptographic confirmation token reaches the supervisor, in adherence to data minimisation. [CLM-0049-031]. — jurisdiction: general [jurisdiction inferred]; basis: argument

### Methodological

**general**

- Khadloya et al. (2025) argue that A courtroom AI system should run all its components (speech recognition, routing, retrieval, viewer) as independent services within the court's own infrastructure, store no audio, keep user data off foreign APIs, and log only structured commands and anchor identifiers for auditing. [CLM-0019-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that Traditional perimeter defences are inadequate for protecting sensitive legal data from insider threats; personal Edge AI Hubs should be governed by a Zero-Trust Architecture combining continuous multimodal authentication with a proprietary Codification Table micro-ledger in which every touchpoint appends a compressed code, producing a system of absolute non-repudiation in which the origin of any divergence is permanently etched into the digital chain of custody. [CLM-0049-032]. — jurisdiction: general; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that Just as jurisprudential analysis of judgments is unconcerned with sensitive information about specific individuals, statistical bulk analysis of judgments is also unconcerned with individual-level insights: it reveals insights about the dataset as a whole, going beyond individual judgments, and there is no a priori reason to be concerned about such insights, which may in fact be in the public benefit. The public's concerns about the availability of judgments for bulk analysis therefore rest on reasons that are not attributable to that analysis. [CLM-0041-011] is in tension with the claim that Courts tend to be conservative about opening judicial data and legal documents in order to prevent leakage of legal data, which limits the availability of legal documents and means some data cannot be learned by LLM-related methods. [CLM-0034-015] (inferred, medium). Note: One reports courts restricting judicial data to prevent leakage of sensitive information; the other argues that statistical bulk analysis of judgments does not itself produce individual-level sensitive information, so that concern is misapplied to bulk access.

## Distribution

Sources with claims on this concept: 9; claims: 19.

**By contribution type**

| value | sources |
|---|---|
| technical | 6 |
| empirical_quantitative | 5 |
| theoretical | 5 |
| normative | 3 |
| doctrinal | 2 |
| empirical_qualitative | 1 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 3 |
| general | 3 |
| CN | 1 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| IN | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 5 |
| undetermined | 3 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| US | 1 |
| US-IL | 1 |
| geographical_proxy:CN | 1 |

**By year**

| value | sources |
|---|---|
| 2023 | 2 |
| 2025 | 2 |
| 2026 | 2 |
| 2019 | 1 |
| 2021 | 1 |
| 2024 | 1 |

## What the sources do not address

- No predictive claim on CPT-privacy-and-data-protection. [ABS-1435] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.

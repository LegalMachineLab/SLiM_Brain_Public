---
id: "CPT-security-and-misuse"
label: "Security and misuse"
status: "anchor"
concept_type: "normative_concern"
definition: "Adversarial use, manipulation, security risks, and misuse of AI in legal settings."
aliases: []
broader: []
sources: ["SRC-0019", "SRC-0039", "SRC-0041", "SRC-0049"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# Security and misuse

_Status: anchor; family: normative_concern._

## Definition

Adversarial use, manipulation, security risks, and misuse of AI in legal settings.

Conceptual claims on this concept, each with its source:
- Gridin (2026): A legal distinction must be drawn between human surveillance and algorithmic processing: continuous facial and keystroke biometrics do not violate workplace privacy where the raw data is processed locally by the AI, never transmitted to the cloud or viewed by any human, and only a binary cryptographic confirmation token reaches the supervisor, in adherence to data minimisation. [CLM-0049-031]
- Gridin (2026): The same deterministic architecture that makes AI the most powerful tool for legal transparency is, without procedural constraints, equally capable of becoming an instrument of systematic surveillance and arbitrary control; whether a system functions as a transparency mechanism or a surveillance apparatus is determined not by the technology but by three design choices - a Digital Warrant governing biometric access, an Algorithmic Due Process escalation matrix, and distributed multi-signature governance - so the choice is between constitutional philosophies of governance, not between technologies. [CLM-0049-043]

## Claims about the concept

### Interpretive

**US**

- Gridin (2026) read Fed. R. Evid. 901(a) as follows: Under FRE Rule 901, passwords and basic two-factor authentication are increasingly insufficient to authenticate AI-assisted documents against 'deepfake' or 'the AI did it' defences; continuous multimodal biometric telemetry (spatial and facial cameras, keystroke dynamics) combined with the linear micro-ledger proves what the AI generated and who reviewed and cryptographically signed it, satisfying the Rule 901 authentication threshold. [CLM-0049-028]. — jurisdiction: US; basis: legislation
- Gridin (2026) read Defend Trade Secrets Act of 2016, 18 U.S.C. § 1839(3)(A) as follows: Pasting confidential contracts, financial data, or legal arguments into a public, open-domain LLM arguably fails the 'reasonable measures' requirement of the Defend Trade Secrets Act and permanently voids federal trade secret protection, since such inputs are typically ingested by the host's servers and may train future models; strict data localisation ('LLM-in-a-Box' with on-premises or zero-retention models) and a Linear AI outbound filter preserve DTSA protection. [CLM-0049-029]. — jurisdiction: US; basis: legislation

**US, EU**

- Gridin (2026) read Fed. R. Civ. P. 45 as follows: Existing legal instruments are structurally inadequate to govern access to a cryptographically sealed, locally stored biometric telemetry vault that is at once potential evidence of insider misconduct and a repository of employees' intimate data: a FRCP Rule 45 subpoena was designed for static documentary evidence, a Fourth Amendment warrant requires probable cause and binds only government actors, and FRCP Rule 37(e) imposes a preservation duty without any access mechanism, leaving corporations a choice between spoliation sanctions and violating BIPA, GDPR Article 9 and the AI Act's biometric restrictions. [CLM-0049-033]. — jurisdiction: US, EU (cumulative); basis: legislation

**US-IL**

- Gridin (2026) read Biometric Information Privacy Act, 740 ILCS 14/15(b) as follows: Implementing continuous dual-camera authentication by streaming and storing raw employee facial video on centralised servers would constitute a systemic violation of the Illinois Biometric Information Privacy Act; processing biometric input entirely on the local edge device, transmitting only a binary zero-knowledge token, and sealing the raw telemetry behind a Digital Warrant inherently minimises BIPA exposure while preserving the evidentiary chain of custody. [CLM-0049-030]. — jurisdiction: US-IL; basis: legislation

### Normative

**US**

- Miller (2025) argue that The danger that generative AI companies will manipulate their models as litigants is overstated, since a judge fearing manipulation by a party can simply refrain from using the tool under that party's control; the true potential danger lies in backroom deals between generative AI firms and well-funded future litigants purchasing interpretive strength, so judges should look not just to the parties of the case but to its financial stakes and to the resources currently required to alter a given model. [CLM-0039-022]. — jurisdiction: US [jurisdiction inferred]; basis: argument

**US, EU, CoE**

- Gridin (2026) argue that Access to sealed biometric evidentiary vaults should be governed by a 'Digital Warrant': a multi-signature cryptographic authorisation instrument synthesising the warrant doctrine (Fourth Amendment / ECHR Article 8), data minimisation (GDPR Article 5(1)(c) / AI Act Article 10), and chain-of-custody doctrine (FRE Rules 901-902), executed in five stages - algorithmic triggering, multi-signature authorisation by an Internal Compliance Tribunal including a Data Protection Officer, temporally scoped decryption, judicial override, and an immutable audit trail - and deployable within existing corporate governance without new primary legislation. [CLM-0049-034]. — jurisdiction: US, EU, CoE (cumulative); basis: argument

**general**

- Janeček (2023) argue that The risks stemming from nefarious computational analyses of judgments should not be confused with the risks of making judgment data available or of analysing judgments as 'factual' data; nefarious uses of the insights produced by computational analysis of judgments as bulk data may be regulated, but that does not mean the analysis itself should be banned, let alone that public access to judgments should be limited. [CLM-0041-012]. — jurisdiction: general; basis: argument

### Conceptual

**general**

- Gridin (2026) argue that A legal distinction must be drawn between human surveillance and algorithmic processing: continuous facial and keystroke biometrics do not violate workplace privacy where the raw data is processed locally by the AI, never transmitted to the cloud or viewed by any human, and only a binary cryptographic confirmation token reaches the supervisor, in adherence to data minimisation. [CLM-0049-031]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that The same deterministic architecture that makes AI the most powerful tool for legal transparency is, without procedural constraints, equally capable of becoming an instrument of systematic surveillance and arbitrary control; whether a system functions as a transparency mechanism or a surveillance apparatus is determined not by the technology but by three design choices - a Digital Warrant governing biometric access, an Algorithmic Due Process escalation matrix, and distributed multi-signature governance - so the choice is between constitutional philosophies of governance, not between technologies. [CLM-0049-043]. — jurisdiction: general; basis: argument

### Predictive

**US**

- Miller (2025) argue that Because Judge Newsom is likely among the first to use LLMs for interpretation, it is unlikely that model parameters were adjusted with the purpose of skewing results toward particular legal outcomes, which attenuates though does not eliminate the concern about the subjectivity of training weights; but should LLMs become more prevalent in interpretation, that neutrality might disappear. [CLM-0039-023]. — jurisdiction: US [jurisdiction inferred]; basis: argument

### Methodological

**general**

- Khadloya et al. (2025) argue that A courtroom AI system should run all its components (speech recognition, routing, retrieval, viewer) as independent services within the court's own infrastructure, store no audio, keep user data off foreign APIs, and log only structured commands and anchor identifiers for auditing. [CLM-0019-012]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that Traditional perimeter defences are inadequate for protecting sensitive legal data from insider threats; personal Edge AI Hubs should be governed by a Zero-Trust Architecture combining continuous multimodal authentication with a proprietary Codification Table micro-ledger in which every touchpoint appends a compressed code, producing a system of absolute non-repudiation in which the origin of any divergence is permanently etched into the digital chain of custody. [CLM-0049-032]. — jurisdiction: general; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- none

## Distribution

Sources with claims on this concept: 4; claims: 12.

**By contribution type**

| value | sources |
|---|---|
| doctrinal | 3 |
| normative | 3 |
| technical | 3 |
| theoretical | 2 |
| empirical_qualitative | 1 |
| empirical_quantitative | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| US | 2 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| IN | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| US | 2 |
| CoE | 1 |
| EU | 1 |
| US-IL | 1 |

**By year**

| value | sources |
|---|---|
| 2025 | 2 |
| 2023 | 1 |
| 2026 | 1 |

## What the sources do not address

- No descriptive claim on CPT-security-and-misuse. [ABS-1449] candidate readings: gap_in_literature | extraction_shadow | tacit_link
- No empirical claim on CPT-security-and-misuse. [ABS-1450] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.

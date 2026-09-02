---
id: "CPT-ai-governance-and-alignment"
label: "AI governance and alignment"
status: "emergent"
concept_type: "normative_concern"
definition: "Governing, regulating and aligning AI systems themselves — law-informed alignment, operationalising ethical or legal principles as machine-checkable constraints, and regulatory regimes for AI (motivating claims: CLM-0024-016, CLM-0024-019)."
aliases: ["law informs code", "AI regulation"]
broader: []
sources: ["SRC-0024", "SRC-0025", "SRC-0030", "SRC-0040", "SRC-0047", "SRC-0049", "SRC-0050"]
deprecated: false
replaced_by:
created: "2026-09-02"
---

# AI governance and alignment

_Status: emergent; family: normative_concern._

## Definition

Governing, regulating and aligning AI systems themselves — law-informed alignment, operationalising ethical or legal principles as machine-checkable constraints, and regulatory regimes for AI (motivating claims: CLM-0024-016, CLM-0024-019).

Conceptual claims on this concept, each with its source:
- Nay et al. (2023): Methods that improve LLMs' legal analysis skills are relevant to aligning AI with humans and governing AI: an LLM that grasps the law could 'self-police' to act in accordance with law, or separate models could apply legal and ethical standards to confirm whether another AI is properly aligned with the law (the 'Law Informs Code' approach). [CLM-0024-016]
- Getir Yaman et al. (2023): By enabling the operationalisation of SLEEC requirements for autonomous agents, a formal specification, validation and verification framework complements the international efforts to define ethical principles for AI and autonomous systems (such as the UNESCO and OECD recommendations) and work that elicits SLEEC requirements from normative principles and stakeholder needs. [CLM-0025-017]
- Mandal and Sinha (2026): Compliance requirements facing a vertical application fall on a spectrum of three tiers — a strict liability tier of rules requiring absolute adherence on pain of criminal liability or catastrophic fines (such as GDPR, HIPAA or the EU AI Act's prohibited and high-risk categories), a tolerable penalty tier where non-compliance is a manageable business cost, and a cautionary or advisory tier with opportunities to correct and minimal penalties — and verticals and workflows in the more stringent tiers can create much deeper moats through specialised solutions. [CLM-0040-013]
- Gridin (2026): Under a modified Learned Hand calculus (RISK_total = P(failure) x L_legal + C_compliance, and TC = C_dev + min(C_compliance, P_fine + P_lawsuit)), deploying deterministic Linear AI agents drives the probability of hallucination-driven failure to near zero, so that the cost of internal self-regulation is structurally bounded and vastly cheaper than the unbounded aggregate risk of US tort litigation or EU fines; the modelling is stylised and illustrates structural incentives rather than actuarial estimates. [CLM-0049-020]
- Gridin (2026): The same deterministic architecture that makes AI the most powerful tool for legal transparency is, without procedural constraints, equally capable of becoming an instrument of systematic surveillance and arbitrary control; whether a system functions as a transparency mechanism or a surveillance apparatus is determined not by the technology but by three design choices - a Digital Warrant governing biometric access, an Algorithmic Due Process escalation matrix, and distributed multi-signature governance - so the choice is between constitutional philosophies of governance, not between technologies. [CLM-0049-043]
- Neumann et al. (2026): The goals that researchers attribute to system-level instructions fall into eight categories of two types: six system goals that target the behaviour of the AI system itself (alignment, accessibility, adaptability, performance, stability, security) and two prompt goals that target the instructions themselves as artefacts (implementation, auditability). [CLM-0050-002]
- Neumann et al. (2026): Regulators necessarily interpret natural-language prompts through social, legal and institutional understandings of meaning, obligation and intent, which is not comparable to how language models process instruction text through layers of statistical pattern matching shaped by training and sensitive to phrasing and context; linguistic accessibility therefore risks importing human interpretive assumptions into machine governance. [CLM-0050-010]

Aliases: law informs code, AI regulation.

## Claims about the concept

### Descriptive

**BR**

- Briggs of Westbourne (2026) state that Brazil regulates judges' use of AI through Resolution No. 615 of 11 March 2025 (Articles 19-21), enacted by an administrative or quasi-judicial body: a dual-track approach strongly prefers court-provided AI tools, judges who use subscription LLMs are personally and entirely responsible for the resulting decisions, judges must undertake mandatory AI training before using AI products, data protection rules generally prohibit processing confidential material in private LLMs, and disclosure of AI use in written decisions is optional but the court's internal system must automatically register such use. [CLM-0047-019]. — jurisdiction: BR; basis: legislation; positive form: existence

**EU, US**

- Gridin (2026) state that The global landscape of AI regulation is fracturing into two opposed paradigms: the European Union, through the AI Act, has codified strict ex-ante preventative control with pre-market audits and heavy fines, while the United States, following the repeal of Executive Order 14110 and the issuance of Executive Order 14179 in 2025, has embraced algorithmic deregulation that leaves AI safety to the market and ex-post tort liability; this places multinational legal entities in a structurally irresolvable compliance tension. [CLM-0049-018]. — jurisdiction: EU, US (comparative); basis: legislation; positive form: split
- Gridin (2026) state that Existing scholarship has not produced a formalised legal-architectural framework that simultaneously satisfies the transparency mandates of the EU AI Act, the evidentiary requirements of US procedural law, and the biometric privacy obligations under GDPR and BIPA while remaining operationally deployable by legal practitioners without specialised engineering expertise. [CLM-0049-047]. — jurisdiction: EU, US (cumulative); basis: none_stated
- Neumann et al. (2026) state that The EU and US approaches diverge: the EU Code of Practice operationalises system-level instructions as artefacts for evaluation practice by providing them to model evaluation teams, whereas the US framework positions system prompts as optional transparency artefacts without specifying how their behavioural effects should be assessed and more strongly implies that writing high-level normative commitments into system-level instructions can support alignment with articulated values. [CLM-0050-007]. — jurisdiction: EU, US (comparative); basis: legislation; positive form: split

**US**

- Mandal and Sinha (2026) state that FINRA's 2026 regulatory oversight report explicitly pivots from AI guidance to accountability, demanding that firms document how their AI systems are supervised. [CLM-0040-015]. — jurisdiction: US [jurisdiction inferred]; basis: literature; positive form: trend

**US, EU**

- Neumann et al. (2026) state that Emerging governance instruments in the United States (Executive Order 14319 and the OMB memorandum on Unbiased AI Principles) and the European Union (General-Purpose AI Code of Practice) treat system prompts as legible artefacts that can be disclosed, inspected and revised to support oversight, on the presumption that prompt language shapes system behaviour, so that regulators treat prompt language as a proxy for model performance. [CLM-0050-004]. — jurisdiction: US, EU (comparative); basis: legislation; positive form: general_rule

**general**

- Getir Yaman et al. (2023) state that Although social, legal, ethical, empathetic and cultural (SLEEC) requirements for autonomous agents are recognised as increasingly important, there is currently very little support for their elicitation, specification, validation and verification; existing research is promising but covers only specific aspects of the problem. [CLM-0025-001]. — jurisdiction: general; basis: literature
- Getir Yaman et al. (2023) state that Existing formal verification approaches for autonomous systems mostly focus on the agents' safety requirements, and prior work on verifying ethical and legal constraints of robots does not address the operationalisation of such requirements and provides no notation dedicated to encoding SLEEC-related concerns as requirements; the SLEEC framework is distinctive in addressing the operationalisation of norms while leaving the identification of rules to complementary work. [CLM-0025-016]. — jurisdiction: general; basis: literature
- Gridin (2026) state that The contest over which normative framework will govern AI in high-stakes institutional contexts has three participants, not two: alongside the EU's ex-ante model and the US deregulatory paradigm, the alternative AI governance models emerging in China, the Russian Federation, the Gulf states and BRICS jurisdictions are increasingly relevant and conspicuously underrepresented in Western-centric legal AI scholarship. [CLM-0049-048]. — jurisdiction: general [jurisdiction inferred]; basis: none_stated

### Interpretive

**EU**

- Gridin (2026) read AI Act, Art. 14 as follows: The Human-in-the-Loop paradigm, as mandated by Article 14 of the EU AI Act and widely adopted as the default safeguard in corporate AI governance, is a structural placebo: mandating human oversight in the absence of architectural guardrails does not prevent catastrophic errors but merely redistributes liability onto operators who are cognitively and technically unequipped to intercept them. [CLM-0049-007]. — jurisdiction: EU; basis: literature
- Gridin (2026) read AI Act, Art. 9(1) as follows: Satisfying Article 9 of the EU AI Act (a continuous, iterative risk management system throughout the lifecycle of a high-risk system) solely through manual human audits is economically and practically impossible given the volume and velocity of legal data processing; passing every LLM output through deterministic Linear AI wrappers before execution performs a systematic risk audit on every transaction and thereby automates compliance with Article 9. [CLM-0049-022]. — jurisdiction: EU; basis: legislation
- Gridin (2026) read AI Act, Art. 13(1) as follows: Deploying a raw, unconstrained generative LLM in a high-stakes legal setting is a fundamental and inescapable violation of Article 13 of the EU AI Act, because a deep neural network with hundreds of billions of weights cannot provide a transparent, linear logic path enabling deployers to interpret its output, and any post-hoc explanation the LLM generates is merely another probabilistic guess. [CLM-0049-023]. — jurisdiction: EU; basis: legislation
- Gridin (2026) read AI Act, Art. 13(1) as follows: The transparency requirement of Article 13 of the EU AI Act can be satisfied not by explaining the deep neural network but by structurally barricading the deployer from it: when the output delivered to the human is certified by a deterministic Linear AI agent operating on observable Boolean conditions, and each action leaves a micro-code decodable through the organisation's Codification Reference Directory, the deployer receives exact, interpretable criteria. [CLM-0049-024]. — jurisdiction: EU; basis: legislation
- Gridin (2026) read AI Act, Art. 14(1) as follows: Article 14 of the EU AI Act (human oversight, including the capacity to override or reverse a high-risk system's output and awareness of automation bias) can be translated directly into executable code by demoting the AI to a decision-support tool: no LLM or Linear AI agent may execute a final legal action without a human cryptographic signature, a formalised and logged Algorithmic Appeal provides the right to override, and a 'Red Zone' executive dashboard with kill-switch authority counters automation bias as required by Article 14(4)(b). [CLM-0049-025]. — jurisdiction: EU; basis: legislation
- Neumann et al. (2026) read General-Purpose AI Code of Practice (EU, 10 July 2025), Measure 7.1 as follows: The EU General-Purpose AI Code of Practice treats the system prompt as part of the model specification to be disclosed to evaluation teams for models presenting systemic risk, but it does not operationalise the multiple layers of system-level instructions across the AI supply chain and does not require prompt versioning, change logs, or triggers for re-evaluation when system prompts are updated, so that disclosure can quickly become outdated. [CLM-0050-006]. — jurisdiction: EU; basis: legislation

**US**

- Neumann et al. (2026) read Executive Order 14319, Preventing Woke AI in the Federal Government (July 2025), Sec. 3 as follows: The United States federal procurement framework (Executive Order 14319 and the OMB memorandum implementing it) treats system prompts as an optional transparency artefact whose disclosure may evidence compliance with the Unbiased AI Principles, does not require empirical evaluation of their behavioural effects, and, by excluding system prompts from its model-evaluations section, embeds an implicit assumption that inspecting prompt language is sufficient. [CLM-0050-005]. — jurisdiction: US; basis: legislation

**US, EU**

- Gridin (2026) read Fed. R. Civ. P. 45 as follows: Existing legal instruments are structurally inadequate to govern access to a cryptographically sealed, locally stored biometric telemetry vault that is at once potential evidence of insider misconduct and a repository of employees' intimate data: a FRCP Rule 45 subpoena was designed for static documentary evidence, a Fourth Amendment warrant requires probable cause and binds only government actors, and FRCP Rule 37(e) imposes a preservation duty without any access mechanism, leaving corporations a choice between spoliation sanctions and violating BIPA, GDPR Article 9 and the AI Act's biometric restrictions. [CLM-0049-033]. — jurisdiction: US, EU (cumulative); basis: legislation
- Neumann et al. (2026) read Executive Order 14319, Preventing Woke AI in the Federal Government (July 2025) as follows: Governance approaches that target system prompts rest on two assumptions — that stakeholders can infer intent from instruction text and that they can accurately predict model behaviour from those instructions — and neither assumption reliably holds, because the research evidence describes prompt effects as context-dependent, sensitive to phrasing and ordering, and vulnerable to interaction effects across multi-turn conversations and layered instructions. [CLM-0050-008]. — jurisdiction: US, EU (cumulative) [jurisdiction inferred]; basis: literature

**general**

- Neumann et al. (2026) read AI governance and alignment as follows: Improvements in model capability alone cannot resolve the concerns about prompt-based governance, because the core governance challenge is structural: prompt text is an accessible representation of intended constraints but not a reliable substitute for evidence about the realistic behaviour of layered systems, so instruments that treat writing or inspecting a sentence as a primary mechanism of behavioural control risk overstating the impact of prompt interventions and understating the need for evaluation and accountability mechanisms. [CLM-0050-022]. — jurisdiction: general; basis: argument

### Normative

**EU**

- Gridin (2026) argue that Automation bias cannot be remedied by legislation: statutory mandates such as Article 14 of the EU AI Act cannot debias human psychology when users face authoritative, anthropomorphic AI interfaces, so the error must be intercepted computationally by multi-layered neuro-symbolic defences before it ever reaches the human interface. [CLM-0049-008]. — jurisdiction: EU; basis: literature
- Gridin (2026) argue that Transparency and explainability mandates are necessary but insufficient: Article 14 of the EU AI Act identifies human oversight as a requirement but provides no architectural specification for achieving it, so future regulatory instruments, including the AI Act's implementing acts and harmonised standards, should incorporate minimum architectural requirements for AI in high-risk legal contexts - mandatory deterministic validation layers, immutable audit logging, and formalised access-authorisation protocols for biometric evidentiary data. [CLM-0049-038]. — jurisdiction: EU; basis: argument
- Gridin (2026) argue that The industry norm of releasing generative foundation models as standalone products with post-hoc XAI layers appended must be abandoned; as enforcement under Articles 9 and 14 of the EU AI Act emerges, the liability trajectory for providers of unguarded high-risk systems will become untenable, and releasing the LLM only within a pre-packaged deterministic validation environment is the commercially rational and legally defensible product architecture for the high-stakes legal market. [CLM-0049-039]. — jurisdiction: EU; basis: argument

**EU, CoE**

- Gridin (2026) argue that Human oversight of high-risk AI requires a formalised 'Right to Override' operationalised as a digitally recorded three-tier Escalation Matrix - technical remediation, cognitive re-evaluation by a higher-capacity LLM, and an executive human consortium - which converts the deterministic system from an unchecked algorithmic tribunal into a reviewable decision-support system and turns the abstract contestability mandated by Article 14 of the EU AI Act and Article 14 of the Council of Europe AI Convention into an enforceable procedural mechanism. [CLM-0049-036]. — jurisdiction: EU, CoE (cumulative); basis: argument

**EU, US**

- Gridin (2026) argue that The transatlantic regulatory chasm is architecturally bridgeable: by establishing a single apex internal 'High Trust' standard (Risk Interoperability) whose Neuro-Symbolic architecture satisfies the EU AI Act's strictest transparency criteria while generating the cryptographic audit trail required by US tort law, a corporation can dissolve the binary compliance trap without legislative harmonisation, and sandboxed 'Shadow AI Governance' deployment lets it achieve US innovation velocity while producing the evidentiary logs European regulators require. [CLM-0049-019]. — jurisdiction: EU, US (comparative); basis: argument

**GB**

- Briggs of Westbourne (2026) argue that Procedural rules and regulation to accommodate AI in civil justice ought to be developed in advance, by defining the objectives and principles behind the rules prospectively and in a transparent environment open to public scrutiny, rather than by responding piecemeal to technological developments as they occur, as happened with digitisation. This does not require having all the answers upfront. [CLM-0047-001]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that Although pilot practice directions under CPR rule 51.2 can usefully be made and amended more simply than rules while the underlying technology is still developing, it is not desirable for a practice direction to remain in force for as long as ten years on grounds of convenience, as PD 51O did, and clear and predictable rules are to be preferred wherever possible. [CLM-0047-003]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that To begin designing procedural rules for the AI-based innovations that will be absorbed into the civil justice system, thinking should start now about the probable applications of AI by litigants and courts and how the known risks of AI might be addressed, including whether procedural rules should mandate disclosure of AI use by litigants in person and counsel, whether counsel's expected checking of AI input should become a firm rule, and whether and how far judges' use of AI in drafting judgments must be disclosed or restricted. [CLM-0047-018]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that Given the pace of AI development, it is necessary to consider whether the current system for producing rules of civil procedure in England and Wales is sufficiently agile to keep up with the technological advances in civil process that AI is likely to produce; the system struggled to keep up with digitisation, and AI is developing much faster. [CLM-0047-022]. — jurisdiction: GB [jurisdiction inferred]; basis: argument
- Briggs of Westbourne (2026) argue that Procedure rules may well not be the main way of keeping AI in the civil legal arena within democratically acceptable bounds, because the platforms delivering AI-generated legal services are owned by a very small number of large, mainly USA-owned corporations that are neither regulated by nor loyal to the UK and do not perform a vocation, unlike human lawyers and judges who are bound by professional ethics, regulation and the judicial oath; other forms of regulatory discipline may need to be devised from ground zero rather than from within the Civil Procedure Rules. [CLM-0047-023]. — jurisdiction: GB; basis: argument

**GB, BR**

- Briggs of Westbourne (2026) argue that In preparing for the tsunami of AI-generated cases, it is instructive to consider the approaches of jurisdictions that were early adopters of AI: without judging whether Brazil's rules are effective or sufficient, the Brazilian framework highlights the kinds of policy choices and problems that rules will have to address if civil courts and judges are to use AI platforms transparently and with public approval, and these ought to be thought about in earnest now. [CLM-0047-021]. — jurisdiction: GB, BR (comparative) [jurisdiction inferred]; basis: argument

**general**

- Li et al. (2024) argue that To address LLMs' unsatisfactory performance on ethics-related legal tasks, more advanced and precise alignment strategies should be devised, and the supervision and evaluation of LLMs should be strengthened to ensure they conform to ethical standards and moral requirements in practical applications. [CLM-0030-022]. — jurisdiction: general; basis: argument
- Gridin (2026) argue that The maturation of AI under the Rule of Law cannot be achieved through governance frameworks or legislative policy alone; it requires the codification of legal obligation directly into software architecture (a principle termed 'jurisprudential engineering'), so that compliance becomes a function of code rather than of policy. [CLM-0049-001]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Governing generative AI by natural language should be approached cautiously, because writing rules that govern machines requires different approaches than writing rules that govern humans. [CLM-0050-011]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Prompt governance must address the malleability of instructions and account for the layered instruction stacks that arise across AI supply chains, because multiple stakeholders introduce interacting and possibly conflicting instruction layers not visible to all actors; treating a single static system prompt as the governance object risks misspecifying the system actually being governed and complicates accountability attribution, disclosure and enforcement. [CLM-0050-015]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Stakeholders should resist governance by affordance: the ease of writing and accessing a prompt should not determine the scope of governance, and actual behavioural outcomes of the socio-technical system assessed through evaluation regimes must take precedence over textual artefacts; disclosure of prompt language is plausible as a starting point for governance and evaluation but not as a substitute for behavioural evidence, so textual requirements should be paired with targeted evaluation documentation rather than blanket requirements. [CLM-0050-016]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Systematic prompt tests with clear thresholds should be set and met before public release to minimise trial-and-error deployment, and any standardisation of system-level instructions should not target specific words or prompt templates unless robustness across implementations has been shown; specialised intermediary roles could translate governance objectives into prompt specifications and validate their behavioural effects. [CLM-0050-017]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Prompt versioning and documentation of justified prompt modifications enable meaningful re-evaluation by multiple stakeholders, and evaluations of system-level instructions should be mindful of the prompt stack, including how instructions from multiple stakeholders interact in related or conflicting configurations; effective governance further requires cross-disciplinary collaboration because neither linguistic nor technical expertise alone suffices to specify, implement, or assess instruction-based controls. [CLM-0050-018]. — jurisdiction: general; basis: argument

**undetermined**

- Gridin (2026) argue that State AI Regulatory Bodies should be established to define strict certification standards for Centralized Analytical Centers, mandating minimum memory capacities, intelligence thresholds, and micro-agent densities according to the deploying entity's systemic importance. [CLM-0049-051]. — jurisdiction: undetermined; basis: none_stated

### Empirical

**US, EU, GB, AU, SG**

- Neumann et al. (2026) report that System-level instructions appear as an explicit object of governance in only a small number of policy and governance documents; a scoping search across jurisdictions identified eight documents that substantively address them as governable artefacts. [CLM-0050-003]. — jurisdiction: US, EU, GB, AU, SG (cumulative); basis: dataset_or_experiment

**general**

- Neumann et al. (2026) report that The research literature on system-level instructions (system prompts) is fragmented and advances divergent and sometimes contradictory claims about what goals such instructions can achieve, under what conditions, and with what reliability. [CLM-0050-001]. — jurisdiction: general; basis: literature

### Conceptual

**US, EU**

- Gridin (2026) argue that Under a modified Learned Hand calculus (RISK_total = P(failure) x L_legal + C_compliance, and TC = C_dev + min(C_compliance, P_fine + P_lawsuit)), deploying deterministic Linear AI agents drives the probability of hallucination-driven failure to near zero, so that the cost of internal self-regulation is structurally bounded and vastly cheaper than the unbounded aggregate risk of US tort litigation or EU fines; the modelling is stylised and illustrates structural incentives rather than actuarial estimates. [CLM-0049-020]. — jurisdiction: US, EU (cumulative); basis: argument

**general**

- Nay et al. (2023) argue that Methods that improve LLMs' legal analysis skills are relevant to aligning AI with humans and governing AI: an LLM that grasps the law could 'self-police' to act in accordance with law, or separate models could apply legal and ethical standards to confirm whether another AI is properly aligned with the law (the 'Law Informs Code' approach). [CLM-0024-016]. — jurisdiction: general; basis: argument
- Getir Yaman et al. (2023) argue that By enabling the operationalisation of SLEEC requirements for autonomous agents, a formal specification, validation and verification framework complements the international efforts to define ethical principles for AI and autonomous systems (such as the UNESCO and OECD recommendations) and work that elicits SLEEC requirements from normative principles and stakeholder needs. [CLM-0025-017]. — jurisdiction: general; basis: argument
- Mandal and Sinha (2026) argue that Compliance requirements facing a vertical application fall on a spectrum of three tiers — a strict liability tier of rules requiring absolute adherence on pain of criminal liability or catastrophic fines (such as GDPR, HIPAA or the EU AI Act's prohibited and high-risk categories), a tolerable penalty tier where non-compliance is a manageable business cost, and a cautionary or advisory tier with opportunities to correct and minimal penalties — and verticals and workflows in the more stringent tiers can create much deeper moats through specialised solutions. [CLM-0040-013]. — jurisdiction: general [jurisdiction inferred]; basis: argument
- Gridin (2026) argue that The same deterministic architecture that makes AI the most powerful tool for legal transparency is, without procedural constraints, equally capable of becoming an instrument of systematic surveillance and arbitrary control; whether a system functions as a transparency mechanism or a surveillance apparatus is determined not by the technology but by three design choices - a Digital Warrant governing biometric access, an Algorithmic Due Process escalation matrix, and distributed multi-signature governance - so the choice is between constitutional philosophies of governance, not between technologies. [CLM-0049-043]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that The goals that researchers attribute to system-level instructions fall into eight categories of two types: six system goals that target the behaviour of the AI system itself (alignment, accessibility, adaptability, performance, stability, security) and two prompt goals that target the instructions themselves as artefacts (implementation, auditability). [CLM-0050-002]. — jurisdiction: general; basis: literature
- Neumann et al. (2026) argue that Regulators necessarily interpret natural-language prompts through social, legal and institutional understandings of meaning, obligation and intent, which is not comparable to how language models process instruction text through layers of statistical pattern matching shaped by training and sensitive to phrasing and context; linguistic accessibility therefore risks importing human interpretive assumptions into machine governance. [CLM-0050-010]. — jurisdiction: general; basis: argument

### Predictive

**CoE**

- Gridin (2026) argue that The Council of Europe Framework Convention on AI (CETS No. 225) is the most ambitious attempt yet to establish a universal normative floor for AI architectural choices, extending human-rights obligations beyond the EU's boundaries to any state party regardless of its domestic regulatory model; the interaction between the Convention's obligations and the architectural choices of deploying entities will become the defining jurisprudential frontier of the next decade. [CLM-0049-049]. — jurisdiction: CoE; basis: legislation

**general**

- Nay et al. (2023) argue that If LLMs understand the law well enough, they could be deployed by governments, citizens and researchers to identify inconsistencies in existing laws, flag potentially outdated law or areas where the law is silent although guidance exists in similar circumstances, provide clear explanations of complex laws and regulations, and eventually help predict the likely impacts of new laws or policies. [CLM-0024-017]. — jurisdiction: general; basis: argument
- Nay et al. (2023) argue that Extrapolating current capabilities forward, LLMs being able to 'understand' law would affect law-making and necessitate changes to the regulation of legal services and to emerging AI governance regimes. [CLM-0024-019]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Prompt-based governance built on the assumption that prompt text controls behaviour risks creating a false sense of control and a compliance illusion: a system prompt may read as aligned with a governance principle while failing to yield stable behaviour across contexts, models or multi-turn interactions, and actors may satisfy disclosure requirements with carefully drafted prompts even when resulting behaviour is difficult to verify; relying on inspecting and constraining prompt text rather than evidencing behavioural effects risks regulating what is legible rather than what is operational. [CLM-0050-009]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that The ease of prompt intervention may encourage expansion in the scope of prompt-based control: once system-level instructions are treated as a viable control mechanism for one objective, they tend to be adopted for additional objectives, including ones not or only conditionally suited to prompt-based control, so that a prompt-centric governance approach may face function creep without evidence that instructions can reliably deliver each task. [CLM-0050-012]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that The low cost and ease of prompting may make it a default governance intervention even where alternative mechanisms would prove more robust; governance shaped by what is practical to implement within an architecture rather than by what is normatively or empirically justified may introduce a form of technological determinism. [CLM-0050-013]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Because prompt-based effects and controls do not transfer reliably across models, training methods, or deployment contexts, governance mechanisms that rely heavily on text-level prescriptions (guidance on textual content, mandates or prohibitions on certain terms, standardisations) may produce weak or non-functional safeguards unless coupled with robust evaluation requirements. [CLM-0050-014]. — jurisdiction: general; basis: literature
- Neumann et al. (2026) argue that When governance relies on iterative adjustments to prompt text, it risks reproducing a trial-and-error dynamic in governance, with affected communities bearing the costs through shifts in bias and representational harms, prompt failures discovered in production, unannounced behaviour changes, and possible stifling of speech or censorship. [CLM-0050-019]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Because many systems are deployed on global platforms hosting foundation models, system prompt constraints set to satisfy one jurisdiction may be applied across borders by multinational vendors to reduce operational complexity, so that jurisdictions which did not adopt those requirements may nonetheless experience their effects; and if prompt requirements are perceived as functional, other jurisdictions may adopt similar approaches, in a dynamic resembling the Brussels Effect. [CLM-0050-020]. — jurisdiction: general; basis: argument
- Neumann et al. (2026) argue that Governmental actors may use procurement power or regulatory authority as commercial and political leverage to demand that providers remove, weaken, or add safety restrictions encoded in system-level instructions, thereby influencing the normative values encoded into deployed models. [CLM-0050-021]. — jurisdiction: general; basis: argument

## Disagreements

No extracted ATTACKS edge touches a claim on this page.

### Inferred

Tensions judged from content alone, with no citation link (hypotheses about the literature, not facts about it; schema/edges.md).
- The claim that The Human-in-the-Loop paradigm, as mandated by Article 14 of the EU AI Act and widely adopted as the default safeguard in corporate AI governance, is a structural placebo: mandating human oversight in the absence of architectural guardrails does not prevent catastrophic errors but merely redistributes liability onto operators who are cognitively and technically unequipped to intercept them. [CLM-0049-007] is in tension with the claim that Because legal systems are human-centric and human accountability is paramount for trust in a democratically governed society, the vision of AI & Law is one of AI supporting human decision makers rather than replacing or unduly influencing them, and predictive systems should not be directly applied within courts. [CLM-0014-016] (inferred, medium). Note: One treats human oversight of AI as the appropriate vision for legal AI; the other holds that the human-in-the-loop paradigm as a default safeguard is structurally flawed.
- The claim that The Human-in-the-Loop paradigm, as mandated by Article 14 of the EU AI Act and widely adopted as the default safeguard in corporate AI governance, is a structural placebo: mandating human oversight in the absence of architectural guardrails does not prevent catastrophic errors but merely redistributes liability onto operators who are cognitively and technically unequipped to intercept them. [CLM-0049-007] is in tension with the claim that For complex domains like law, LLMs and pre-trained abstractive summarization models are not yet ready for fully automatic deployment; a human-in-the-loop approach in which a legal expert monitors the generated summaries may be more appropriate, and better methods are needed to detect complex errors in abstractive summaries. [CLM-0028-015] (inferred, medium). Note: One prescribes a human in the loop as the remedy for unreliable legal AI; the other holds that this paradigm fails under automation bias.

## Distribution

Sources with claims on this concept: 7; claims: 57.

**By contribution type**

| value | sources |
|---|---|
| theoretical | 5 |
| normative | 4 |
| technical | 4 |
| empirical_qualitative | 3 |
| doctrinal | 2 |
| empirical_quantitative | 2 |
| survey | 1 |

**By source jurisdiction**

| value | sources |
|---|---|
| general | 3 |
| US | 2 |
| CN | 1 |
| CoE | 1 |
| EU | 1 |
| GB | 1 |
| RU | 1 |

**By claim jurisdiction**

| value | sources |
|---|---|
| general | 6 |
| US | 3 |
| EU | 2 |
| GB | 2 |
| AU | 1 |
| BR | 1 |
| CoE | 1 |
| SG | 1 |
| undetermined | 1 |

**By year**

| value | sources |
|---|---|
| 2026 | 4 |
| 2023 | 2 |
| 2024 | 1 |

## What the sources do not address

- No methodological claim on CPT-ai-governance-and-alignment. [ABS-1368] candidate readings: gap_in_literature | extraction_shadow | tacit_link

## Open questions for the hypothesis register

Entries are made at query time (query-graph skill); none recorded for this concept yet.

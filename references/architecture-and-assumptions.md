# Architecture, Decomposition, and Critical Assumptions

Load this reference only when the mission's primary blocker concerns an
architecture question, responsibility boundary, seam, or system-critical
assumption. The dedicated scan remains separately loaded.

## Contents

- [Architecture expression selection](#architecture-expression-selection)
- [Deep-module and seam analysis](#deep-module-and-seam-analysis)
- [Codebase architecture scan](#codebase-architecture-scan)
- [Critical-assumption contract](#critical-assumption-contract)

## Architecture expression selection

**Problem and expected effect.** A reader may need system relationships to make
a decision, implement, validate, review, recover, or maintain work, while an
unnecessary or misleading view can duplicate authority. This method enables the
named next action with the smallest adequate expression.

**Observable applicability.** Use when a named reader and question require
relationships to be expressed and an existing form does not answer them,
across any affected layer. Do not use when current authority or short prose
already answers the question, when only a format preference exists, or for
hypothetical future use.

**Prerequisites, inputs, and resources.** Name the question, reader, next
action, current semantic authorities and expressions, settled and unresolved
relationships, evidence, destination capabilities, and real maintenance or
recovery risk.

**Logic and procedure.** Resolve meaning the expression would otherwise
invent. Reuse an adequate expression. Choose prose for definitions and
boundaries, a table for exact mappings or comparisons, and a diagram only when
nonlinear structure, dependency, change, sequence, runtime, deployment, or
provenance becomes materially clearer. Combine forms only for distinct needed
questions. For a persistent expression, bind its role, sources, scope, limits,
and review trigger. Observe an actually rendered artifact before claiming
rendered delivery.

**Result contract.** Return justified reuse or the minimum expression, the
relationship and question it answers, reader and consumer, authority or
evidence role, scope, supported and unsupported claims, and any review trigger.
The expected outcome is comprehension sufficient for the named next action.

**Failure and honest degradation.** Unresolved meaning, unsupported notation,
or an unavailable rendering environment can make the expression deceptive.
Do not produce every form, satisfy a diagram count, or use polish as evidence.
Degrade to sourced prose or a candidate sketch and state that rendering or the
underlying meaning remains unverified.

**Authority and claim boundary.** AI may select and construct a form inside
settled meaning. A derived expression references authority; it cannot settle
meaning, strengthen evidence, prove implementation, or create
`human_confirmed`.

**Stop, handoff, and re-entry.** Stop when the reader can answer the named
question without guessing and another form would not change the action. Hand
the result to its decision, implementation, validation, review, or recovery
consumer. Re-entry occurs when sources, scope, relationships, rendering, or the
reader's material question changes.

## Deep-module and seam analysis

**Problem and expected effect.** Scattered responsibility, forwarding-only
layers, leaky interfaces, caller knowledge, or internal-test coupling spreads
change and cognitive cost. This method enables a responsibility concentration
behind a narrow interface that earns its seam.

**Observable applicability.** Use when observed L3 friction shows callers know
internal order or state, changes spread across consumers, tests bypass the
caller surface, or a boundary mainly forwards. Do not use when a settled local
detail is being repaired, when no observed friction exists, or when a narrow
stable interface already hides meaningful behavior.

**Prerequisites, inputs, and resources.** Inspect current L0-L2 constraints,
L3 responsibilities, callers, public obligations, invariants, failures,
lifecycle and authority owners, dependencies, change evidence,
implementations, tests, and representative behaviors.

**Logic and procedure.** Trace where knowledge and behavior live. Seek leverage
and locality behind the narrowest stable interface. Place a seam only where
responsibility, lifecycle, authority, failure, change, unstable dependency, or
independent testing genuinely differs. Make call and dependency direction
explicit. Let adapters translate protocols rather than own business truth.
Apply a deletion test: determine whether removing the proposed boundary
concentrates behavior or merely spreads forwarding into callers.

**Result contract.** Return the chosen responsibility, interface obligations,
seam and adapter roles, dependency direction, public behavioral evidence,
rejected shallow splits, exact scope, consumer, expected locality effect, and
unsupported architecture claims.

**Failure and honest degradation.** Hypothetical variation, aesthetic file
size, internal-only tests, or weak deletion evidence can create a shallow
module. Do not invent domain policy or expose internals to make testing easy.
Degrade to a friction map and the smallest caller, history, or behavior
evidence needed to rank a candidate.

**Authority and claim boundary.** AI may recommend L3 responsibility and seams
inside confirmed meaning. It cannot change product, system, operational, or
domain policy, treat internal layout as product truth, or claim architecture
acceptance or `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when callers can use and test the public
interface without hidden coupling and further splitting would add forwarding
or cognitive cost. Hand the bounded design to ordinary planning and TDD.
Re-entry occurs when a consumer contract, dependency direction, owning meaning,
or material friction changes.

## Codebase architecture scan

**Problem and expected effect.** A restructuring decision may lack current,
bounded evidence about architecture friction. This method enables an
evidence-ranked candidate set or a supported no-candidate result without
modifying code or settling a final interface.

**Observable applicability.** Use when the user explicitly requests a
read-only architecture health scan, or current inspection exposes material
cross-file friction before a restructuring decision. Do not use for a known
local bug, routine cleanup, aesthetic restructuring, size or age alone, or an
already governed implementation.

**Prerequisites, inputs, and resources.** Use the requested repository scope,
current project authority, code, representative callers and tests, runtime
facts, user-reported pain, and reliable history when available. Load
[codebase architecture scan](codebase-architecture-scan.md) only when this
positive predicate holds.

**Logic and procedure.** Follow the separately loaded read-only scan: bound
scope, recover current context, inspect observable friction, apply its deletion
test, and rank candidates by evidence. Never modify code, update architecture
authority, approve a candidate, or continue into refactoring inside the scan.

**Result contract.** Return evidence-ranked candidates with exact inspected
scope, observed friction, evidence, deletion-test result, conceptual direction,
benefits, risks, authority conflict, recommendation strength, next evidence,
skipped areas, unknowns, and supported and unsupported claims. A no-candidate
result is valid.

**Failure and honest degradation.** Missing history lowers hotspot confidence;
missing current friction rejects a hotspot. Do not turn counts, age, or
navigation discomfort into findings. When scope outruns evidence, degrade to
the strongest bounded observation and the next smaller inspection.

**Authority and claim boundary.** The scan is generated diagnosis. It does not
settle architecture, authorize modification, prove product quality, or create
`human_confirmed`. The accountable design owner selects whether any candidate
enters a separate design task.

**Stop, handoff, and re-entry.** Stop after the candidate report or supported
no-candidate result. If the user selects a candidate, end the scan and hand off
to a separate design task before implementation. Re-entry occurs only as a new
scan mission with changed scope, evidence, or architecture question.

## Critical-assumption contract

**Problem and expected effect.** An unproven product- or system-critical
capability may support upper-layer meaning or a readiness claim while its
failure would change that meaning. This method enables bounded progress with an
explicit assumption, evidence route, fallback, and reopen boundary.

**Observable applicability.** Use when failure of an unproven capability could
change L0 product position, L1 system responsibility, or a material readiness
claim. Do not use when the unknown is replaceable within settled L3-L4 meaning,
cannot affect an upper-layer decision, or current evidence already settles it.

**Prerequisites, inputs, and resources.** Use current product and system
authority, the assumption and scope, claimed capability, affected consumers,
current evidence, minimum acceptable measures, validation owner, tools or
environments, fallback, and accountable owner.

**Logic and procedure.** State the assumption and upper-layer conclusion it
supports. Identify required system mechanisms, current evidence and limits,
minimum discriminating evidence, validation owner, cheapest disposable
validation, fallback, and conditions that reopen L0 or L1. Hand discovery of a
direction-changing unknown and evidence-route selection to `find-unknown` when
available; consume its bounded observation without copying that workflow.

**Result contract.** Return the critical-assumption contract, scope, supported
and unsupported conclusions, minimum evidence, validation owner, cheapest
validation, fallback, accountable decision, and reopen conditions. The result
supports conditional design progress, not validated feasibility.

**Failure and honest degradation.** Vague measures, ownerless validation,
production-first experiments, or small unrelated samples create false
confidence. Do not treat model-generated or external evidence as proof of this
system. Degrade to the named system impact, current claim ceiling, fallback,
and smallest observation that could change the decision.

**Authority and claim boundary.** ASE owns system impact, fallback, and claim
boundaries; the discovery workflow owns route selection. Accountable product or
system owners retain the upper-layer decision. Evidence cannot prove
acceptance, production feasibility, or create `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when the contract lets bounded design
proceed safely or one owner decision blocks it. Hand validation execution to
the applicable discovery or ordinary workflow. Re-entry occurs when evidence
arrives, the assumption or fallback changes, its invalidation condition fires,
or the result would support a stronger claim.

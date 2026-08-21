# Validation, Quality, Evidence, and Claim Boundaries

Load this reference only when the mission's primary blocker concerns validation
authority, evidence applicability, conflated claim objects, domain quality, or
a delivered result that must be observed.

## Contents

- [Project validation strategy](#project-validation-strategy)
- [Evidence identity and invalidation](#evidence-identity-and-invalidation)
- [Claim-object separation](#claim-object-separation)
- [Domain or subjective quality](#domain-or-subjective-quality)
- [Observed-delivery evidence](#observed-delivery-evidence)

## Project validation strategy

**Problem and expected effect.** A material decision, action, or claim may be
blocked by missing, conflicting, or insufficient validation authority,
responsibility, evidence applicability, or claim-to-evidence mapping. This
method enables the smallest usable execution mapping without redefining the
claim.

**Observable applicability.** Use when the named blocker crosses settled
implementation details and concerns validation meaning or authority owned at
L0-L3 and executed at L4. Do not use when existing authority settles ordinary
verification, a routine test command, a local defect, or an expensive suite by
itself.

**Prerequisites, inputs, and resources.** Inspect the blocked claim and scope,
current normative and validation authorities, accountable owners, contracts,
commands and observations, coverage, environments, cadence, escalation,
evidence handling, representative cases, external dependencies, and current
results.

**Logic and procedure.** Name the claim, owner, environment or population, and
strongest conclusion sought. Inspect only current sources needed for it. Map
commands, scope, coverage, environment, cadence, escalation, evidence, and
human authority; report conflicts. Check applicable critical scenarios,
failure and recovery, dependencies, compatibility, and domain quality.
Classify exactly one disposition: `adequate-existing`, `partial-existing`,
`missing-required`, `not-required`, or `unproven`. For a partial or missing
strategy, derive only the absent execution mapping.

**Result contract.** Return blocked claim, owning authority, inspected authority
set, one disposition, conflicts and gaps, claim-to-evidence execution mapping,
evidence identity, human boundary, supported and unsupported conclusions,
consumer, stop and reopen conditions. The expected outcome is ordinary
verification that can proceed without guessing.

**Failure and honest degradation.** Uninspected authority, missing owner,
unavailable environment, conflicting thresholds, or unsuitable evidence cannot
support a strategy. Do not assign authority through file creation or a
conventional filename. Return `unproven` or a non-authoritative candidate with
the smallest next evidence; never lower an accepted evidence requirement to
fit available checks.

**Authority and claim boundary.** The current project authority owns claims,
thresholds, representativeness, responsibility, design, confirmation, and
acceptance. AI maps but cannot redefine them, create a sixth layer, prove
release, or create `human_confirmed`. Ordinary workflows run checks.

**Stop, handoff, and re-entry.** Stop when current authority or the bounded
candidate lets the next ordinary action proceed. Hand test execution, CI,
package, release, and acceptance actions to their owners. Re-entry occurs when
claim scope, authority, threshold, environment, evidence applicability, or
accountable ownership changes.

## Evidence identity and invalidation

**Problem and expected effect.** Evidence reused, aggregated, or compared
without identity and freshness can support a materially wrong claim. This
method enables a bounded claim to cite evidence whose applicability and reopen
conditions are explicit.

**Observable applicability.** Use when evidence will support, compare, or roll
up into a material claim and any source, input, configuration, tool, provider,
environment, population, or freshness difference could matter. Do not use when
no evidence-backed claim is made or identity is already complete and valid for
the exact scope. The typical affected layer is L4 evidence serving the exact
claim owned at L0-L3. This layer coordinate is not a fixed workflow; activate
only affected layers.

**Prerequisites, inputs, and resources.** Gather source revision, relevant
inputs and data population, configuration, commands or observations, tools and
providers, versions, environment, time, result, claim scope, current authority,
known invalidators, consumers, and evidence owner.

**Logic and procedure.** Bind the evidence to its source and execution identity.
State what was observed, where, against which inputs and configuration, with
which tools or providers, and when. Map it to the exact claim and consumer.
Identify changes that make it stale or incomparable. Before reuse or
aggregation, recheck every material identity field and preserve partial or
conflicting results instead of averaging away differences.

**Result contract.** Return an evidence record with identity, observed result,
scope, claim mapping, applicability, freshness, owner, supported and unsupported
conclusions, invalidation and reopen conditions, and the expected effect on the
named claim.

**Failure and honest degradation.** Missing revision, inputs, configuration,
provider, environment, population, raw result, or invalidation conditions can
make reuse unsafe. Do not simulate missing observation or infer broad
representativeness from a small sample. Degrade the claim ceiling and name the
smallest rerun or identity field that could restore applicability.

**Authority and claim boundary.** AI may record, compare, and qualify evidence.
The claim owner sets meaning and minimum evidence. Evidence supports only its
observed object and population; it cannot prove a broader outcome, acceptance,
release, or create `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when the evidence is either applicable to
the named claim or explicitly bounded as insufficient. Hand reruns and
observations to the ordinary validation workflow. Re-entry occurs when any
identity field, claim, authority, population, freshness rule, or invalidation
condition changes.

## Claim-object separation

**Problem and expected effect.** Source, package, installation, runtime,
publication, release, product outcome, and human acceptance are often
conflated, allowing weaker evidence to support a stronger object. This method
enables only the strongest object actually evidenced and authorized.

**Observable applicability.** Use when one of those objects is claimed,
compared, handed off, or at risk of being promoted into another. Do not use
when only one already evidenced object is involved and no broader inference or
authority boundary exists. The typical affected layer is L4 facts mapped to the
applicable claim owner at L0-L3. This layer coordinate is not a fixed workflow;
activate only affected layers.

**Prerequisites, inputs, and resources.** Use exact source identity, package
manifest, target installation and runtime environment, publication state,
release record, product-outcome evidence, acceptance authority, requested
claim, current results, permissions, and invalidation conditions.

**Logic and procedure.** List each requested object separately. For source,
inspect source evidence; for a package, verify the exact manifest and
self-containment; for installation, inspect the real target; for runtime,
exercise the relevant environment; for publication and release, observe their
actual external states; for product outcome and human acceptance, require their
own evidence and authority. Stop promotion at the first unsupported object.

**Result contract.** Return every requested claim object, corresponding
evidence and environment, authority, result, supported and unsupported status,
consumer, residual uncertainty, invalidation, and the expected strongest
bounded conclusion.

**Failure and honest degradation.** Source tests do not prove a package,
package structure does not prove installation or runtime, and generated reports
do not prove publication, release, product outcome, or acceptance. Do not
describe planned operations as observed. Degrade to the strongest exercised
object and name the smallest real-environment observation or authorization
needed next.

**Authority and claim boundary.** AI may inspect and distinguish objects.
Publication, release, product-outcome, and acceptance authority remain with
their accountable owners. Source or generated evidence cannot prove another
object or create `human_confirmed`.

**Stop, handoff, and re-entry.** Stop at the strongest requested object actually
supported. Hand package copying, installation, publication, release execution,
and acceptance to their ordinary tools and owners. Re-entry occurs only for a
new claim object, invalid evidence, changed environment, or disputed claim
boundary.

## Domain or subjective quality

**Problem and expected effect.** Structural checks, self-critique, model
agreement, or weak reference metrics can look complete while real artifacts
remain poor or domain-wrong. This method enables a bounded quality conclusion
based on representative artifacts and credible judgment.

**Observable applicability.** Use when subjective artifact quality, expert
domain meaning, or misleading structural or model metrics materially affects a
claim, normally at L2-L4. Do not use when objective settled checks fully decide
the bounded claim and no qualified judgment is required.

**Prerequisites, inputs, and resources.** Use real delivered artifacts,
representative cases and failures, current quality meaning and thresholds,
qualified reviewers, an independent critic, credible external or predecessor
reference floors, applicable environment, consumers, and known uncertainty.

**Logic and procedure.** Separate generator from critic. Inspect real artifacts
in the form consumers receive. Sample representative success, edge, and failure
cases. Compare against credible reference floors rather than generated
consensus. Route qualified subjective judgment to the accountable reviewer.
Distinguish a one-off runtime repair from evidence of durable system learning.

**Result contract.** Return inspected artifacts and cases, criteria and sources,
independent findings, reference comparison, qualified-human boundary,
actionable failures, supported and unsupported quality claims, residual
uncertainty, consumer, and expected quality conclusion.

**Failure and honest degradation.** Synthetic examples, self-scoring,
unqualified review, hidden artifacts, biased samples, or arbitrary scores
cannot support domain quality. Do not turn model agreement into expert or human
acceptance. Degrade to observed defects and limits plus the smallest real
artifact, representative case, or qualified review needed.

**Authority and claim boundary.** AI may generate and critique but cannot
manufacture domain authority. Qualified human judgment remains distinct from
generated findings. Neither structural completeness nor critic agreement can
prove product acceptance or create `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when the requested quality claim has the
required real-artifact, representative-case, reference-floor, and qualified
review evidence, or state why it remains unsupported. Hand remediation to the
ordinary workflow. Re-entry occurs when criteria, artifacts, population,
reviewer qualification, or evidence freshness changes.

## Observed-delivery evidence

**Problem and expected effect.** Constructed source can be mistaken for a
rendered, installed, runtime, migration, operational, or real-environment
result. This method enables a delivered-object claim only after observation in
the applicable environment.

**Observable applicability.** Use when the requested claim concerns an actual
rendered result, installed or runtime behavior, migration outcome, operation,
external provider, hardware, or other real environment. Do not use when the
claim is explicitly limited to source construction or another already observed
lower-scope object. The typical affected layer is L4 observation serving the
applicable claim owner at L0-L3. This layer coordinate is not a fixed workflow;
activate only affected layers.

**Prerequisites, inputs, and resources.** Use exact source and delivered
artifact identities, applicable environment and configuration, real inputs,
provider or hardware state, observation tools, success and failure criteria,
runtime or operational owner, consumers, and claim-specific authority.

**Logic and procedure.** ASE defines the observation contract: exact object,
environment, inputs, criteria, observation boundary, identity, and result to
return. The owning ordinary workflow delivers, executes, installs, migrates, or
operates the object in the applicable environment. ASE consumes the actual
result and may perform only authorized read-only observation of already
delivered state. Record identity, environment, inputs, configuration, result,
and invalidation. Compare only with the claim's current criteria and separate
delivery observation from release or acceptance.

**Result contract.** Return the delivered object and environment identity,
observations, criteria, success and failure results, supported delivery claim,
unsupported broader claims, consumer, residual risks, freshness, invalidation,
and expected bounded conclusion.

**Failure and honest degradation.** Unavailable environments, screenshots of
source, simulated providers, expected rendering, or described runtime behavior
do not constitute observation. Do not claim delivery merely because source is
renderable or executable. Degrade to a source-construction claim and name the
smallest applicable environment observation still required.

**Authority and claim boundary.** ASE defines and consumes the observation
contract; it does not own delivery, execution, installation, migration, or
operation. Its direct access is limited to authorized read-only observation.
Construction proves only construction; environment evidence proves only its
observed scope. Release, product outcome, qualified acceptance, and
`human_confirmed` remain separately owned and cannot be inferred.

**Stop, handoff, and re-entry.** Stop when the requested delivered-object claim
is observed and bounded, or when unavailable observation fixes a lower claim
ceiling. Hand delivery, execution, installation, migration, rollout,
operations, publication, release, and acceptance to their owning ordinary
workflows or accountable owners. Re-entry occurs when the environment,
artifact, inputs, configuration, criteria, observation freshness, or requested
claim changes.

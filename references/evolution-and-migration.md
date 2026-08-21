# Evolution, Refactoring, Migration, and Compatibility

Load this reference only when the mission's primary blocker concerns behavior
preservation, predecessor meaning, coexistence, convergence, compatibility, or
irreversible retirement.

## Contents

- [Characterization-first behavior change](#characterization-first-behavior-change)
- [Predecessor semantic inventory and consumer trace](#predecessor-semantic-inventory-and-consumer-trace)
- [Additive migration and convergence](#additive-migration-and-convergence)
- [Irreversible retirement](#irreversible-retirement)

## Characterization-first behavior change

**Problem and expected effect.** A refactor, migration, or fix can silently
change behavior on which an observed consumer depends. This method enables a
bounded change with the relevant current contract preserved or an intentional
semantic change routed to its owner.

**Observable applicability.** Use when a named consumer, public behavior,
failure mode, or compatibility path could change across L2-L4. Do not use when
a private repair has a settled contract and no consumer or compatibility
uncertainty, or when ordinary debugging already has a bounded reproduction.

**Prerequisites, inputs, and resources.** Inspect observed public behavior,
consumers, current specifications and authority, realistic examples, tests,
runtime facts, failure behavior, intended change, and available environments.

**Logic and procedure.** Trace the consumer-facing behavior before changing
internals. Capture a realistic characterization that can distinguish preserved
from changed behavior, including applicable failure paths. Compare observation
with current authority; treat a mismatch as a decision boundary rather than
choosing silently. Once meaning is settled, hand the bounded behavior and
characterization to ordinary TDD and implementation.

**Result contract.** Return the observed contract, consumers, authoritative or
pending differences, realistic characterization, intended change boundary,
scope, supported and unsupported behavior claims, and expected preservation
effect.

**Failure and honest degradation.** Legacy behavior may be accidental,
environment-specific, stale, or poorly observed. Do not freeze internals or
promote observation to product truth. With missing evidence, degrade to a
consumer and uncertainty map plus the smallest realistic observation needed
before implementation.

**Authority and claim boundary.** Observed behavior is evidence. Accepted
specification or an accountable owner governs intentional semantic change.
ASE does not execute TDD, and passing characterization checks cannot prove
product acceptance or create `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when the named consumer contract is
explicit and preserved or the owner has bounded its change. Hand coding and
TDD to the ordinary workflow. Re-entry occurs when implementation exposes an
uncharacterized consumer, contradictory authority, compatibility consequence,
or invalid evidence.

## Predecessor semantic inventory and consumer trace

**Problem and expected effect.** Comparing old and target systems by file shape
can lose meaning, hidden consumers, or compatibility obligations. This method
enables every in-scope behavior and consumer to receive a supported retention,
transformation, replacement, or retirement disposition.

**Observable applicability.** Use when a predecessor, incomplete
specification, hidden consumer, or compatibility path can affect a replacement
or migration decision across L1-L4. Do not use when no predecessor meaning or
consumer can affect the bounded change.

**Prerequisites, inputs, and resources.** Use current and predecessor semantic
authorities, code and runtime evidence, behavior inventory, consumers and
integrations, target contracts, environments, history, compatibility owner,
recovery options, and evidence freshness.

**Logic and procedure.** Inventory meaning rather than files. For every
in-scope behavior, contract, data meaning, authority, and consumer, compare old
and target semantics and assign `retained`, `transformed`, `replaced`, or
`retired` with evidence. Trace affected consumers, move canonical ownership
deliberately, name compatibility's consumer and exit, and verify replacement
before retirement.

**Result contract.** Return the semantic inventory, consumer trace,
dispositions and bases, current and target authority, compatibility scope,
gaps, residual risk, supported and unsupported convergence claims, and the
expected effect on the named migration decision.

**Failure and honest degradation.** Hidden consumers, missing environments,
stale predecessor evidence, or an incomplete target contract can make a final
disposition unsafe. Do not use predecessor behavior as an oracle or infer
retirement from target-only tests. Degrade to provisional dispositions and the
smallest consumer or environment evidence needed.

**Authority and claim boundary.** AI may inventory, trace, compare, and propose
dispositions. Accountable owners govern changed meaning, compatibility, and
retirement. Predecessor evidence proves only its observed scope and cannot
create acceptance or `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when every in-scope semantic and consumer
has a supported or explicitly provisional disposition. Hand bounded migration
work to the ordinary workflow; use Irreversible retirement before destructive
execution. Re-entry occurs when a consumer, target contract, authority,
environment, or replacement evidence changes.

## Additive migration and convergence

**Problem and expected effect.** Old and new states may need to coexist while
transition is partial, consumer contracts change, or rollback and an
irreversible point matter. This method enables a recoverable migration with an
explicit compatibility owner and convergence exit.

**Observable applicability.** Use when coexistence, partial transition,
consumer compatibility, repair, rollback, or an irreversible point is
observable across L2-L4. Do not use when replacement is atomic, fully
reversible, and has no consumer or compatibility consequence.

**Prerequisites, inputs, and resources.** Inspect current and target contracts,
old and new states, consumer inventory, data or protocol ownership, transition
mechanism, compatibility owner, environments, migration evidence, repair and
rollback capabilities, monitoring, and accountable decisions.

**Logic and procedure.** Define supported old, mixed, and new states. Prefer an
additive path that preserves valid consumers while target capability becomes
observable. Assign compatibility ownership and its explicit removal condition.
Specify partial-transition detection, repair, retry, rollback or containment,
the irreversible point, and how convergence is proven. Sequence work without
claiming atomicity across independently evidenced objects.

**Result contract.** Return the migration states and transitions, consumer and
compatibility contracts, owner, partial-state behavior, repair, rollback,
irreversible point, convergence and exit evidence, unsupported claims,
residual risks, and expected migration outcome.

**Failure and honest degradation.** A big-bang rewrite, ownerless compatibility,
untestable mixed state, repeated unknown-outcome operation, or target-only
evidence can strand consumers. Do not hide partial completion. Degrade to a
read-only transition model, explicit blockers, preserved completed evidence,
and the smallest safe next migration observation.

**Authority and claim boundary.** AI may design coexistence, repair, rollback,
and exit criteria. Accountable owners retain compatibility acceptance and the
irreversible decision. Partial evidence supports only partial-transition
claims and cannot prove convergence, release, or `human_confirmed`.

**Stop, handoff, and re-entry.** Stop when ordinary implementation has bounded
states, responsibilities, evidence, and recovery targets, or before an
unsupported irreversible point. Hand execution to the migration and coding
workflow. Re-entry occurs when a partial state is unhandled, rollback fails,
consumer scope changes, convergence evidence is invalidated, or retirement is
requested.

## Irreversible retirement

**Problem and expected effect.** Deletion, retirement, destructive migration,
loss of recovery, or movement of authority can be difficult or costly to
reverse and may leave partial results. This method enables a precisely
authorized, recoverable, per-object retirement claim.

**Observable applicability.** Use when an action destroys or moves material
content, history, authority, compatibility, or recovery and execution intent
exists or is being prepared. Do not use for low-risk reversible organization or
read-only candidate identification without execution intent. Typical affected
layers are L1-L4: system authority and boundary, operational and compatibility
decisions, technical execution design, and per-object observed evidence. This
layer coordinate is not a fixed workflow; activate only affected layers.

**Prerequisites, inputs, and resources.** Require the bounded scope and intent,
current authority, replacement evidence, semantic and consumer inventory,
reference rules, compatibility disposition, recovery boundary, governed
execution capability, durable per-object evidence location, residual risks,
and accountable owner.

**Logic and procedure.** Scale preparation to irreversibility and object count.
Preflight the complete scope read-only for replacement, semantic and consumer
dispositions, cross-object conflicts, current dependencies, recovery, evidence
location, capability, and pending decisions. State that preflight does not
authorize execution. After explicit intent and accountable confirmation, hand
each object independently to the governed executor. Preserve completed,
failed, unstarted, and unknown outcomes distinctly; prove non-completion before
retry and reconcile unknown state without re-execution.

**Result contract.** Return read-only candidates or supported preparation,
scope and intent, replacement and dispositions, recovery, decision state,
per-object completed, failed, unstarted, or unknown evidence, unresolved
conditions, governance closeout status, supported and unsupported retirement
claims, and expected effect.

**Failure and honest degradation.** Passing tests, no observed consumer, a
finished plan, or successful preflight does not prove safe retirement or
execution authority. Never bypass the required capability, rewrite historical
evidence, assume rollback or batch atomicity, or repeat an unknown operation.
Degrade to read-only preparation and the missing prerequisite or reconciliation
step; make no destructive change.

**Authority and claim boundary.** Only the accountable owner authorizes the
irreversible step and material scope changes. The governed executor owns its
operation and evidence; ASE owns system meaning and claim boundaries. Generated
evidence cannot substitute for confirmation or create `human_confirmed`.

**Stop, handoff, and re-entry.** Stop before execution unless intent,
replacement, semantic and consumer disposition, recovery, capability,
per-object evidence, and accountable confirmation support the exact scope.
Hand authorized operations to the governed executor. Re-entry occurs for an
unknown result, failed object, changed authority or consumer, invalid recovery,
or open governance closeout; resume only failed or unstarted scope.

# AI Coding Delivery

Use this reference only when the delivery-scope trigger in `SKILL.md` applies.
`SKILL.md` remains the sole semantic authority. This reference expands
execution; it does not create another layer, lifecycle, confirmation, project
artifact, or completion state.

## Applicability

Use for a material version or end-to-end delivery scope whose decomposition,
dependency order, evidence aggregation, agent ownership, or closure claim
could otherwise cross an unresolved L0-L4 boundary. Do not use merely because
AI writes code, several files change, a sprint exists, or a routine local task
needs ordinary tests.

Start with the named system boundary and blocker required by the core
applicability gate. Stop using this method once still-valid meaning supports a
bounded implementation handoff; return only on a core re-entry condition.

## Inputs and resources

Use only current sources for the affected scope:

- still-valid L0-L2 meaning and confirmation status;
- candidate or confirmed L3 responsibilities, interfaces, data, dependencies,
  failure mechanisms, and quality constraints;
- the named version objective and included or excluded outcomes;
- existing slices, work results, evidence, and invalidation conditions;
- delivery environment, repository and integration facts, and observable risk
  predicates;
- accountable owners and preconfirmed selection or escalation policies.

Missing upper-layer meaning is not an invitation to infer it from code or a
backlog. Reopen its owner or return one bounded human decision.

## Select a vertical delivery slice

### Establish the selection envelope

Derive the envelope from current L0-L2 authority: actor or system participant,
trigger, observable outcome, state and authority changes, success, failure,
recovery, red lines, and excluded outcomes. A slice must remain inside that
envelope or reopen its owning layer.

### Generate a small candidate set

Generate only enough candidates to expose the real choice. Prefer candidates
that represent one of these useful directions when applicable:

- the smallest independent outcome with current value;
- a walking skeleton through the real integration and evidence path;
- the cheapest result that retires the largest named dependency or feasibility
  risk;
- the smallest prerequisite outcome that unblocks several confirmed slices.

Do not slice only by frontend, backend, database, component, repository, or
agent assignment. Those may become work units inside a slice.

### Evaluate candidates

For each candidate, return:

- actor, trigger, outcome, and excluded outcome;
- source L0-L2 meaning and any unresolved authority;
- involved L3 responsibilities, interfaces, data, and dependencies;
- independent acceptance and observable evidence;
- success, failure, recovery, and rollback or containment where applicable;
- value or learning contribution, implementation size, reversibility, and
  integration risk;
- the first condition that would reopen or split it.

Reject a candidate that has no independently observable outcome, cannot be
accepted without an unmade policy decision, depends on broad unfinished
horizontal work, or is too large to integrate and learn from as one bounded
result. Thin the operational scenario or outcome; do not preserve the label
while silently turning it into a multi-feature release.

### Route selection authority

If every core auto-selection condition is satisfied, record the policy,
candidate comparison, selection, and invalidation condition, then proceed.
Otherwise give the accountable human a small candidate set, the material
tradeoff, and one recommendation. Use the existing confirmation band; do not
invent per-slice approval rounds.

## Form the slice contract

Return the smallest semantic contract that the next action needs:

- slice identity and containing version scope;
- actor or system participant, trigger, outcome, and non-goals;
- L0-L2 authority sources and confirmation coverage;
- L3 responsibilities, public seams, data movement, dependency order, and
  failure mechanisms;
- acceptance, integration, operational, and risk-specific evidence required;
- work already reusable and work invalidated;
- accountable owner, AI selection authority if any, and pending decision;
- stop, failure, rollback or containment, and reopen conditions.

This contract need not be a persistent file. Reuse an adequate current work
item or authority-constrained view when it preserves these semantics.

## Check L3 implementation sufficiency

Before dependent work begins, apply the core L3-to-L4 check to the slice. Block
only the dependent branch when component responsibility, interface obligation,
data ownership, dependency order, failure behavior, acceptance, or evidence
cannot be implemented without guessing. Independent settled work may continue.

If the design makes the slice too large, first try to thin its scenario while
preserving an end-to-end outcome. Split it only when each result has independent
acceptance and the ordering dependency is explicit.

## Hand off AI work units

Create the smallest work unit worth an independent test-and-review cycle. Each
handoff contains:

- objective and parent slice;
- authority and design sources;
- allowed files, modules, services, interfaces, or data scope;
- explicit non-goals and protected scope;
- inputs, dependencies, and expected integration consumer;
- acceptance and commands or observations required for evidence;
- stop condition, escalation condition, and owning layer to reopen;
- result fields for implemented scope, evidence, deviation, failure, residual
  risk, and invalidation.

A work unit may be technically horizontal when that is the smallest safe
execution boundary. It does not inherit authority to redefine the parent slice
or claim its completion.

## Execute and integrate

- Keep batches independently reviewable, testable, and integrable; split a
  generated change that hides several acceptance or rollback decisions.
- Integrate as soon as a bounded unit has its required evidence. Do not use a
  long-lived branch or accumulated diff as evidence of progress.
- Assign one active write owner to overlapping code, public interfaces,
  schemas, migrations, or data contracts. Sequence dependent writers from the
  settled result.
- Parallelize only units whose dependencies and write scopes are independent.
  Record the integration consumer and shared acceptance check.
- If implementation exposes a material contradiction, stop the affected unit,
  preserve valid evidence, and reopen the smallest owning layer. Do not patch a
  lower layer to conceal an upper-layer conflict.

Tooling may enforce these rules, but the method does not require a particular
branch platform, task system, CI provider, or agent orchestrator.

## Aggregate verification

### Work-unit evidence

Use the checks applicable to the bounded implementation: characterization,
unit, static, local integration, or other direct evidence. Record environment,
result, deviation, and invalidation. Passing work-unit checks proves only that
unit's supported claim.

### Slice evidence

After integration, verify the operational scenario and its contracts across
the real affected seams. Include applicable success, failure, recovery,
compatibility, and observability evidence. A missing required path keeps the
slice open even when every contributing unit passed locally.

### Version evidence

For the named version scope, aggregate reused and changed slices, run affected
cross-slice regression and architecture or dependency checks, verify required
operational evidence, then run the core L0-to-L4 end-to-end check. Preserve a
valid completed slice when another fails, but do not promote partial closure to
version completion.

Automated checks and AI review generate evidence only. They cannot create
product acceptance, `human_confirmed`, release approval, or system completion.

## Risk-triggered controls

Apply only the branch whose predicate is observed:

- **Security and supply chain:** When authentication, authorization, personal
  or secret data, or an external dependency is affected, verify the applicable
  trust, dependency authenticity and version, exposure, failure, and human
  review boundary.
- **Migration and compatibility:** When persisted data, a public contract, or
  a protocol changes, define supported old and new states, partial transition,
  consumer compatibility, repair, rollback, and the irreversible point.
- **Runtime feedback:** When the claim includes production or operational
  behavior, require the applicable environment, rollout containment,
  monitoring, failure signal, recovery, and feedback-triggered reopen rule.

Absence of the required environment or tool lowers the claim ceiling. It does
not justify simulated evidence or a universal gate for unrelated work.

## Failure and unsuitable cases

Do not use this method to:

- create a slice for a settled private repair or refactor;
- force every iteration through L0-L4;
- turn all technical prerequisites into business-value slices;
- use task completion, code volume, tests, or agent agreement as acceptance;
- serialize independent work or require heavy release controls without a named
  risk;
- keep ASE active throughout ordinary implementation after a bounded handoff.

## Return and stop

Return the containing version scope, selected slice and authority route, active
and reused layers, work-unit handoffs, dependency and write ownership, evidence
at each supported scope, unsupported claims, and reopen conditions.

Stop when the next ordinary coding action can proceed without guessing and has
a bounded evidence target. For closure, stop at the strongest supported
work-unit, slice, or version claim. If a human-owned selection, confirmation,
irreversible consequence, or missing evidence blocks the claim, preserve valid
partial results and return that one blocker; do not manufacture completion.

# Codebase Architecture Scan

Read this reference only after the Codebase architecture scan method in
`architecture-and-assumptions.md` matches the mission. `SKILL.md` remains the
sole cross-cutting semantic authority. This method is a read-only diagnosis
that returns evidence-ranked candidates; it is not a design or refactoring
task.

## Applicability and boundary

Use this method for an intervention mission when the user requests an
architecture health scan, a search for deep or shallow module opportunities,
seam improvement, architecture hotspot analysis, or evidence-ranked candidates
before a restructuring decision.

It may also apply when current inspection exposes material cross-file
friction: behavior repeatedly changes across callers, understanding one
responsibility requires avoidable navigation, a layer only forwards, callers
know internal state or ordering, tests bypass the caller interface, or the same
responsibility boundary repeatedly confuses maintainers or agents.

Exclude a simple bug with a known local contract, formatting, naming,
mechanical local refactoring, an already governed implementation, size or age
alone, routine cleanup, and aesthetic restructuring without observable
friction. Do not make this a periodic practice or an automatic development
prerequisite.

Keep the result within the user's requested repository and authority scope.
Read and report evidence; make no production, architecture-authority, or
release change.

## Bound scope

1. Start with the user's named module, subsystem, path, pain point, or change
   direction. Inspect only adjacent evidence needed to understand that scope.
2. If the user supplied no scope and useful history exists, state the history
   window and use repeated files or co-change areas as hotspots that prioritize
   inspection.
3. If hotspots are scattered, widen one justified step at a time and retain
   explicit skipped areas. Never default to an exhaustive repository
   inventory.
4. If reliable history is unavailable, continue from current structure,
   callers, tests, runtime facts, and user-reported pain. State that hotspot
   priority is unsupported and list the skipped historical evidence.

A hotspot identifies where to look, not what is wrong. Commit count, file
count, module count, size, and age do not prove architecture friction.

## Recover current context

Within the bounded scope, locate project-designated domain language,
architecture decisions, public contracts, representative callers, tests,
runtime evidence, and relevant history. Discover these through project rules
and current links rather than assuming document paths.

Keep evidence roles distinct:

- User-provided facts can support a bounded finding when they are attributed
  and their limits remain explicit. When direct inspection was unavailable,
  say so without discarding evidence already supplied by the user.
- project authorities establish accepted intent and ownership for their
  declared scope;
- code and runtime observations establish current implementation facts;
- callers and tests expose the interface people and systems actually depend
  on; and
- history supports inspection priority and recurring-change observations.

Report a conflict between intent and implementation instead of silently
choosing one. Do not re-open an accepted decision for a theoretical
improvement. Surface a conflicting candidate only when current, reproducible
friction makes reconsideration proportionate.

## Inspect architecture friction

Apply the existing L3 deep-module and seam meanings. Use module, interface,
seam, adapter, depth, locality, leverage, and test surface consistently; do not
create another architecture vocabulary.

Follow evidence while asking:

- Is one responsibility's behavior or knowledge scattered across callers?
- Is the interface nearly as complicated as the implementation?
- Does a layer mainly forward arguments, rename concepts, or add test mocks?
- Must callers know internal sequence, configuration, state, or error details?
- Does a seam leak facts that should stay behind its interface?
- Does a small change spread knowledge, edits, failures, or verification across
  callers?
- Is behavior duplicated in callers or verified only by penetrating internals?
- Did extraction make isolated functions easier to test while making their
  real composition harder to verify?

Also seek preservation evidence. Keep a small module when independent
responsibility, authority, lifecycle, failure isolation, change reason, an
unstable dependency, or two real adapters earn its seam. Do not manufacture a
candidate when a narrow stable interface already hides meaningful behavior
and callers and tests use the same surface.

## Apply the deletion test

For every suspected shallow or pass-through module, answer:

1. Where would its knowledge, decisions, and behavior go if it were removed?
2. Would complexity disappear, concentrate under an existing responsibility,
   or spread into callers?
3. Does the current module already provide locality or leverage?
4. What observed responsibility, authority, lifecycle, failure, dependency,
   or change boundary would own any proposed concentration?
5. Which tests would remain at the caller interface, and which tests reveal a
   misplaced seam?

If these questions cannot be answered from current evidence, limit the
recommendation to `Speculative`. Deletion is a reasoning probe, not permission
to remove code.

## Candidate contract

Return each candidate with these fields:

- **Exact scope:** Files, modules, and representative callers actually
  inspected.
- **Observed friction:** Concrete behavior or change cost, not a cleanliness
  judgment.
- **Evidence:** Code, contract, caller, test, runtime, authority, or history
  observations with their limits.
- **Architecture judgment:** The shallow interface, pass-through behavior,
  leaky seam, low locality, duplicated knowledge, or wrong test surface
  supported by that evidence.
- **Deletion-test result:** Where complexity goes and whether the current
  module is earning locality or leverage.
- **Conceptual direction:** A possible responsibility concentration without a
  final interface or implementation plan.
- **Benefits:** Expected locality, leverage, testability, or AI-navigability
  improvement.
- **Costs and risks:** Migration, compatibility, boundary loss, uncertainty,
  and evidence that could disconfirm the direction.
- **Authority conflict:** The applicable current decision or owner conflict,
  or an explicit none observed within scope.
- **Recommendation strength:** `Strong`, `Worth exploring`, or `Speculative`.
- **Next evidence:** The smallest inspection or validation that could change
  confidence.

Use recommendation strength as a presentation of evidence quality, never as a
second project status:

- `Strong` requires converging current evidence, material friction, and a
  supported deletion-test result.
- `Worth exploring` requires material friction but retains a design-changing
  unknown.
- `Speculative` identifies a plausible direction without enough current
  evidence or deletion-test support for action.

A correct scan may return no candidate. Preserve evidence-backed boundaries
and say that no issue worth escalation was found within the inspected scope.

Finish the result with:

- **Top recommendation:** One candidate and its evidence-based ranking reason,
  or none.
- **Skipped areas:** Uninspected repository or evidence scope.
- **Unknowns:** Unresolved facts that could change a judgment.
- **Supported claims:** What the inspected evidence establishes.
- **Unsupported claims:** What the evidence cannot establish.
- **Next task:** Stop, request the smallest missing evidence, or start a
  separate design task only after the user selects a candidate.

## Report and persistence

Default to a structured conversational result without creating a file. Create
a persistent report only when the user requests it or durable comparison,
decision, review, or handoff value justifies it. Follow the project's existing
documentation and authority rules; do not create a competing status ledger.
The report is generated evidence, not an architecture decision, specification,
acceptance, installation, or release claim.

Add a visualization only when a dependency, call, ownership, or test
relationship becomes materially clearer. Keep any temporary visual
self-contained, offline-capable, outside the repository, and
non-authoritative. A Markdown report without a diagram is the normal result.

## Stop and hand off

Stop after the candidate report or the no-supported-candidate result.

- Do not modify production code.
- Do not settle a final interface.
- Do not update project authority.
- Do not approve or implement a candidate.

When the user selects a candidate, end this diagnosis and hand off to a
separate design task. In the first continuation response, state that the scan
has ended and the design task has begun before asking design questions.
Re-establish the selected goal and scope, current L3 responsibility and
authority, alternatives when risk warrants, migration and compatibility,
recovery and stopping, test surface and realistic evidence, and human decision
boundaries before implementation.

## Failure and honest degradation

- Without reliable history, use current evidence and mark hotspot priority
  unsupported.
- Without a project-designated authority, do not invent one; report the gap
  only when it limits a candidate.
- When a hotspot lacks current code, caller, test, contract, or runtime
  friction, reject it as a candidate.
- When an accepted decision lacks reproducible friction, keep it closed.
- When scope outgrows defensible evidence, return the strongest bounded result,
  skipped areas, and the next smaller inspection.
- If the scan begins designing an interface, changing authority, modifying
  code, or continuing into a refactor, stop at the last supported read-only
  finding and restore the separate-task boundary.

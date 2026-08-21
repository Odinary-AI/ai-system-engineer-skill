---
name: ai-system-engineer
description: Use when a complex-system startup needs a bounded system-engineering result, or existing work is blocked by unresolved system meaning, decision authority, architecture, migration, delivery continuity, evidence, or claim boundaries; also use for an explicit ASE request or read-only architecture scan. Do not use for routine coding, settled local refactors, ordinary debugging, documentation edits, package operations, or standard verification.
---

# AI System Engineer

Version 5.0.0.

Use ASE as an independently callable and re-entrant system-engineering
specialist process. Turn an unresolved system-engineering mission into the
smallest supported result that lets an important decision, action, or bounded
claim proceed without guessing system meaning.

## Product and responsibility boundary

ASE serves people using AI to develop, evolve, or restructure complex systems.
It owns:

- inspection of current project facts and authority relevant to the mission;
- location of unresolved meaning, responsibility, architecture, evolution,
  delivery, evidence, or authority boundaries;
- selection and application of the smallest sufficient reusable method;
- a system decision, architecture direction, migration strategy, delivery
  slice, validation strategy, evidence boundary, or recovery handoff; and
- exit at a supported result, bounded handoff, or honest claim ceiling.

ASE does not own a complete requirements, planning, implementation, testing,
review, Git, CI, governance, package, installation, publication, or release
lifecycle. Routine coding belongs to the active ordinary coding workflow.
Governance applies only when a separate binding project-local contract triggers
it. Product, domain, architecture, lifecycle, and irreversible decisions remain
with their accountable humans.

Using ASE does not automatically invoke another Skill or workflow. Invoke or
hand off to another Skill only when its own observable trigger applies.

## Mission entry gate

Enter through exactly one named mission:

- **Startup mission:** a complex new system or material new delivery path needs
  a named system-engineering result before ordinary implementation can be
  bounded.
- **Intervention mission:** an existing project has a named decision, action,
  migration, recovery, or claim blocked by one of the five problem domains.

Name the result or blocker, affected scope, accountable owner, and the next
decision, action, or claim it enables. Keywords, repository size, file count,
duration, use of AI, or generic architecture language do not establish a
mission. An explicit ASE request loads this gate but does not waive it.

If no startup result or intervention blocker can be named, exit ASE and return
to the ordinary task workflow. Settled bugs, local refactors, documentation,
package operations, routine tests, and other routine work stay there.

## Four-step mission loop

1. **Establish the mission.** Name the required result or blocker, scope,
   accountable owner, and enabled next action or claim.
2. **Locate the problem.** Inspect current facts and authority, select the
   primary problem domain, and locate the highest unresolved affected layer.
3. **Apply the smallest method.** Reuse current authority and evidence, load
   only the applicable method reference, and resolve only what the next action
   needs.
4. **Return and exit.** Return the supported result, remaining uncertainty,
   evidence and claim boundary, bounded implementation handoff, and re-entry
   condition.

Do not keep ASE active after ordinary coding can proceed without invented
upper-layer meaning and with a bounded acceptance or evidence target.

The mission result is a bounded decision package:

- established result or removed blocker and exact affected scope;
- current authority reused, decision still owned, and uncertainty remaining;
- method result with its supported and unsupported claims;
- evidence used, evidence still required, and its invalidation boundary; and
- ordinary-workflow handoff, exit reason, and smallest re-entry condition.

## Five-layer semantic coordinate

The five-layer semantic coordinate answers where meaning belongs. The layers
are not phases, routes, mandatory checkpoints, or a required document set.

- **L0 Product:** why the product should exist and what outcome it owns.
- **L1 System:** what the system is responsible for and what lies outside it.
- **L2 Operation and domain:** how work and state change, which contracts
  apply, and who holds material authority.
- **L3 Technical design:** how governed meaning is realized through
  capabilities, components, interfaces, data, dependencies, and failure
  mechanisms.
- **L4 Implementation and evidence:** what was implemented or observed and
  what that evidence can support.

Only affected layers activate. Locate the highest unresolved meaning on which
the mission depends, reuse still-valid upper meaning, and stop descending when
the next action no longer needs to guess. Keep `proposed`, `human_confirmed`,
`implemented`, and `verified` distinct.

When a user asks for more detail or lists layers, methods, views,
confirmations, or checks, treat those categories as the reporting shape. Apply
this positive recipe when one L2 semantic delta or decision delta is active and
L0, L1, L3, and L4 remain valid:

- Active layer: L2.
- Method result: one semantic delta.
- Human decision: exactly the actual accountable L2 decision, when unresolved.
- Views: none. Activate an existing view only for a named consumer need,
  maintenance need, or recovery need.
- Cross-layer checks: none. Activate one only when the bounded decision or claim
  spans another layer.
- Handoff: reference the acceptance target without activating L4.
- Inactive categories: report each inactive category with its reason.

A request for detail changes reporting only and creates no project artifact.
Treat impact tracing under the same view predicate and the same check predicate,
regardless of label. Outside this recipe, a layer, method, view, confirmation,
or check activates only when its observable positive predicate holds for this
mission; otherwise report it inactive. Still-valid lower-layer meaning remains
closed when the bounded decision already supports the handoff.

A binding project-local semantic model wins. Use it directly and do not
automatically renumber, rewrite, migrate, or replace it. Translate to L0-L4
only when useful, label the mapping as a candidate, and preserve the project's
authority and ownership semantics.

## Five problem domains

Domains are entry classifications, not five workflows. Name one primary
problem domain and read its reference first. Load at most one necessary
secondary reference only after a demonstrated dependency prevents the primary
method from returning its result. Keep loading proportional and limited to this
minimum necessary dependency. No fixed domain-to-layer mapping exists.

1. **System meaning and decision authority**
2. **Architecture, decomposition, and critical assumptions**
3. **Evolution, refactoring, migration, and compatibility**
4. **AI coding delivery decomposition and continuity**
5. **Validation, quality, evidence, and claim boundaries**

## Method router and reference loading

Read the primary domain reference first after observing its trigger:

- Material terms, semantic ownership, accountable decision deltas, product
  principles, red lines, or precedence: read
  [system meaning and authority](references/system-meaning-and-authority.md).
- Architecture expression, responsibility concentration, seams, or a critical
  unproven capability: read
  [architecture and assumptions](references/architecture-and-assumptions.md).
- Consumer-visible behavior change, predecessor meaning, coexistence,
  compatibility, convergence, or irreversible retirement: read
  [evolution and migration](references/evolution-and-migration.md).
- Vertical slicing, work-unit scope, version horizons, context recovery, or a
  material correction: read
  [delivery and continuity](references/delivery-and-continuity.md).
- Validation authority, evidence identity, conflated claim objects, subjective
  quality, or an observed-delivery claim: read
  [validation, quality, and evidence](references/validation-quality-and-evidence.md).

For an explicit architecture health scan or observed material cross-file
architecture friction, first read the Codebase architecture scan method in the
architecture reference. Load
[codebase architecture scan](references/codebase-architecture-scan.md) only
when that method's positive predicate holds. Keep the scan read-only and end it
before any design or code modification.

Do not read all references for completeness. Select a method by its observable
positive and negative predicates, not its name, desired detail, project size,
or a generic keyword. Apply its full result, failure, authority, claim, stop,
handoff, and re-entry contract without creating a mandatory project artifact.

## Cross-cutting authority and claim boundaries

- Give each material meaning one current authority for its scope. Lower-layer
  evidence may support, refute, or reopen upper meaning; it cannot silently
  create or rewrite it.
- AI may choose reversible implementation details inside settled boundaries.
  Accountable humans own material product, system, domain, architecture,
  lifecycle, compatibility, and irreversible decisions.
- Only an accountable human creates `human_confirmed`. Tests, reports,
  generated evidence, elapsed time, model agreement, or agent consensus cannot
  create or substitute for it.
- Match claims to objects and evidence. Source, package, installation, runtime,
  publication, release, product outcome, and human acceptance are distinct.
  Evidence for one does not prove another.
- Bind reusable evidence to source revision, relevant inputs, configuration,
  tools or providers, environment, result, freshness, and invalidation or
  reopen conditions. Missing identity lowers the claim ceiling.
- Add a control only for an observed failure, risk, authority boundary, or
  irreversible consequence. More process or more evidence volume is not a
  stronger claim.

When authority is missing, return a candidate and the one accountable decision
instead of inventing an authority file. When evidence is missing, return the
strongest honest weaker result and the smallest discriminating next evidence.
When several domains appear, lead with the primary blocker and add only a
necessary dependent method.

## Handoff, stop, and re-entry

A bounded implementation handoff gives the ordinary coding workflow:

- objective, affected scope, authority sources, and protected non-goals;
- settled contracts, dependencies, and any pending human decision;
- acceptance or evidence target, unsupported claims, and invalidation state;
- stop condition and the smallest condition that re-enters ASE.

Hand ordinary planning, coding, TDD, debugging, review, branching, integration,
test execution, package operation, and release execution to the applicable
ordinary workflow or specialist Skill. Hand direction-changing unknown
discovery to `find-unknown` when available, while ASE retains system impact,
fallback, and claim boundaries. Hand autonomy-versus-confirmation calibration
to `decision-calibration` when its independent trigger applies.

Re-enter ASE only for a newly named system-engineering mission, invalidated
authority, cross-layer conflict, material migration or recovery consequence,
or a higher-scope closure claim. Re-entry reuses still-valid results and opens
only the smallest affected authority, method, and downstream scope.

Stop before irreversible action unless execution intent, replacement,
semantic and consumer disposition, recovery, per-object evidence, and
accountable confirmation support the exact scope. Stop at the strongest
supported claim even when the wider project remains incomplete.

---
name: ai-system-engineer
description: Use only when work must resolve a material cross-layer system decision, authority or lifecycle boundary, irreversible migration or recovery decision, readiness claim that ordinary implementation evidence cannot settle, or local choice depending on unresolved upper-layer meaning; also use for an explicit ASE request or read-only architecture scan. Do not use for routine coding, local refactors, ordinary debugging, documentation edits, package operations, or standard verification when requirements and authority are settled.
---

# AI System Engineer

Version 4.2.0.

Apply the smallest control that prevents the model from guessing system meaning
or overstating a claim.

## Applicability and exit gate

Before using any ASE method, name a specific unresolved system boundary and
state what material decision, action, or claim it blocks. For an explicit
read-only architecture scan, name the concrete architecture question and the
restructuring decision it will inform; the diagnosis may then determine
whether an unresolved boundary exists. If neither item can be named,
immediately stop using ASE and return to the ordinary task workflow.

Keywords alone—including architecture, recovery, migration, lifecycle, and
readiness—do not establish applicability. Task size, file count, duration, or
use of several modules does not establish it either. An explicit ASE request
loads this gate but does not waive it.

Using ASE does not automatically invoke another governance Skill or workflow,
create a governance file, add a project gate, or expand verification scope. Do
any of those only when independently required by the task and its applicable
instructions.

## Instruction level

Compact is the default. `使用 ASE`, `use ASE`, `使用 ASE 精简级`, and
`use ASE compact` select Compact. Compact does not read
`references/guided.md`.

`使用 ASE 细致级` and `use ASE guided` select Guided. For Guided, read
`references/guided.md` once and use only the applicable method sections.
Generic requests for more detail do not select Guided. Binding project, safety,
and permission rules apply at either level. This file is the sole semantic
authority; Guided expands execution but cannot override it or create a second
lifecycle.

## Control loop

1. Use the system boundary and blocker named at the applicability gate.
2. Locate the highest unresolved meaning that the requested action depends on.
3. Resolve only what the next action needs; keep the user's accountable
   decisions with the user.
4. Invoke a known method by name when native model competence is sufficient.
5. Bind the result to evidence with object, scope, relevant inputs,
   environment, result, and invalidation or reopen condition.
6. Stop when the bounded claim is supported and remaining uncertainty is
   explicit; escalate only for a named risk, failure, authority boundary, or
   irreversible consequence.

## Architecture expression selection

Before creating or revising an architecture expression, name the question and
choose the smallest sufficient expression. Reuse an adequate current
expression; if prose, a short list, or the existing authority is enough, do not
create a new diagram or file. Use prose for meaning and boundaries, a table for
exact mapping or comparison, and a diagram only when structure, dependency,
change, sequence, runtime, deployment, or provenance becomes materially clearer
nonlinearly. Combine forms only when each answers a distinct necessary
question. A requested diagram count, chosen notation, or possible future use
is not a reason to add an expression. Resolve unresolved meaning before
depicting it as settled.

For a persistent expression, identify whether it is formal semantic authority,
an authority-constrained derived view, candidate design, implementation or
validation evidence, or historical material. A derived view references its
current source and cannot silently become a second authority. Keep current and
future, logical and physical, confirmed, implemented, and verified, and partial
evidence and system completion distinct. Add sources, scope, claim limits, and
review triggers only in proportion to real maintenance or recovery risk.

For an explicit rendered-visual request, create or render a form supported by
the destination, observe the actual user-visible result or a delivered
inspectable artifact, inspect it, then show or attach that verified result.
Check readability, hierarchy, authority, scope, and evidence role during
inspection. Authoring renderable source, expecting downstream rendering, or
describing a result as rendered does not constitute inspection. If observation
is unavailable, explicitly report that delivery was not verified or completed.
Source alone satisfies only an explicit source request.

## Project-local model precedence

Use the default five-layer model below only when no binding project-local model
exists for the affected scope. When one exists, the project-local model and
authority win. Do not automatically renumber, rewrite, migrate, or reapprove
its architecture or evidence. A translation is a candidate mapping only; if it
changes meaning, authority, approval scope, or maintained consumers, require
explicit bounded human approval before migration. Installing this Skill does
not migrate a project.

## Five-layer architecture closure

For work that crosses system meanings, apply the control loop and treat the
highest unresolved active layer as the highest uncertain altitude. Do not
mechanically start at L0. Activate only the layers whose meaning or evidence is
unresolved, reuse still-valid upper-layer meaning and confirmations, and
descend only when the next layer can proceed without guessing. Exit when more
upper-layer design would not change the bounded decision or its evidence.
Required outputs are semantics, not mandatory documents. Keep `proposed`,
`human_confirmed`, `implemented`, and `verified` distinct at every layer.

### L0 Product Position

**Owns:** Why the product should exist and which outcome it is accountable for.

**Minimum inputs:** The affected users or beneficiaries, observed problem or
opportunity, current product authority, material constraints, and known red
lines.

**Required semantic outputs:** Answer fixed questions, not a fixed document
shape: target users and beneficiaries; the confirmed core problem or
opportunity and reason the product should exist; intended value, outcome, and
product responsibility; decision meaning that distinguishes success, failure,
out-of-scope results, and when insufficient or invalid evidence permits no
conclusion; in-scope and out-of-scope results and non-goals; material
constraints and product red lines; and conditions that invalidate or reopen
the product position. A project may merge or split these semantics without
duplicate authority. Do not prescribe a section count, headings, artifact
form, or discussion order.

Add only the supplements whose observable predicates apply:

- If outputs can materially affect people, groups, or organizations that are
  not users, identify the affected parties, plausible harms, and rights
  boundaries.
- If an unproven capability supports core L0 or L1 value and its failure would
  change product position or system responsibility, use the existing
  innovation-dependency contract below. Before L0 closes, make its assumption
  and scope, supported product conclusion, minimum evidence, validation owner,
  cheapest disposable validation, fallback, and L0 reopen condition explicit
  in that authority; do not copy the full contract into L0.
- If experimental, shadow, limited-pilot, and formal-use states differ,
  distinguish their claim boundaries. Without the specific-use validation
  required for a state, do not claim suitability for that use.
- If product claim, project or environment applicability, and formal adoption
  depend on different evidence or accountable decisions, keep the conclusions
  distinct; they cannot substitute for one another. Keep only the conclusion
  boundaries in L0, system boundaries in L1, and teams, process, permissions,
  and operational responsibility in L2.
- If core value depends on total cost, cycle time, or practical adoptability,
  define the comparison scope, costs that cannot be hidden, minimum evidence,
  fallback, and corresponding reopen condition.

**Exit standard:** All core semantics are complete; every supplement whose
predicate is observed is resolved, while untriggered supplements are not added
mechanically. The accountable owner can distinguish success, failure,
out-of-scope, and currently inconclusive results without depending on an
undefined system or implementation.

**Authority boundary:** Only the accountable product owner may mark L0
`human_confirmed`; technical feasibility evidence cannot silently redefine
product position.

**Constrains:** L1 system responsibility and every downstream claim.

**Reopen when:** A user or beneficiary, core problem or opportunity, reason to
exist, intended value, outcome, product responsibility, scope, constraint, red
line, decision meaning, or triggered supplement changes or proves unsupported,
or a recorded invalidation or reopen condition occurs.

### L1 System Definition and Boundaries

**Owns:** What the system is responsible for, what it excludes, and how it
relates to people, organizations, and external systems.

**Minimum inputs:** Still-valid L0 meaning, current system context and
authority, external actors and systems, ownership, material constraints,
trust boundaries, and system-level risks or unproven dependencies.

**Required semantic outputs:** System responsibility, boundary and context,
external relationships, accountable ownership, system invariants, material
constraints, and system-level failure absorption or fallback.

**Exit standard:** L2 can define operation without inventing system
responsibility. L1 does not settle the full solution architecture.

**Authority boundary:** Confirm product or system responsibility with its
accountable owner; keep solution choices that do not change it below L1.

**Constrains:** L2 operational authority and domain contracts, and all later
solution and evidence claims.

**Reopen when:** System responsibility, boundary, external relationship,
ownership, invariant, or system-level dependency changes or is contradicted.

### L2 Operational Model, Authority, and Domain Contracts

**Owns:** How the system operates, how domain state changes, and who may decide
or perform each material action.

**Minimum inputs:** Still-valid L1 meaning, representative operational
scenarios, domain facts, roles and authority sources, lifecycle constraints,
compliance obligations, and known failure or recovery cases.

**Required semantic outputs:** Operational flows, state transitions, roles and
decision rights, domain rules and contracts, invariants, exceptions, and
failure and recovery semantics.

**Exit standard:** L3 can design without inventing domain policy, operational
authority, lifecycle meaning, or system responsibility.

**Authority boundary:** Accountable domain and authority owners confirm
material rules and decision rights; a technical design cannot create them.

**Constrains:** L3 capabilities, components, interfaces, data responsibility,
and failure mechanisms.

**Reopen when:** A flow, state, domain rule, authority, invariant, exception,
or recovery obligation changes or conflicts with L1.

### L3 Solution Architecture and Design

**Owns:** How governed product, system, operational, and domain meaning is
realized as a coherent technical solution.

**Minimum inputs:** Still-valid L2 contracts, current technical authorities,
quality attributes, platform and delivery constraints, dependency facts, and
relevant feasibility evidence.

**Required semantic outputs:** Required capabilities, component and module
responsibilities, public interfaces, data ownership and movement, dependency
direction, runtime or deployment mechanisms when material, failure handling,
and traceability to L2 contracts.

**Exit standard:** L4 can implement without guessing design meaning, and the
L3-to-L4 implementation-sufficiency check passes.

**Authority boundary:** Keep material architecture choices with the
accountable owner; AI may choose reversible implementation details inside the
confirmed design boundary.

**Constrains:** L4 implementation scope, tests, validation, and supported
claims.

**Reopen when:** A governed contract, component responsibility, interface,
data owner, dependency, quality attribute, or failure mechanism changes or
proves infeasible.

### L4 Implementation and Verification

**Owns:** What was actually implemented and what the observed evidence can
support.

**Minimum inputs:** Still-valid L3 design, bounded implementation scope,
source and runtime environment, acceptance and verification criteria,
deviations, and required operational evidence.

**Required semantic outputs:** Implemented scope, verification results and
environment, traceability to design, deviations, failures, residual risks,
unsupported claims, and invalidation conditions.

**Exit standard:** Implementation matches the confirmed design, required
verification passes for the bounded claim, and the L0-to-L4 end-to-end
consistency check passes before final confirmation.

**Authority boundary:** Implementation and tests create implementation or
verification evidence only; they cannot create product acceptance,
`human_confirmed`, release approval, or system completion.

**Constrains:** Only the bounded operational, readiness, installation, or
release claims actually supported by corresponding evidence.

**Reopen when:** Implementation diverges from design, evidence becomes stale or
invalid, a required check fails, or an upper-layer meaning changes.

## Derived architecture views

When L1 exits, generate or refresh the **Product and System Intent View** from
L0-L1. When L2 exits, generate or refresh the **Operational and Domain Contract
View**. When L3 exits, generate or refresh the **Solution Design View**. When L4
implementation completes, generate or refresh the **Implementation and
Evidence View** with `implemented` status; refresh it after verification with
`verified` status.

Each view is a smallest-sufficient, authority-constrained presentation for its
reader, not a second semantic authority. Reference its sources, scope, status,
unresolved items, evidence limits, and reopen condition. Reuse an adequate
current view and refresh only affected views. Automatic view production does
not by itself create a persistent file or require a diagram; use the
architecture-expression rule above to choose prose, table, diagram, or reuse.

## Three mandatory confirmation bands

For an end-to-end closure, require three separate accountable-human
confirmations:

1. **Product and System Band (L0-L1):** after L1 exits, confirm product position,
   system responsibility, boundaries, ownership, and material constraints.
2. **Operational and Contract Band (L2):** after L2 exits, confirm flows, state,
   domain contracts, authority, failure, and recovery meaning.
3. **Design and Implementation Band (L3-L4):** after L4 evidence and the
   end-to-end check are ready, confirm design, implementation, verification,
   deviations, and residual risk for the named scope.

Record each result as `human_confirmed`, `rejected`, or `reopen`. Do not merge
or skip confirmations because one person owns all three bands. An existing
still-valid confirmation may satisfy its named checkpoint; do not request it
again unless affected meaning or evidence reopens. The L3-to-L4 automatic
check does not create a fourth human confirmation. Final-band confirmation
does not imply release approval unless release is explicitly in its scope.

## Cross-layer consistency

Before each L1-L4 layer exits, compare its required outputs with the direct
upper layer and resolve any missing mapping, contradiction, or invented meaning.
Additionally:

- Before L4 work that depends on L3 begins, run the **L3-to-L4
  implementation-sufficiency check**; dependent implementation stops if the
  design cannot support it without guessing.
- Before closing the final band, run the **L0-to-L4 end-to-end consistency
  check** so locally consistent adjacent layers cannot hide cumulative drift.

Return each consistency result with checked layers, source versions, satisfied
mappings, gaps or conflicts, a pass, blocked, or reopen status, affected
downstream scope, and invalidation conditions. On failure, do not close the
current layer or band. Reopen the smallest affected owning layer and invalidate
dependent downstream results, views, and confirmations; repair, freshly check,
and reconfirm only the affected scope.

## Delivery scope and claim aggregation

For material AI-coding delivery closure, distinguish **Version Scope**,
**Vertical Delivery Slice**, and **AI Work Unit**. They are delivery and claim
objects, not architecture layers. An AI Work Unit does not prove a Vertical
Delivery Slice complete. A Vertical Delivery Slice does not prove a Version
Scope complete. Give each object its authority sources, bounded scope, status,
evidence, unsupported claims, and invalidation or reopen condition.

Multi-version planning is a delivery-planning horizon, not an architecture
layer. For successive versions in one product, system responsibility, and
continuous evolution chain, reuse one current architecture authority and vary
design depth by planning horizon, without mechanically repeating layers,
confirmations, or derived views:

- **Current delivery horizon:** complete the affected-layer closure, produce an
  implementable design, and obtain the implementation, verification, and
  evidence required for that version's claim. Reuse still-valid upper meaning,
  views, and confirmations.
- **Next delivery horizon:** design only far enough to prevent a foreseeable
  current-version block. Identify expected user outcomes and key operational
  scenarios; cross-layer effects on current product and system meaning, domain
  contracts, interfaces, data ownership, and quality attributes; the minimum
  architecture runway the current version must preserve; and unproven critical
  assumptions, their least-cost validation, and triggers for re-entering
  detailed design. This does not support implementation-level design,
  verification, or version-closure claims for the next version.
- **Longer-term horizon:** retain only direction, red lines, key assumptions,
  and triggers for more detailed design. Do not freeze modules, interfaces,
  implementation choices, verification conclusions, or human confirmation.

Planning horizons are not fixed depth quotas. Deepen a future horizon only for
the affected scope when it contains an irreversible or high-migration-cost
decision, long-lead dependency, cross-version shared contract, public interface,
or data model, a security, compliance, recovery, or operational risk that would
change the current design, or a technical assumption whose prior validation is
required for the current product or system commitment. If a future version
changes current product position, system responsibility, domain rules, or other
upper meaning, reopen the highest affected owning layer and its downstream
scope; do not treat the change as architecture runway. If named versions belong
to a different product, system responsibility, or discontinuous evolution
chain, give each its own architecture closure instead of applying this shared
multi-version rule.

Define each Vertical Delivery Slice at L2 as the smallest independently
assessable operational scenario and outcome. Make it implementable at L3, then
implement and verify it at L4. Trace it to still-valid L0-L1 meaning; do not
mechanically reopen L0-L1. For a complex new delivery path, prefer a walking
skeleton that exercises the real integration and evidence path. Enabler work
must name the slice it unblocks and cannot claim business value by itself.

AI may propose, compare, and recommend candidate slices. AI may select one only
inside still-valid human-confirmed L0-L2 meaning, under a preconfirmed selection
policy, when the choice is reversible and changes no product priority,
authority, contract, acceptance meaning, red line, or material risk boundary.
Otherwise the accountable human selects through the existing Operational and
Contract Band. This slice decision does not create a fourth confirmation.

For an iteration, identify the highest affected layer for each changed scope.
Reuse unaffected layers, views, confirmations, slices, and evidence. Reopen
that layer and only its dependent downstream scope; invalidate a reused result
only when changed meaning or evidence affects it. A formal version candidate
aggregates changed and reused slices, runs required cross-slice checks and the
L0-to-L4 end-to-end check, and uses the existing final band. Release approval
remains separate unless explicitly included in its accountable scope.

Roll up work-unit evidence only after integration into its named slice. Slice
closure requires slice-level scenario, contract, integration, failure, and
recovery evidence applicable to its claim. Version closure additionally
requires version-level cross-slice regression, affected architecture and
dependency consistency, and required operational evidence. A higher-scope
status cannot be inferred from lower-scope evidence. Tests cannot create
`human_confirmed`.

Before ordinary implementation, hand off a bounded AI Work Unit with objective,
authority sources, allowed scope, non-goals, acceptance, required checks,
dependencies, stop condition, and reopen route. Work in small independently
reviewable and integrable batches. Maintain one active write owner for
overlapping files, interfaces, schemas, or data contracts; parallelize only
independent non-overlapping scope with explicit integration obligations.

Add risk-specific evidence only when its observable predicate applies:

- For authentication, authorization, personal or secret data, or external
  dependencies, check the applicable security and supply-chain boundary.
- For a migration, public contract, protocol, or irreversible data change,
  check compatibility, partial transition, repair, rollback, and the
  irreversible point.
- For a production or operational claim, require the applicable environment,
  rollout, monitoring, failure-absorption, and recovery evidence.

Apply these controls only when the named risk is present. Once the handoff is
bounded and upper meaning is settled, return to the ordinary coding workflow.
Re-enter ASE only for a named cross-layer conflict, invalidated authority,
irreversible consequence, or slice or version closure claim. For detailed
execution, read `references/ai-coding-delivery.md` only when this section
applies.

## Cross-layer decision controls

When a material L2-L4 choice depends on recurring cross-layer product
principles, red lines, or precedence, use the current product-design
constitution or equivalent authority; reuse an adequate current authority. If
it is absent, conflicting, or cannot distinguish the alternatives, do not
close the affected choice until the accountable product owner confirms its
authority boundary, actionable principles, non-negotiable red lines with
source and scope, conflict precedence, and bounded deviation conditions; when
a long-term vision or research source exists, separate it from current
commitments; do not require a vision document, and do not require a new file.
The constitution guides L2-L4 but cannot change L0-L1; reopen the owning
altitude if product or system meaning changes, using the owning layer in the
active model. Do not apply this to ordinary reversible work with settled
criteria.

If an unproven technical capability supports a product value, system
definition, or readiness claim and its failure would change L0 or L1 meaning,
establish a bounded innovation-dependency contract; do not close the affected
L0 or L1 design until it names the assumption and scope, supported upper-layer
conclusion, required system mechanisms, current evidence and unsupported
claims, minimum acceptable measures, validation owner, cheapest disposable
validation, fallback, and conditions that reopen L0 or L1. Production
implementation may remain pending. Validation execution may remain pending.
The contract, not completed validation, is the closure requirement; validation
responsibility and safe failure absorption may not remain implicit. External,
model-generated, or small-sample evidence supports only its observed scope,
not this system's production feasibility. Do not apply this to an ordinary
choice or an innovation replaceable inside governed L3-L4 meaning; route an
unanswered design-changing unknown through the existing method trigger below.

For a material unresolved human-owned decision, use a Socratic decision-tree
interview: inspect available facts, resolve parent decisions before dependent
ones, ask one question at a time with a recommended answer, and do not begin
implementation that depends on the unresolved decision.

## Method triggers

- Existing behavior at risk: characterization testing, then TDD with a
  realistic example. Preserve observed contracts before changing internals;
  stop when the named behavior is preserved and affected checks pass. A simple
  local bug with a settled contract and repair path uses ordinary debugging
  and TDD; do not load the scan reference.
- Predecessor convergence: semantic inventory plus consumer trace. Treat prior
  behavior and evidence as inputs, not an oracle; give compatibility a named
  consumer and exit.
- Package or installation claim: exact mirror plus real-environment smoke.
  For this Skill's package-structure check, run `scripts/check_package.py`;
  its result supports structure and self-containment only, not installation or runtime behavior.
  Keep source, package, personal installation, tag, and public release as
  separate claim objects. Stop at the strongest claim object actually
  exercised.
- Domain or subjective quality: independent critic plus reference floor.
  Generated agreement supports no accountable-human decision. Stop with the
  bounded quality claim and residual uncertainty explicit.
- Materially ambiguous, overloaded, or conflicting domain terms: active domain
  language. Cross-check scenarios and current facts; update only an existing
  confirmed authority, never promote an AI proposal to domain truth, and stop
  when the next governed action has one usable meaning or a human-owned
  decision is explicit.
- L3 solution or module boundary or public interface at risk: deep-module and seam
  analysis. Prefer a narrow stable interface around real responsibility,
  authority, lifecycle, failure, dependency, or change boundaries; adapters
  translate protocols, not business truth. Reject forwarding-only splits and
  stop when dependency direction and public-interface evidence support local
  change.
- Explicit codebase architecture scan or observed cross-file architecture
  friction: read `references/codebase-architecture-scan.md` and perform a
  read-only diagnosis. Prefer user scope, then evidence-backed hotspots, and
  return traceable candidates without modifying code or settling an
  interface. Stop after the prioritized finding; if the user selects a
  candidate, end the diagnosis and start a separate `design-change`.
- Design-changing unknown not answerable from current facts or dialogue:
  invoke `find-unknown`. Prototype only when preference requires seeing or the
  answer requires executable behavior; ask one question with the cheapest
  disposable medium. Return observations, limits, and design impact, never a
  production, acceptance, or release claim.
- Work spanning sessions or agents, or with material recovery cost:
  recoverable handoff. Reference current authorities and evidence, remove
  sensitive data, keep one current status pointer and one decision trace, and
  stop only when a fresh context can recover the next action and pending human
  decision without hidden chat.

## Hard boundaries

- Give each normative question one current authority for its scope. A lower
  layer cannot invent product, system, operational, domain, design, or authority
  meaning owned above it.
- AI may choose reversible implementation details inside governed boundaries.
  Material product, architecture, authority, lifecycle, and irreversible
  decisions remain with the accountable user.
- Only an accountable human creates `human_confirmed`. Tests, reports, time,
  model output, or agent consensus cannot substitute.
- Structural, source, runtime, and human evidence support only corresponding
  claims. Do not infer product outcome, installation, release, or human
  acceptance from a weaker evidence type.
- On a material correction use `Capture → Classify failed control → Repair →
  Prevent → Fresh verify`. Repair the smallest owner and dependent claims; add
  only a proportional prevention and prove it distinguishes the failed and
  repaired conditions.
- When continuity matters, require a fresh context to recover objective and
  scope, current authority, supported and unsupported claims, evidence and
  reopen triggers, next action, and pending human decision. Hidden chat,
  obsolete plans, or unrouted history leave continuity unsupported.
- When an active-authority file enters an excluded immutable archive, classify
  it as irreversible retirement, not ordinary organization, deletion, or later
  archive editing. Require an exit reason, authority or replacement
  disposition, reference and consumer disposition, a recovery boundary, and
  accountable confirmation; then route one file at a time to a verified
  controlled archive intake that preserves ordinary excluded-path blocking.
  If any lifecycle prerequisite remains unresolved, if any required
  configuration for the active-source root, archive root, or approval type is
  absent or invalid, or if the capability is unavailable or does not complete,
  stop without a bypass and leave retirement unproven. Process multiple files
  separately; do not claim atomic multi-file intake.
- Read-only candidate identification and preflight do not authorize irreversible
  execution; require explicit execution intent for the bounded scope. For
  multiple in-scope objects, perform a read-only whole-scope conflict check
  before the first irreversible operation, then execute and evidence each
  object independently; do not claim batch atomicity. If execution stops
  partway, preserve completed evidence, distinguish completed, failed, and
  unstarted scope. Before retrying a failed object, prove that it did not
  complete; treat an unknown outcome separately and reconcile it without
  re-execution. Resume only failed or unstarted objects after their blockers
  are resolved; continuation does not extend the accountable decision.
  Completed object operations do not prove governance closeout: verify the
  current authority and affected consumers, result evidence, and disposition
  of any temporary execution authority before making that claim.
- Before irreversible retirement or deletion, require replacement evidence,
  semantic and consumer disposition, a recovery boundary, and accountable
  confirmation.

Do not add a gate, template, agent, review, route, or file without a named
failure or risk that needs it. More activity is not stronger evidence.

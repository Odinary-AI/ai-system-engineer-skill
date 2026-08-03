---
name: ai-system-engineer
description: Use only when work must resolve a material cross-layer system decision, authority or lifecycle boundary, irreversible migration or recovery decision, readiness claim that ordinary implementation evidence cannot settle, or local choice depending on unresolved upper-layer meaning; also use for an explicit ASE request or read-only architecture scan. Do not use for routine coding, local refactors, ordinary debugging, documentation edits, package operations, or standard verification when requirements and authority are settled.
---

# AI System Engineer

Version 3.5.0.

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

## Conditional altitude check

For work crossing several system boundaries, reason from the highest uncertain
altitude: L0 Product, L1 System, L2 Lifecycle, L3 Capability, L4 Module, L5
Implementation. Descend only when the next layer can proceed without guessing.
Exit when the next layer has sufficient governed meaning and more upper-layer
design would not change the bounded decision or its evidence. Do not create an
architecture artifact merely because this check was used.

When a material L2-L5 choice depends on recurring cross-layer product
principles, red lines, or precedence, use the current product-design
constitution or equivalent authority; reuse an adequate current authority. If
it is absent, conflicting, or cannot distinguish the alternatives, do not
close the affected choice until the accountable product owner confirms its
authority boundary, actionable principles, non-negotiable red lines with
source and scope, conflict precedence, and bounded deviation conditions; when
a long-term vision or research source exists, separate it from current
commitments; do not require a vision document, and do not require a new file.
The constitution guides L2-L5 but cannot change L0-L1; reopen the owning altitude if product or
system meaning changes. Do not apply this to ordinary reversible work with
settled criteria.

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
choice or an innovation replaceable inside governed L3-L5 meaning; route an
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
- L4 module boundary or public interface at risk: deep-module and seam
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
  layer cannot invent product, system, lifecycle, capability, or authority
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

# Project Validation Strategy

Read this reference only for the project-validation-strategy trigger in
`SKILL.md`. `SKILL.md` remains the sole semantic authority. This method
assesses and repairs a project validation execution boundary; it does not add
an architecture layer or run routine verification.

## Contents

- [Applicability and boundary](#applicability-and-boundary)
- [Authority ownership](#authority-ownership)
- [Assessment](#assessment)
- [Result contract](#result-contract)
- [Proportional verification and reuse](#proportional-verification-and-reuse)
- [Persistence and canonicality](#persistence-and-canonicality)
- [Relationship and exit](#relationship-and-exit)

## Applicability and boundary

Use this method only after the ASE applicability gate identifies a named
material decision, action, or claim blocked by missing, conflicting, or
insufficient project validation authority. The unresolved boundary must concern
claim-to-evidence meaning, validation responsibility, evidence applicability,
or accountable-human confirmation across more than settled implementation
details.

Do not use repository size, test count, testing or release keywords, a routine
defect, an ordinary refactor, a concrete test command, or an expensive suite by
itself as the trigger. When existing requirements and authority already settle
the work, Exit ASE and use ordinary verification.

## Authority ownership

Treat the strategy as an authority-constrained execution mapping. The current
project normative authority retains ownership of each claim, minimum evidence
state, applicable representativeness, operational responsibility, technical
validation design, and acceptance threshold. The project-local model and
authority win. Do not translate or renumber its meanings. Only when the default
five-layer model applies, map these owners to L0-L3. The strategy may map those
decisions to concrete commands, affected scope, cadence, environments,
escalation predicates, and evidence handling. It cannot redefine the owning
meaning, create `human_confirmed`, or become a sixth layer.

Inspect the current project validation authority set before proposing a change.
The set may be one source or several traceable, non-conflicting sources such as
testing guidance, contribution rules, CI contracts, engineering handbooks,
release procedures, operational rules, or governance authorities. Do not
require one file or one conventional testing-policy filename when the set is
already usable.

## Assessment

1. Name the blocked claim, owning authority or layer, bounded scope,
   environment or population, accountable decision, and strongest conclusion
   sought.
2. Locate only the current sources needed to assess that claim. Map their
   commands, scope, coverage, environment, cadence, escalation, evidence
   handling, and human authority; report conflicts instead of choosing one.
3. Check critical scenarios and contracts, applicable failure and recovery
   paths, external dependencies, compatibility, and domain or subjective
   quality. Activate security, provider, hardware, performance, artifact, or
   real-environment evidence only when the claim requires it.
4. Classify the authority disposition before designing anything new. State
   exactly one literal disposition label in every result, including when the
   authority set has not yet been inspected:
   - `adequate-existing`: reuse the current authority set.
   - `partial-existing`: propose the smallest repair to its current carrier.
   - `missing-required`: return the smallest candidate strategy without
     assigning it authority.
   - `not-required`: exit because ordinary verification can proceed without
     unresolved cross-layer meaning.
   - `unproven`: stop because authority, inputs, environment, or accountable
     ownership cannot support a strategy or the requested claim.
5. For `partial-existing` or `missing-required`, derive only the execution
   mapping needed by the blocked claim. Preserve supported and unsupported
   conclusions and name the smallest next evidence.

## Result contract

Return these semantics in the smallest useful form:

- **Blocked claim:** Object, scope, owning authority or layer, strongest
  requested conclusion, and the validation boundary that blocks it.
- **Authority set:** Sources inspected, their current scope, mappings,
  conflicts, gaps, and accountable owners.
- **Disposition:** Exactly one assessment disposition and its evidence basis.
- **Execution mapping:** Each applicable claim or contract mapped to the
  focused, affected-flow, integration, full-regression, real-environment,
  operational, or human evidence it needs and cannot obtain from weaker checks.
- **Evidence identity:** Source revision, inputs, commands or observations,
  configuration, tools or providers, environment, result, freshness, and
  invalidation conditions.
- **Human boundary:** Who may define or confirm claim meaning, validation
  operation, acceptance, stage transition, and release; keep these decisions
  distinct when their authority differs.
- **Stop and reopen:** Unsupported claims, the next ordinary action, and the
  changes that invalidate the strategy or reopen an owning authority or layer.

## Proportional verification and reuse

Use focused checks for fast feedback and affected-flow checks for integration
only when they support the bounded claim. Full regression follows current
project authority and the named claim; suite cost cannot lower an accepted
evidence requirement. If authority is unresolved, recommend proportional
evidence but do not use partial checks to infer a broader integration,
readiness, merge, stage, or release conclusion.

Reuse expensive evidence only when its source revision, relevant inputs,
configuration, tools or providers, environment, result, and invalidation
conditions remain applicable. A changed dependency, provider, configuration,
environment, claim scope, evidence population, or affected contract may make
prior evidence stale even when a check has the same label.

## Persistence and canonicality

Return the candidate in the conversation by default. Persist it only when the
current task authorizes a write to the project's durable workspace. Use the
project's existing authority and approval rules as well as its carrier,
location, and name. Write permission alone does not authorize changing
validation authority. If no carrier is designated or the task cannot modify
its authority, leave the carrier, location, and name to the user or accountable
owner and return a non-authoritative candidate or patch proposal.

Do not give the candidate a conventional policy filename unless the
accountable project authority also confirms or maps it as the current
authority. A reversible write, an AI proposal, automated evidence, or file
creation cannot create canonical authority. Update an existing adequate
carrier instead of creating a duplicate.

## Relationship and exit

Ordinary development workflows execute tests and collect L4 evidence. This
method alone does not invoke GAC, modify another workflow, create CI, or select
a routine test command. Automated checks and AI critics cannot create human
acceptance, stage approval, release approval, or subjective-quality approval.

If the strategy would need to invent or change a claim, acceptance threshold,
operational authority, design contract, or formal approval, reopen the smallest
owning authority or layer; name L0-L3 only when the default five-layer model
applies. If no accountable owner or applicable evidence can be established,
return `unproven`. Exit ASE when the authority set or bounded candidate lets the
next ordinary action proceed without guessing; persistence and canonicalization
may remain a separate accountable decision.

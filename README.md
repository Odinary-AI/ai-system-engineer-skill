# AI System Engineer

An independently callable and re-entrant system-engineering method Skill for
developing, evolving, and restructuring complex systems with AI coding.

## When to use

Use this Skill when either:

- a complex-system startup or material new delivery path needs a bounded
  system-engineering result before ordinary implementation can be scoped; or
- existing work is blocked by unresolved system meaning, decision authority,
  architecture, migration, delivery continuity, evidence, or claim boundaries.

An explicit read-only architecture scan is also supported when it names the
architecture question and the restructuring decision it will inform.

Do not use it for routine coding, local refactoring, ordinary debugging,
documentation edits, package operations, or standard verification when
requirements, authority, and evidence are already settled. Keywords, repository
size, file count, project duration, or generic architecture language do not
establish applicability by themselves. If no startup result or intervention
blocker can be named, return to the ordinary task workflow.

## Current version

This package contains Version 5.0.0. It replaces fixed depth modes and
lifecycle-shaped closure machinery with:

- a startup/intervention mission gate and four-step bounded mission loop;
- a five-layer semantic coordinate that is not a development lifecycle;
- five observable problem domains routing 21 reusable methods; and
- proportional reference loading, ordinary-workflow handoff, and explicit
  re-entry conditions.

ASE does not own routine planning, coding, TDD, debugging, review, Git, CI,
installation, publication, or release execution. It may precede or interrupt an
ordinary coding workflow for a named system-engineering mission, then exits as
soon as that workflow can proceed without guessing upper-layer meaning.

A binding project-local model remains authoritative. Installing this Skill does
not automatically renumber, migrate, or reapprove an existing project's
architecture or evidence.

## Install in Codex

The following commands install the current `main` branch into a new destination:

```bash
git clone https://github.com/Odinary-AI/ai-system-engineer-skill.git
mkdir -p ~/.codex/skills/ai-system-engineer
cp -R ai-system-engineer-skill/SKILL.md \
  ai-system-engineer-skill/references \
  ai-system-engineer-skill/scripts \
  ~/.codex/skills/ai-system-engineer/
python3 ~/.codex/skills/ai-system-engineer/scripts/check_package.py
```

For an upgrade, back up the existing destination and replace it as one unit
before copying the new package. Do not merge-copy over an older installation:
the checker detects missing or unexpected runtime files but does not restore the
previous installation.

For another Agent Skills-compatible host, use that host's normal installation
method and preserve the destination directory name `ai-system-engineer`.

## Use

```text
Use $ai-system-engineer to review this system decision.
```

The Skill keeps accountable product, architecture, lifecycle, authority, and
irreversible decisions with the responsible human. Tests, reports, model
output, or agent agreement cannot create human confirmation.

See [SKILL.md](SKILL.md) for the complete workflow.

## Requirements

- An Agent Skills-compatible host.
- Python 3.9 or later only when running the bundled package checker.

## License

Available under the [MIT License](LICENSE).

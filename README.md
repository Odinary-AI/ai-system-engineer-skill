# AI System Engineer

An Agent Skill for AI-assisted system work that crosses product intent,
architecture, authority, lifecycle, migration, recovery, irreversible change,
or readiness-claim boundaries.

## When to use

Use this Skill only when an unresolved cross-layer system meaning, authority or
lifecycle boundary, irreversible migration or recovery decision, or readiness
claim blocks a material decision, action, or claim. An explicit read-only
architecture scan is also supported when it names the architecture question and
the restructuring decision it will inform.

Do not use it for routine coding, local refactoring, ordinary debugging,
documentation edits, package operations, or standard verification when
requirements and authority are already settled. Keywords such as
`architecture`, `migration`, or `readiness` do not establish applicability by
themselves. If no concrete unresolved boundary and blocked outcome can be
named, return to the ordinary task workflow.

## Current version

The `main` branch contains Version 4.3.1. The latest annotated tag and
non-draft GitHub Release remain v4.3.0; a default clone installs `main`, not the
latest tagged Release.

Version 4.3.1 adds a conditional confirmation-readiness quality gate for
proposed or reopened L0-L3 normative meaning. It references still-valid
authority instead of resubmitting unchanged meaning and presents one bounded
normative question as one confirmation request, while preserving separate
owners and confirmation bands. The existing project-validation-strategy method,
project-local authority precedence, and routine-task exit boundary remain
unchanged. The two instruction levels remain unchanged:

- **Compact** is the default and applies the smallest control needed.
- **Guided** loads additional guidance for work that needs a more detailed
  method.

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

Compact:

```text
Use $ai-system-engineer to review this system decision.
```

Guided:

```text
Use $ai-system-engineer in guided mode for this migration decision.
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

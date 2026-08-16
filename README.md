# AI System Engineer

An Agent Skill for AI-assisted system work that crosses product intent,
architecture, authority, lifecycle, migration, recovery, irreversible change,
or readiness-claim boundaries.

Version 4.3.0 adds a conditional project-validation-strategy method for material
decisions, actions, and claims blocked by missing, conflicting, or insufficient
validation authority. It assesses a single source or distributed authority set,
returns an explicit disposition, and derives the smallest usable execution
mapping without turning AI output, a write, or a conventional filename into
project authority. It preserves project-local authority models and keeps
routine testing outside ASE. The two instruction levels remain unchanged:

- **Compact** is the default and applies the smallest control needed.
- **Guided** loads additional guidance for work that needs a more detailed
  method.

A binding project-local model remains authoritative. Installing this Skill does
not automatically renumber, migrate, or reapprove an existing project's
architecture or evidence.

## Install in Codex

```bash
git clone https://github.com/Odinary-AI/ai-system-engineer-skill.git
mkdir -p ~/.codex/skills/ai-system-engineer
cp -R ai-system-engineer-skill/SKILL.md \
  ai-system-engineer-skill/references \
  ai-system-engineer-skill/scripts \
  ~/.codex/skills/ai-system-engineer/
python3 ~/.codex/skills/ai-system-engineer/scripts/check_package.py
```

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

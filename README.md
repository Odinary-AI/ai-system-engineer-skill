# AI System Engineer

An Agent Skill for AI-assisted system work that crosses product intent,
architecture, authority, lifecycle, migration, recovery, irreversible change,
or readiness-claim boundaries.

Version 3.4.1 provides two instruction levels:

- **Compact** is the default and applies the smallest control needed.
- **Guided** loads additional guidance for work that needs a more detailed
  method.

This version also adds proportional architecture-expression selection and
strengthens irreversible retirement: read-only identification and preflight do
not authorize execution, multi-object work is preflighted as a whole and
executed independently, partial results remain explicit, and completed object
operations do not by themselves prove governance closeout.

## Install in Codex

```bash
git clone https://github.com/Odinary-AI/ai-system-engineer-skill.git
mkdir -p ~/.codex/skills/ai-system-engineer
cp -R ai-system-engineer-skill/SKILL.md \
  ai-system-engineer-skill/references \
  ai-system-engineer-skill/scripts \
  ~/.codex/skills/ai-system-engineer/
```

For another Agent Skills-compatible host, use that host's normal installation
method and preserve the destination directory name `ai-system-engineer`.
`README.md` and `LICENSE` document this repository but are not part of the
installed runtime Skill package.

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

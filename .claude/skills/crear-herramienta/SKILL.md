---
name: crear-herramienta
description: Crea una nueva skill, subagente o ajuste de Claude Code dentro del cerebro (este repo) y la sube a GitHub para que esté disponible en todos los dispositivos. Úsala cuando el usuario pida crear o modificar una skill, un agente, un comando o un hook.
---

# Crear herramienta

## Skill
Crea `.claude/skills/<nombre-en-kebab-case>/SKILL.md`:

```markdown
---
name: <nombre>
description: <qué hace y CUÁNDO usarla; esto decide si Claude la activa>
---

# <Título>
<instrucciones paso a paso; archivos de apoyo junto a SKILL.md si hacen falta>
```

## Subagente
Crea `.claude/agents/<nombre>.md`:

```markdown
---
name: <nombre>
description: <cuándo delegarle trabajo>
tools: Read, Grep, Glob   # omite para heredar todas
---

<prompt de sistema del agente>
```

## Ajustes / hooks / permisos
Edita `.claude/settings.json` (JSON válido; fusiona, no sobrescribas).

## Al terminar
1. Añade una línea en la tabla "Herramientas" de `README.md`.
2. Commit (`skill: <nombre>` / `agente: <nombre>` / `config: …`) y súbelo a la rama principal `claude/zealous-cray-ira4xc` (ver reglas en `CLAUDE.md`).
3. Recuerda al usuario: en una sesión nueva ya estará disponible; en local, `git pull` en su clon.

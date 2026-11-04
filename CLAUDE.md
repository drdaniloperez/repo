# Cerebro de Danilo

Este repositorio es mi "cerebro": memoria, skills, agentes y configuración de Claude Code.
Vive en GitHub para que cualquier sesión (nube, escritorio, móvil, terminal) tenga las mismas herramientas.

## Memoria (se carga en cada sesión)

@memoria/perfil.md
@memoria/preferencias.md
@memoria/aprendizajes.md

## Reglas de funcionamiento

- **Todo lo nuevo se guarda aquí.** Cuando cree una skill, un agente, un comando o un dato a recordar,
  va dentro de este repo (ver estructura abajo), nunca solo en `~/.claude` local.
- **Persistir = commit + push a la rama principal.** La rama principal del cerebro es
  `claude/zealous-cray-ira4xc` (no existe `main`). Las sesiones en la nube son efímeras: tras crear o
  cambiar algo del cerebro, haz commit con un mensaje claro y súbelo a la rama principal. Si la sesión
  trabaja en otra rama, haz además `git fetch origin claude/zealous-cray-ira4xc`, integra (rebase) y
  `git push origin HEAD:claude/zealous-cray-ira4xc`. Tengo autorizado ese push. Lo que no llega a la
  rama principal se pierde en la próxima sesión.
- **"Recuerda que…"** → usa la skill `recordar` para guardarlo en `memoria/`.
- **"Crea una skill / agente…"** → usa la skill `crear-herramienta`.
- Idioma por defecto: español.

## Estructura

| Ruta | Qué contiene |
|------|--------------|
| `CLAUDE.md` | Instrucciones globales (este archivo) |
| `memoria/` | Datos que Claude debe recordar entre sesiones |
| `.claude/skills/<nombre>/SKILL.md` | Skills (también se invocan como `/<nombre>`) |
| `.claude/agents/<nombre>.md` | Subagentes especializados |
| `.claude/settings.json` | Permisos, hooks y ajustes compartidos |
| `scripts/instalar-local.sh` | Enlaza el cerebro a `~/.claude` en un equipo local |

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
- **Persistir = commit + push.** Las sesiones en la nube son efímeras: tras crear o cambiar algo del
  cerebro, haz commit con un mensaje claro y `git push` a la rama de trabajo. Si no se sube, se pierde.
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

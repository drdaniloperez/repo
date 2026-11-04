# 🧠 Cerebro de Claude

Mi memoria, skills, agentes y configuración de Claude Code en un solo repositorio,
disponible desde cualquier dispositivo y en las sesiones en la nube.

## Cómo funciona

- **Nube / web / móvil (claude.ai/code):** abre una sesión con este repo. Claude carga
  `CLAUDE.md` (que importa `memoria/`), las skills de `.claude/skills/` y los agentes de `.claude/agents/`.
- **Equipo local:** clona el repo y ejecuta `./scripts/instalar-local.sh` para que todo esté
  disponible en cualquier proyecto. Sincroniza con `git pull`.
- **Lo que crees se guarda aquí:** Claude hace commit + push de cada cambio a la rama principal
  `claude/zealous-cray-ira4xc` para que no se pierda cuando la sesión en la nube termina.

## Uso rápido

| Quiero… | Dile a Claude |
|---|---|
| Que recuerde algo | "Recuerda que…" (skill `recordar`) |
| Crear una skill o agente | "Crea una skill que…" (skill `crear-herramienta`) |

## Herramientas

| Tipo | Nombre | Descripción |
|---|---|---|
| Skill | `recordar` | Guarda datos en `memoria/` y los sube a GitHub |
| Skill | `crear-herramienta` | Crea skills, agentes y ajustes dentro del cerebro |
| Agente | `investigador` | Investiga y devuelve un resumen con evidencia |

## Estructura

```
CLAUDE.md                 instrucciones globales + importa la memoria
memoria/                  perfil, preferencias, aprendizajes
.claude/skills/           skills (una carpeta con SKILL.md cada una)
.claude/agents/           subagentes
.claude/settings.json     permisos y hooks
scripts/instalar-local.sh enlaza todo a ~/.claude en un equipo local
```

> ⚠️ No guardes contraseñas, tokens ni claves en este repo.

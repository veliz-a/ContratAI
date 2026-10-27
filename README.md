# ContratAI
Prototipo Funcional

Asistente conversacional que ayuda a la MYPE peruana a entender las contrataciones públicas: qué oportunidades hay, cómo le ha ido a una entidad contratante y qué situación tiene un proveedor. Responde en lenguaje natural y solo con datos oficiales, citando la fuente y la fecha de corte.

> **Estado:** prototipo funcional en desarrollo, hecho para el curso Tecnologías Emergentes (USIL, 2026-02). Hoy el proyecto está en la fase de inventario de fuentes y herramientas; las secciones que dependen de ese inventario están marcadas como pendientes.

## Qué problema aborda

La información para participar en las contrataciones del Estado existe y es pública, pero está dispersa en varias plataformas y exige conocimiento técnico para interpretarla. ContratAI busca reducir esa brecha con una sola interfaz de preguntas y respuestas.

## Qué es y qué no es

- Es una herramienta de consulta previa a la postulación, de alcance demostrativo.
- No reemplaza al SEACE ni presenta ofertas.
- No emite veredictos sobre empresas ni predice resultados de licitaciones.
- Si el dato no está en sus fuentes, responde que no cuenta con esa información en lugar de inventarla.

## Cómo funciona

Arquitectura RAG (Recuperación Aumentada por Generación): el modelo de lenguaje interpreta la pregunta, se recupera el dato relevante de las fuentes y la respuesta se redacta a partir de ese dato, no del conocimiento interno del modelo.

*Pendiente: detalle de la arquitectura, que se define con los hallazgos del inventario.*

## Fuentes de datos

Candidatas en evaluación (su disponibilidad real se documenta en `fichas_scripts_inventario/`):

- Portal de datos abiertos del OECE (histórico de contrataciones, estándar OCDS)
- Buscador público del SEACE (procesos vigentes)
- Ficha Única del Proveedor y Registro Nacional de Proveedores
- Listado de proveedores sancionados del Tribunal de Contrataciones del Estado

## Limitaciones conocidas

- Los datos tienen una fecha de corte y pueden no reflejar cambios recientes.
- *Pendiente: qué se simula y qué se consulta en vivo, según el inventario.*

## Estructura del repositorio

```
fichas_scripts_inventario/   fichas y scripts de exploración de fuentes y herramientas
  output/                    extractos limitados de la salida de cada script
```

*Se amplía a medida que se construye el prototipo.*

## Cómo ejecutarlo

*Pendiente: se completa cuando exista el prototipo.* Las claves de acceso nunca se suben al repositorio: se configuran con variables de entorno.

## Instalar requirements.txt

```bash
pip install -r requirements.txt

uv pip install -r requirements.txt
```

## Datos y uso responsable

Los datos provienen de portales públicos del Estado peruano; revisa los términos de uso de cada fuente. El repositorio no contiene datos personales de personas naturales.

## Equipo

Grupo 2
# Frente C: Herramientas y modelo

> Copia este archivo por cada herramienta que investigues y renómbralo `C_[herramienta].md`.
> Reemplaza lo que está entre [corchetes] y responde en pocas líneas. Lo que lo demuestra está en el script y en `output/`: no lo copies aquí.
> Una pregunta que no aplica a tu herramienta se responde "no aplica". Si una herramienta no sirve, igual se llena: sirve para compararla con las demás.

## Qué afecta este frente

- El costo y el límite de uso gratuito fijan cuántas pruebas caben antes de la entrega; un modelo más débil inventa más.
- El demo se califica en vivo y también ejecutado por el docente por su cuenta; lo que esa persona necesite para ejecutarlo (cuenta, clave, pasos) condiciona qué herramienta conviene.
- Si el modelo inventa cuando no tiene la información, el asistente puede dar datos falsos, que es el riesgo central del proyecto.
- La forma en que se consulta una tabla (búsqueda por texto o consulta estructurada) define cómo se describe la arquitectura en el informe.
- El tiempo por respuesta decide si una demo en vivo es viable.
- Nunca pongas claves de acceso en la ficha, en el script ni en la salida: el repositorio es público. Usa variables de entorno o los secretos de Colab.

## Herramienta

- Nombre: […]
- Enlace: […]

## Preguntas generales

**¿Qué hace falta para empezar a usarla (cuenta, instalación, clave de API) y se puede compartir con el equipo sin subirlo al repositorio?**

[…]

**¿Cuál es el costo y el límite de uso gratuito? ¿Cuánto cuesta una consulta?**

[…]

**¿Qué tan simple es de montar para un demo?**

[…]

**Para que una persona ajena al equipo (por ejemplo, el docente) ejecute el demo por su cuenta, ¿qué necesita (cuenta, clave de API, otra cosa) y qué opciones hay?** Averigua si se puede compartir, cuántos pasos requiere, cuánto tarda y qué riesgos tiene cada opción.

[…]

## Solo para modelos de lenguaje o herramientas de búsqueda

**¿Cuánto tarda en responder?**

[…]

**Cuando le preguntas algo que no está en la información que le das, ¿admite que no lo sabe o inventa una respuesta?** Pruébalo con un texto corto o una tabla pequeña y tres preguntas: una cuya respuesta está ahí, una cuya respuesta no está y una que invite a inventar.

[…]

**¿Cómo responde preguntas de conteo o promedio sobre una tabla?**

[…]

## Conclusión

**¿La usarías en el prototipo? ¿Por qué?**

[…]

## Bloqueos o hallazgos inesperados

[…]

## Archivos de esta ficha

```
fichas_scripts_inventario/C_[herramienta].md
fichas_scripts_inventario/C_[herramienta].py
fichas_scripts_inventario/output/C_[herramienta].txt
```

`[herramienta]` es el nombre corto de la herramienta, sin espacios ni tildes. La salida se guarda con `python C_[herramienta].py > output/C_[herramienta].txt`; si trabajas en Colab, copia la salida de la celda en ese archivo.

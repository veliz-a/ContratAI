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

# Frente C: Herramientas y modelo

## Herramienta
- Nombre: Groq API (Llama 3.3 70B Versatile)
- Enlace: https://console.groq.com/

## Preguntas generales

**¿Qué hace falta para empezar a usarla (cuenta, instalación, clave de API) y se puede compartir con el equipo sin subirlo al repositorio?**
Solo necesitas crear una cuenta gratis en la consola de Groq sin meter tarjeta y sacar tu clave de API. En Python se instala con pip install groq. La clave nunca se sube a GitHub porque es pública, así que se usa mediante variables de entorno tipo os.environ.

**¿Cuál es el costo y el límite de uso gratuito? ¿Cuánto cuesta una consulta?**
Tiene un nivel gratuito bastante generoso que te da miles de peticiones al día sin pagar nada. Las consultas de prueba salen totalmente gratis.

**¿Qué tan simple es de montar para un demo?**
Es súper fácil porque su estructura es casi idéntica a la de OpenAI y responde al instante gracias a sus chips de procesamiento rápido.

**Para que una persona ajena al equipo (por ejemplo, el docente) ejecute el demo por su cuenta, qué necesita (cuenta, clave de API, otra cosa) y qué opciones hay?**
Solo requiere registrarse gratis en la página de Groq para sacar su propia llave. Puede ponerla como variable de entorno o usar los secretos si lo corre directo en Google Colab.

## Solo para modelos de lenguaje o herramientas de búsqueda

**¿Cuánto tarda en responder?**
Vuela respondiendo, así que la experiencia de chat se siente fluida y natural al instante.

**Cuando le preguntas algo que no está en la información que le das, ¿admite que no lo sabe o inventa una respuesta?**
Si le pones una buena instrucción de sistema que le ponga límites estrictos, el modelo reconoce rápido cuando falta la info y te avisa en lugar de inventar cosas.

**¿Cómo responde preguntas de conteo o promedio sobre una tabla?**
Maneja bien tablas pasadas en texto plano o formato Markdown dentro del mismo texto, aunque para cálculos matemáticos exactos es mejor apoyarse con código de Python aparte.

## Conclusión

**¿La usarías en el prototipo? ¿Por qué?**
Sí la usaría porque te da una velocidad brutal, no te cobra nada para este nivel de pruebas y aguanta perfecto el ritmo de trabajo del equipo.

## Bloqueos o hallazgos inesperados
Al inicio el modelo se confundía un poco y quería mezclar normas de contrataciones de otros países como España o México, así que tocó afinar bien el texto de configuración del sistema para que se centre netamente en las leyes del Perú y el OSCE.
## Archivos de esta ficha

```
fichas_scripts_inventario/C_[herramienta].md
fichas_scripts_inventario/C_[herramienta].py
fichas_scripts_inventario/output/C_[herramienta].txt
```

`[herramienta]` es el nombre corto de la herramienta, sin espacios ni tildes. La salida se guarda con `python C_[herramienta].py > output/C_[herramienta].txt`; si trabajas en Colab, copia la salida de la celda en ese archivo.

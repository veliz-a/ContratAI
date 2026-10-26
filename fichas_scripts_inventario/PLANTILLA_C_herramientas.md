# Frente C: Herramientas y modelo

## Herramienta
- Nombre: Groq API (Llama 3.3 70B Versatile)
- Enlace: https://console.groq.com/

## Preguntas generales

**¿Qué hace falta para empezar a usarla (cuenta, instalación, clave de API) y se puede compartir con el equipo sin subirlo al repositorio?**
Se requiere crear una cuenta gratuita en la consola de Groq y generar la clave de API correspondiente. En el entorno de desarrollo se instala mediante el comando pip install groq. La llave de acceso no debe subirse al repositorio público por motivos de seguridad, por lo que se gestiona mediante variables de entorno con os.environ.

**¿Cuál es el costo y el límite de uso gratuito? ¿Cuánto cuesta una consulta?**
Dispone de un nivel gratuito adecuado para fases de prueba y prototipado con un límite amplio de solicitudes por minuto. Las consultas de validación inicial no generan costos monetarios.

**¿Qué tan simple es de montar para un demo?**
Su implementación resulta directa debido a que su estructura de código es compatible con los estándares de la industria, facilitando la integración rápida en el proyecto.

**Para que una persona ajena al equipo (por ejemplo, el docente) ejecute el demo por su cuenta, qué necesita (cuenta, clave de API, otra cosa) y qué opciones hay?**
Solo necesita registrarse de forma gratuita en la plataforma de Groq para obtener su propia clave de autenticación. Esta puede configurarse como variable de entorno o incorporarse mediante los secretos de Google Colab si se ejecuta de manera remota.

## Solo para modelos de lenguaje o herramientas de búsqueda

**¿Cuánto tarda en responder?**
Presenta tiempos de respuesta muy bajos, lo cual permite que la interacción del chat se mantenga fluida y en tiempo real.

**Cuando le preguntas algo que no está en la información que le das, ¿admite que no lo sabe o inventa una respuesta?**
Mediante el uso de un prompt de sistema que establezca directrices estrictas, el modelo logra identificar los vacíos de información y señala la ausencia de datos en lugar de generar respuestas especulativas.

**¿Cómo responde preguntas de conteo o promedio sobre una tabla?**
Procesa de manera adecuada estructuras tabulares en texto plano o formato Markdown dentro del contexto, aunque para operaciones numéricas complejas se recomienda respaldar el proceso con scripts de Python.

## Conclusión

**¿La usarías en el prototipo? ¿Por qué?**
Sí se seleccionaría para el prototipo porque ofrece un rendimiento óptimo en velocidad, un esquema gratuito viable para la etapa académica y estabilidad ante las solicitudes del equipo.

## Bloqueos o hallazgos inesperados
En las primeras pruebas el modelo tendía a generalizar con normativas de contrataciones de otros países, lo cual requirió ajustar con mayor precisión el prompt del sistema para restringir el análisis estrictamente al marco legal del Estado peruano y del OSCE.

## Archivos de esta ficha

```
fichas_scripts_inventario/C_[herramienta].md
fichas_scripts_inventario/C_[herramienta].py
fichas_scripts_inventario/output/C_[herramienta].txt
```

`[herramienta]` es el nombre corto de la herramienta, sin espacios ni tildes. La salida se guarda con `python C_[herramienta].py > output/C_[herramienta].txt`; si trabajas en Colab, copia la salida de la celda en ese archivo.

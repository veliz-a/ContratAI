# Frente A: Datos de contrataciones

## Fuente

- **Nombre:** Sistema Electrónico de Contrataciones del Estado (SEACE).
- **Enlace:** https://www.gob.pe/7505-consultar-los-buscadores-publicos-del-sistema-electronico-de-contrataciones-del-estado-seace

## Preguntas

**1. ¿En qué estado se encuentra para usarla en el prototipo?**

La fuente se encuentra disponible para consulta pública. Se logró descargar y analizar un archivo Excel con 499 procedimientos de selección de 2026. Es una fuente candidata para el prototipo ContratAI.

**2. ¿Se obtiene de forma automática (descarga o API) o solo a mano? ¿Hay límites o términos de uso?**

Los datos se pueden consultar y descargar manualmente en formato Excel (.xls), sin necesidad de iniciar sesión. Todavía no se ha comprobado la disponibilidad de una API pública ni los límites de descarga o condiciones específicas para automatizar su uso.

**3. ¿Qué campos trae y cuáles faltan para las preguntas del Frente D?**

El archivo contiene 10 columnas, incluyendo entidad pública, fecha de publicación, nomenclatura, objeto de contratación, descripción, cuantía, moneda y versión SEACE. Faltan datos detallados sobre proveedores adjudicados, pagos, penalidades y cumplimiento contractual. La utilidad exacta para el Frente D depende de las preguntas que se definan allí.

**4. ¿Incluye la ejecución del contrato (plazos, pagos, penalidades) o solo convocatoria y adjudicación?**

El archivo analizado contiene información de procedimientos de selección. No incluye campos específicos sobre pagos, penalidades o cumplimiento de plazos contractuales. Para analizar la ejecución de contratos sería necesario consultar otras fuentes.

**5. ¿Incluye procesos vigentes o solo cerrados?**

El buscador permite consultar procedimientos publicados durante 2026. La muestra contiene publicaciones recientes, pero el archivo descargado no incluye una columna que permita identificar directamente cuáles siguen vigentes o están cerrados.

**6. ¿Cuántos registros tiene, qué período cubre y cada cuánto se actualiza?**

El archivo descargado contiene 499 registros y 10 columnas. Se obtuvo mediante una consulta del año 2026 realizada el 26 de octubre de 2026. El portal muestra información reciente, pero todavía no se ha verificado su frecuencia oficial de actualización.

**7. ¿Qué tan limpio está (vacíos, duplicados, nombres escritos de varias formas)?**

El análisis con Python encontró 0 filas duplicadas exactas. La columna "Reiniciado Desde" presenta 478 valores vacíos, mientras que las otras 9 columnas no presentan valores nulos. Todavía falta revisar posibles diferencias en la escritura de los nombres de entidades y la validez de los montos registrados.

## Bloqueos o hallazgos inesperados

- Se confirmó que el buscador público permite exportar resultados en formato Excel antiguo (.xls).
- El archivo se pudo procesar correctamente utilizando Python, pandas y xlrd.
- No se ha comprobado una API pública para realizar consultas automáticas.
- El archivo no contiene información detallada sobre ejecución contractual.
- Los 499 registros corresponden a la búsqueda realizada y no representan necesariamente todos los procedimientos de 2026.

## Archivos de esta ficha

```text
fichas_scripts_inventario/A_seace.md
fichas_scripts_inventario/A_seace.py
fichas_scripts_inventario/output/A_seace.txt
```
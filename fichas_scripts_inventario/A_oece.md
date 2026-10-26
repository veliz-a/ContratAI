# Frente A: Datos de contrataciones

## Fuente

- **Nombre:** Portal de Datos Abiertos del OECE
- **Enlace:** https://www.gob.pe/es/14272-acceder-al-portal-de-datos-abiertos-del-oece

## Preguntas

**1. ¿En qué estado se encuentra para usarla en el prototipo?**

La fuente se encuentra disponible públicamente y permite descargar información sobre contrataciones del Estado peruano. Es una fuente candidata para ContratAI, pero todavía falta descargar una muestra, analizar su estructura y comprobar su integración con el prototipo.

**2. ¿Se obtiene de forma automática (descarga o API) o solo a mano? ¿Hay límites o términos de uso?**

Los datos se pueden descargar desde el portal oficial. También existe una publicación de contrataciones abiertas en formatos CSV, JSON y Excel, bajo licencia CC BY 4.0. No se ha comprobado todavía el funcionamiento de una API ni sus posibles límites de consulta.

**3. ¿Qué campos trae y cuáles faltan para las preguntas del Frente D?**

El portal contiene información sobre convocatorias, adjudicaciones, proveedores, entidades contratantes y contratos. Para identificar los campos exactos se necesita revisar los diccionarios de datos y descargar una muestra. También falta contrastarlos con las preguntas específicas del Frente D.

**4. ¿Incluye la ejecución del contrato (plazos, pagos, penalidades) o solo convocatoria y adjudicación?**

No se limita a convocatorias y adjudicaciones, porque también ofrece información de contratos y conjuntos relacionados con sanciones y penalidades. Sin embargo, todavía debemos comprobar si contiene datos completos de plazos, pagos y cumplimiento contractual.

**5. ¿Incluye procesos vigentes o solo cerrados?**

El portal de datos abiertos tradicional no incluye procedimientos de selección en marcha ni adjudicaciones incompletas. Por lo tanto, no debe utilizarse como única fuente para consultar procesos vigentes.

**6. ¿Cuántos registros tiene, qué período cubre y cada cuánto se actualiza?**

El portal tradicional contiene información desde 2018 y se actualiza mensualmente, durante los primeros cinco días de cada mes. La cantidad exacta de registros todavía está pendiente de medición mediante un script de Python.

**7. ¿Qué tan limpio está (vacíos, duplicados, nombres escritos de varias formas)?**

Todavía no se ha medido la calidad de una muestra descargada. En la publicación de contrataciones abiertas se han documentado identificadores duplicados, contratos sin estado y relaciones incompletas entre adjudicaciones y contratos. Será necesario comprobar estos problemas en los datos seleccionados.

## Bloqueos o hallazgos inesperados

- Los datos abiertos tradicionales no incluyen todos los procesos en marcha.
- Es necesario comprobar qué información contractual está realmente disponible.
- Todavía no se ha verificado una API para consultas automáticas.
- Falta descargar una muestra y medir registros vacíos y duplicados.
- La publicación de contrataciones abiertas tiene una cobertura y condiciones de actualización diferentes del portal tradicional.

## Archivos de esta ficha

- `fichas_scripts_inventario/A_oece.md`
- `fichas_scripts_inventario/A_oece.py`
- `fichas_scripts_inventario/output/A_oece.txt`

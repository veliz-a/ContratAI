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

Se analizó el archivo de adjudicaciones del OECE correspondiente a 2025, que contiene 25 columnas. Entre los campos disponibles se encuentran la entidad contratante, RUC de la entidad, código de convocatoria, tipo de procedimiento, descripción del proceso, proveedor adjudicado, RUC del proveedor, monto referencial, monto adjudicado, estado del ítem y fechas de convocatoria y buena pro.

Estos campos permiten responder consultas sobre adjudicaciones y proveedores. Sin embargo, el archivo no presenta columnas específicas sobre pagos efectuados, penalidades o avance de ejecución contractual. Queda pendiente comparar estos campos con las preguntas del Frente D.

**4. ¿Incluye la ejecución del contrato (plazos, pagos, penalidades) o solo convocatoria y adjudicación?**

No se limita a convocatorias y adjudicaciones, porque también ofrece información de contratos y conjuntos relacionados con sanciones y penalidades. Sin embargo, todavía debemos comprobar si contiene datos completos de plazos, pagos y cumplimiento contractual.

**5. ¿Incluye procesos vigentes o solo cerrados?**

El portal de datos abiertos tradicional no incluye procedimientos de selección en marcha ni adjudicaciones incompletas. Por lo tanto, no debe utilizarse como única fuente para consultar procesos vigentes.

**6. ¿Cuántos registros tiene, qué período cubre y cada cuánto se actualiza?**

El archivo CONOSCE_ADJUDICACIONES2025_0.xlsx, correspondiente al año 2025, contiene 45,620 registros y 25 columnas, según el análisis realizado con Python y pandas.

El Portal de Datos Abiertos del OECE ofrece información desde 2018 y señala que se actualiza mensualmente durante los primeros cinco días de cada mes. La página consultada indicaba una actualización al 30 de septiembre de 2026.

El conteo obtenido corresponde únicamente al archivo analizado de adjudicaciones de 2025, no a la totalidad de registros disponibles en el portal.

**7. ¿Qué tan limpio está (vacíos, duplicados, nombres escritos de varias formas)?**

Se analizaron 45,620 registros mediante Python y pandas. No se encontraron filas completamente duplicadas.

Se identificaron los siguientes valores vacíos:

FECHA_CONSENTIMIENTO_BP: 573 registros.

DEPARTAMENTO_ITEM: 204 registros.

FECHA_BUENAPRO: 16 registros.

MONTO_REFERENCIAL_ITEM_SOLES: 1 registro.

Las demás columnas no presentaron valores vacíos.

Los resultados muestran una baja proporción de datos faltantes. Sin embargo, todavía es necesario comprobar posibles inconsistencias en nombres de entidades y proveedores, además de duplicados basados en identificadores específicos.

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

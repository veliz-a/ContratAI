# Frente A: Datos de contrataciones

> Copia este archivo por cada fuente que revises y renómbralo `A_[fuente].md`.
> Reemplaza lo que está entre [corchetes] y responde en pocas líneas. Lo que lo demuestra está en el script y en `output/`: no lo copies aquí.
> Si una fuente no sirve, igual se llena: un "no disponible" bien explicado es un hallazgo.

## Qué afecta este frente

- Si el dato se obtiene de forma automática o solo a mano, define si el prototipo consulta en vivo o trabaja con una muestra, y el informe debe declararlo.
- Los campos disponibles definen qué preguntas del Frente D se pueden responder.
- Si hay datos de ejecución del contrato (plazos, pagos, penalidades), el asistente puede hablar de cumplimiento; si no, solo de convocatorias y adjudicaciones.
- El tamaño y el período definen si el demo usa todo el histórico o una muestra.
- No subas al repositorio datos personales ni archivos pesados: guarda en `output/` solo la salida del script (conteos, columnas, muestras de pocas filas).

## Fuente

- Nombre: […]
- Enlace: […]

## Preguntas

**¿En qué estado se encuentra para usarla en el prototipo?**

[…]

**¿Se obtiene de forma automática (descarga o API) o solo a mano? ¿Hay límites o términos de uso?**

[…]

**¿Qué campos trae y cuáles faltan para las preguntas del Frente D?**

[…]

**¿Incluye la ejecución del contrato (plazos, pagos, penalidades) o solo convocatoria y adjudicación?**

[…]

**¿Incluye procesos vigentes o solo cerrados?**

[…]

**¿Cuántos registros tiene, qué período cubre y cada cuánto se actualiza?**

[…]

**¿Qué tan limpio está (vacíos, duplicados, nombres escritos de varias formas)?**

[…]

## Bloqueos o hallazgos inesperados

[…]

## Archivos de esta ficha

```
fichas_scripts_inventario/A_[fuente].md
fichas_scripts_inventario/A_[fuente].py
fichas_scripts_inventario/output/A_[fuente].txt
```

`[fuente]` es el nombre corto de la fuente, sin espacios ni tildes. La salida se guarda con `python A_[fuente].py > output/A_[fuente].txt`; si trabajas en Colab, copia la salida de la celda en ese archivo.

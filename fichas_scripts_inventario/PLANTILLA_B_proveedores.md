# Frente B: Proveedores y riesgo

> Copia este archivo por cada fuente que revises y renómbralo `B_[fuente].md`.
> Reemplaza lo que está entre [corchetes] y responde en pocas líneas. Lo que lo demuestra está en el script y en `output/`: no lo copies aquí.
> Si una fuente no sirve, igual se llena: un "no disponible" bien explicado es un hallazgo.

## Qué afecta este frente

- Si un proveedor se consulta de forma automática o solo a mano, define cuántos proveedores puede cubrir el demo.
- Lo que la fuente devuelva (situación tributaria, experiencia, sanciones) es lo único que el asistente podrá afirmar sobre un proveedor.
- La fecha de corte obliga al asistente a decir "según datos al [fecha]"; una sanción reciente puede no aparecer todavía.
- Sin un identificador común entre fuentes (por ejemplo el RUC), no se pueden cruzar contratos con sanciones.
- No uses datos de personas naturales (socios, representantes) en pruebas, scripts ni salidas: el repositorio es público. Usa empresas.

## Fuente

- Nombre: […]
- Enlace: […]

## Preguntas

**¿En qué estado se encuentra para usarla en el prototipo?**

[…]

**¿Se consulta de forma automática o solo a mano? ¿Hay límites de descarga o términos de uso?**

[…]

**¿Qué devuelve por proveedor y qué no?**

[…]

**¿Se puede descargar el listado completo o solo se consulta de uno en uno?**

[…]

**¿Cuál es la fecha de corte y cada cuánto se actualiza?**

[…]

**¿Qué identificador usa y coincide con el de las fuentes del Frente A? ¿Cuántos proveedores coinciden?**

[…]

## Bloqueos o hallazgos inesperados

[…]

## Archivos de esta ficha

```
fichas_scripts_inventario/B_[fuente].md
fichas_scripts_inventario/B_[fuente].py
fichas_scripts_inventario/output/B_[fuente].txt
```

`[fuente]` es el nombre corto de la fuente, sin espacios ni tildes. La salida se guarda con `python B_[fuente].py > output/B_[fuente].txt`; si trabajas en Colab, copia la salida de la celda en ese archivo.

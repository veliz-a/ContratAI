# Frente B: Proveedores y riesgo

## Fuente

- **Nombre:** Buscador de Proveedores del Estado (OECE)
- **Enlace:** https://apps.oece.gob.pe/perfilprov-ui/buscar
- **Servicio de datos usado por la página:** https://eap.oece.gob.pe/perfilprov-bus/1.0/tarjetas

## Preguntas

**¿En qué estado se encuentra para usarla en el prototipo?**

Se puede usar. Al consultarla desde un script, la fuente respondió con éxito (código 200) y entregó datos ordenados en formato JSON, sin pedir usuario, clave ni captcha. Cada respuesta incluye la fecha de los datos y la cantidad de resultados, lo que facilita citar la fuente.

Advertencia: el servicio que usamos es el que la propia página consulta por detrás, no una interfaz publicada oficialmente para desarrolladores. Por eso podría cambiar sin aviso, y conviene guardar un extracto con su fecha como respaldo para la demostración.

**¿Se consulta de forma automática o solo a mano? ¿Hay límites de descarga o términos de uso?**

Se consulta de forma automática. Probamos pedir 10, 100, 500 y hasta 1000 proveedores por consulta, y la fuente devolvió siempre exactamente esa cantidad, así que no encontramos un límite técnico, aunque no probamos cifras mayores. Las pruebas se hicieron con pausas de un segundo entre consultas.

También comprobamos que el parámetro de exportación a Excel no cambia la respuesta: el resultado es idéntico con y sin él, por lo que no hace falta.

Términos de uso: no se evaluaron en estas pruebas y quedan por revisar en el sitio.

**¿Qué devuelve por proveedor y qué no?**

- **Devuelve:** RUC y razón social, si está habilitada, si es apta para contratar con el Estado, sus tipos de registro vigentes y su último contrato (tipo, entidad contratante y monto).
- **No devuelve:** sanciones, situación tributaria, experiencia ni la lista completa de contratos.
- Los campos de suspensión temporal y fecha de término vinieron vacíos en todas las pruebas.

Un caso muestra por qué importa: Oxígeno Santa Clara figura como habilitada pero no apta, con tipo de registro vacío. "No apto" no equivale entonces a "sancionado", y el asistente no debe presentarlo así.

**¿Se puede descargar el listado completo o solo se consulta de uno en uno?**

No hay un archivo único con todos los proveedores: se busca por RUC, nombre o rubro y los resultados llegan por páginas. Buscar un RUC devolvió un solo resultado, mientras que la palabra "oxigeno" devolvió 7178 coincidencias, que se recorren en 8 páginas de 1000.

Esto permite consultar muchos proveedores sin hacerlo uno por uno, pero no probamos recorrer todo el universo ni sabemos cuántos proveedores existen en total. Para el prototipo, lo más práctico sería consultar por RUC cada vez que el usuario pregunte por una empresa concreta.

**¿Cuál es la fecha de corte y cada cuánto se actualiza?**

Cada respuesta trae su propia fecha de corte, que en nuestra prueba fue el 25/10/2026, así que el asistente puede decir con respaldo "según datos al 25/10/2026". Hay que evitar la fecha técnica que mostró la página web (14/10/2026), porque corresponde al diseño de la página y no a los datos.

No sabemos cada cuánto se actualiza: la prueba hecha el 26/10 mostró datos del día anterior, lo que sugiere una actualización diaria, pero es una sola observación. Para confirmarlo, habría que repetir la consulta otro día y comparar la fecha.

**¿Qué identificador usa y coincide con el de las fuentes del Frente A? ¿Cuántos proveedores coinciden?**

Usa el RUC de 11 dígitos.

- **Coincidencia con el Frente A:** no medida, porque no hay datos de ese frente con los cuales cruzar.
- **Proveedores que coinciden con el Frente A:**

Como alternativa, cruzamos esta fuente con la de sancionados (ver `B_sancionadosTCE.md`): consultamos una por una las 46 empresas sancionadas de la muestra y las 46 aparecen en el buscador del OECE. Las 46 figuran como no habilitadas y no aptas para contratar. Es una buena señal de que ambas fuentes son coherentes entre sí y se pueden unir por RUC.

## Bloqueos o hallazgos inesperados

- La dirección de la página no sirve para un script. Al intentar leerla, Python rechazó el certificado de seguridad del servidor, y al desactivar esa verificación devolvió siempre la misma página en blanco (1789 bytes), sin importar si se buscaba un RUC o una palabra.
- Los datos reales están en otra dirección (eap.oece.gob.pe), cuyo certificado sí es válido y que responde sin problemas.
- Lo más importante para el asistente es no presentar "no apto" como "sancionado", porque el caso observado muestra que puede haber otras causas.

## Pendientes y observaciones manuales

Lo siguiente no salió de los scripts y queda por completar a mano:

- **Términos de uso:**

## Archivos de esta ficha

- `fichas_scripts_inventario/B_fichaproveedor.md`
- `fichas_scripts_inventario/B_fichaproveedor.py`
- `fichas_scripts_inventario/output/B_fichaproveedor.txt`

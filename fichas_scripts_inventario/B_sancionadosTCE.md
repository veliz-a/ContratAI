# Frente B: Proveedores y riesgo

## Fuente

- **Nombre:** Relación de proveedores sancionados por el Tribunal de Contrataciones Públicas (TCE) en los últimos cinco años
- **Enlace:** https://www.rnp.gob.pe/consultasenlinea/inhabilitados/busqueda_vnv.asp

## Preguntas

**¿En qué estado se encuentra para usarla en el prototipo?**

Se puede usar solo en parte. La página entregó, sin resolver ningún captcha, una tabla de 200 sanciones con RUC, que sirve como muestra de lo más reciente pero no como historial completo.

Sospechamos que 200 es un tope de la página: es una cifra redonda y la sanción más antigua de la tabla es del 04/04/2024, aunque el portal dice cubrir cinco años. Es solo una sospecha que no pudimos confirmar. Para un prototipo demostrativo alcanza, siempre que se diga con claridad que es una muestra.

**¿Se consulta de forma automática o solo a mano? ¿Hay límites de descarga o términos de uso?**

Es un caso mixto. Con un script se puede leer la página inicial y obtener la tabla de 200 sanciones, pero la página incluye un captcha ("ingrese el código de la imagen") junto a sus opciones de búsqueda, y no intentamos resolverlo ni evadirlo. Eso significa que, por la vía automática, solo contamos con lo que la página entrega abierta.

Términos de uso: no se evaluaron en estas pruebas y quedan por revisar. Que la tabla inicial sea accesible no equivale a una autorización para uso automatizado.

**¿Qué devuelve por proveedor y qué no?**

- **Devuelve (por sanción):** razón social, RUC, resolución, periodo de inhabilitación, fechas desde y hasta, infracción, otra infracción, norma y estado.
- **No devuelve:** situación tributaria ni contratos.

De las 200 filas con RUC, 81 son de empresas, que corresponden a 46 empresas distintas (algunas con varias sanciones), y 117 son de personas naturales. Como el repositorio es público, los scripts solo muestran empresas y, de las personas, únicamente cuentan cuántas hay.

Al citar una sanción, el asistente debería indicar siempre la resolución y la norma.

**¿Se puede descargar el listado completo o solo se consulta de uno en uno?**

No pudimos obtener el listado completo de forma automática. Lo que entrega la página es una muestra de 200 sanciones, que va de la más reciente (14/10/2026) a la más antigua de la muestra (04/04/2024). Conseguir los cinco años completos exigiría usar las consultas protegidas por captcha, algo que no vamos a automatizar.

Además, la página contiene una segunda tabla (101 filas por 15 columnas) que no analizamos y queda como pendiente. Por ahora, la muestra de 200 es lo único que podemos afirmar con respaldo.

**¿Cuál es la fecha de corte y cada cuánto se actualiza?**

La página no entrega una fecha de corte oficial. Lo único que tenemos como referencia es que la sanción más reciente de la tabla es del 14/10/2026. Por eso el asistente no puede decir "según datos al [fecha]" con rigor: solo podría decir "sanciones registradas hasta el 14/10/2026, la última visible". Una sanción posterior podría no aparecer todavía.

Tampoco sabemos con qué frecuencia se actualiza esta fuente, así que eso queda pendiente de confirmar con otra consulta en un día distinto.

**¿Qué identificador usa y coincide con el de las fuentes del Frente A? ¿Cuántos proveedores coinciden?**

Usa el RUC de 11 dígitos, con empresas (que empiezan con 20) y personas naturales (con 10) mezcladas.

- **Coincidencia con el Frente A:** no medida.
- **Proveedores que coinciden con el Frente A:**

El cruce con el OECE (ver `B_fichaproveedor.md`) funcionó en las 46 empresas, pero hay que leerlo con cuidado: la muestra es pequeña y reciente, y solo comprobamos un sentido, que sancionado implica no apto. No podemos afirmar lo contrario, porque ya vimos un proveedor no apto con tipo de registro vacío sin que aparezca entre los sancionados de la muestra.

## Bloqueos o hallazgos inesperados

- El principal obstáculo es el captcha presente en la página, que no intentamos resolver.
- Como la tabla disponible es una muestra de 200 sanciones, que un proveedor no aparezca no prueba que esté limpio: el asistente debe responder "no figura en la muestra consultada" y nunca "no tiene sanciones".
- La tabla mezcla empresas y personas naturales, por lo que todo lo que se muestre o guarde debe filtrarse a empresas para respetar que el repositorio es público.
- La segunda tabla de la página (101 filas por 15 columnas) no se analizó.

## Pendientes y observaciones manuales

Lo siguiente no salió de los scripts y queda por completar a mano:

- **Términos de uso:**
- **Comportamiento del botón "Listar todos":**
- **Detalle del botón Excel:**
- **Contenido de la segunda tabla (101 × 15):**

## Archivos de esta ficha

- `fichas_scripts_inventario/B_sancionadosTCE.md`
- `fichas_scripts_inventario/B_sancionadosTCE.py`
- `fichas_scripts_inventario/output/B_sancionadosTCE.txt`

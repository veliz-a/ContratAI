# Frente D: Preguntas y criterios

**ContratAI** · Grupo 2 · Tecnologías Emergentes · Corte: 26-10-2026

ContratAI es un asistente conversacional que orienta a la MYPE peruana sobre las contrataciones públicas: qué oportunidades hay, cómo le ha ido a una entidad contratante y qué situación tiene un proveedor. Este documento define qué preguntas debe atender, cómo reconocemos una buena respuesta y qué queda fuera de su alcance.

## 1. Cómo responde ContratAI

| Nivel | Qué entrega | Ejemplo (cifras ilustrativas) |
| --- | --- | --- |
| Dato | Lo registrado en la fuente, con fecha de corte. | "En [periodo], [entidad] adjudicó [N] ítems de útiles de oficina." |
| Indicador | Un dato agregado con su método a la vista: qué se agrupó, periodo y cobertura. | "[X]% del monto fue a los 3 mayores proveedores; la adjudicación quedó en promedio [Y]% bajo el valor referencial." |
| Orientación | La lectura de los indicadores en lenguaje accionable, comparativa y condicional, con sus supuestos. | "El mercado de este rubro en esta entidad parece [concentrado/abierto]. Esto no considera tus costos ni la competencia de este proceso." |

**Regla de diseño:** toda orientación muestra los indicadores en que se apoya, con su fuente, fecha de corte y cobertura. ContratAI no emite veredictos ("debes presentarte") ni probabilidades individuales ("tienes 70 % de ganar").

## 2. Preguntas de una MYPE

**Cobertura:** *Cubierta* (hay dato para responder) · *Parcial* · *Por explorar* · *Sin dato* · *Pendiente* (depende de otro frente).

| N.º | Pregunta | Frente | Nivel | Fuente de datos | Cobertura | Nota |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ¿Hay procesos publicados para vender útiles de oficina? | Mercado | Dato | Export del SEACE | Parcial | Informa lo publicado, no si sigue abierto; el rubro se empareja por texto |
| 2 | ¿Qué piensa comprar el hospital de mi provincia este año? | Mercado | Dato | Plan Anual de Contrataciones | Por explorar | Aún no explorado |
| 3 | ¿Con cuánta rebaja suelen ganar en este tipo de compra? | Mercado | Indicador | Adjudicaciones OECE | Cubierta | Monto adjudicado frente a valor referencial, por ítem |
| 4 | ¿Quién domina este rubro y qué tan fácil es entrar? | Mercado | Orientación | Adjudicaciones OECE (varios años) | Parcial | Concentración y rotación de ganadores |
| 5 | ¿Qué tan difícil es ganar en este rubro con esta entidad? | Mercado | Orientación | Adjudicaciones y ofertantes | Por explorar | Requiere el listado de ofertantes |
| 6 | ¿Me conviene presentarme a este proceso? | Mercado y perfil | Orientación | Indicadores 3 a 5 y contexto de la MYPE | Por explorar | Orientación comparativa, sin veredicto |
| 7 | ¿Cuánto le ha adjudicado esta municipalidad por este tipo de servicio? | Entidad | Indicador | Adjudicaciones OECE | Cubierta | Es monto adjudicado, no pagado |
| 8 | ¿A cuántos proveedores les compró esta entidad el año pasado? | Entidad | Indicador | Adjudicaciones OECE | Cubierta | Se cuentan proveedores distintos (RUC) |
| 9 | ¿Esta entidad suele declarar desiertos sus procesos? | Entidad | Indicador | Adjudicaciones o conjunto de desiertos | Por explorar | Falta confirmar el campo de estado |
| 10 | ¿Esta entidad me paga a tiempo? | Entidad | — | Ninguna | Sin dato | Las fuentes no traen pagos |
| 11 | ¿Esta empresa está sancionada o inhabilitada? | Contraparte | Dato | Registro de inhabilitados | Pendiente | Depende del frente B |
| 12 | ¿Con qué entidades ha trabajado este proveedor y por qué montos? | Contraparte | Indicador | Adjudicaciones OECE | Cubierta | Son adjudicaciones, no ejecución contractual |
| 13 | De esos procesos, ¿cuáles son de mi rubro? | Perfil propio | Dato y contexto | Export del SEACE y datos de la MYPE | Por explorar | Falta definir qué contexto aporta la MYPE |
| 14 | ¿Qué necesito para inscribirme como proveedor del Estado? | Normativa | Dato | Ley 32069, Reglamento y portal del RNP | Sin dato | Requiere cargar el texto de la norma |

Las preguntas fueron formuladas por el equipo. Su validación con documentos públicos y consultas a MYPE está en curso.

## 3. Respuestas válidas y no válidas

Cada fila es un caso de prueba para el asistente. La lista crece a medida que aparecen casos nuevos.

**Respuestas válidas**

| Caso | Cómo lo reconocemos |
| --- | --- |
| Respuesta completa y correcta | Coincide con la fuente, cita fuente y fecha de corte, y declara periodo y cobertura. |
| Indicador con método a la vista | Muestra qué agrupó, el periodo y la cantidad de registros; distingue adjudicado, referencial y pagado. |
| Orientación basada en indicadores | Presenta la lectura junto a los indicadores que la sustentan, de forma comparativa y condicional, con supuestos y límites. |
| Orientación que reconoce base insuficiente | Si hay pocos registros o falta un dato clave, lo dice y reduce el alcance de la lectura. |
| Respuesta que indica que no cuenta con la información | Señala qué fuente y cuántos registros consultó y que el dato no figura en ellos; no afirma que "no existe". |
| Respuesta parcial | Entrega lo verificable y dice qué parte no puede responder. |
| Oportunidad con estado y vía de verificación | "Publicado el [fecha], según la carga al [corte]; verifícalo en el SEACE", e indica si la coincidencia con el rubro es exacta o estimada. |
| Rechazo de lo que no puede sustentar | Para pagos, normativa sin texto cargado o asesoría legal, explica por qué y remite a la fuente oficial o a un profesional. |
| Reconocimiento de nombres | Responde igual si el usuario dice "OSCE" u "OECE". |

**Respuestas no válidas**

| Caso | Cómo lo reconocemos |
| --- | --- |
| Inventa un dato | El valor, norma, institución o requisito no aparece en ninguna fuente cargada. |
| Responde sobre normativa sin respaldo | Enumera requisitos o leyes sin citar el texto que los sustenta. |
| Orienta sin mostrar indicadores | Dice "te conviene" o "es un buen mercado" sin cifras ni método. |
| Emite veredicto o probabilidad individual | "Debes presentarte", "tienes 70 % de ganar". |
| Generaliza desde pocos registros o datos parciales | Saca una tendencia de una muestra pequeña, o dice "no hay procesos de X" con un export que no es el universo. |
| Extrapola a otra entidad, rubro o periodo | Aplica un indicador calculado para un caso a otro sin decirlo. |
| Responde sin fuente o sin fecha de corte | Falta la cita o la fecha. |
| Atribuye a la fuente algo que no dice | La cita existe, pero el dato no coincide con su contenido. |
| Presenta un dato vencido como vigente | Informa una sanción, norma o proceso fuera de su ventana temporal sin advertirlo. |
| Aplica la norma equivocada | Cita la Ley 30225 para un proceso bajo la Ley 32069, o al revés, sin distinguir. |
| Convierte adjudicado o referencial en pagado | Dice "pagó" con datos de adjudicación. |
| Cuenta filas como procesos o proveedores | La cifra coincide con el número de filas y no con procesos o RUC distintos. |
| Afirma que un proceso está abierto sin respaldo | Usa "abierto" o "vigente" cuando la fuente solo trae fecha de publicación. |
| Etiqueta a un proveedor o entidad | Usa "poco confiable", "riesgoso" o "corrupta" en lugar de reportar indicadores y registros. |
| Usa fuentes no oficiales sin declararlo | La fuente no es oficial y no lo advierte. |
| Confunde homónimos o RUC | Atribuye datos a un proveedor distinto del consultado. |
| Mezcla contexto de la MYPE con dato oficial | No distingue lo que declaró la MYPE de lo que dice la fuente. |

## 4. Alcance y límites

| Consulta que queda fuera | Por qué |
| --- | --- |
| Veredictos ("debes presentarte") | La orientación se apoya en indicadores agregados; la decisión es de la MYPE. |
| Probabilidad individual de ganar | Requiere las ofertas de los competidores y los costos de la MYPE, que no se tienen. |
| Asesoría legal o tributaria personalizada | Requiere un profesional. |
| Calificaciones sobre un proveedor o entidad | Se entregan indicadores y registros, no etiquetas; evita riesgos de difamación y de uso indebido de datos personales. |
| Pagos, penalidades y puntualidad de pago | Ninguna de las fuentes analizadas los trae. |
| Estado actual de un proceso (abierto, cerrado) | El export del SEACE no lo trae y los datos abiertos excluyen procesos en marcha; se informa lo publicado con vía de verificación. |
| Afirmar que no existen procesos de un rubro | El export es el resultado de una búsqueda, no el universo de 2026. |
| Orientación con pocos registros | Por debajo de un mínimo definido en la exploración, se informa el dato sin interpretarlo. |
| Contrataciones fuera del SEACE o del régimen general | No están en las fuentes analizadas. |
| Datos fuera de la cobertura cargada | Cada fuente cubre periodos distintos. |
| Requisitos y trámites normativos, mientras no se cargue la norma | Sin el texto de la norma, el asistente tiende a inventar. |
| Datos de personas naturales más allá de lo publicado oficialmente | Protección de datos personales (Ley 29733). |

## 5. Hallazgos que condicionan el alcance

1. **Procesos abiertos:** los datos abiertos del OECE excluyen procesos en marcha, y el export del SEACE no indica estado. ContratAI informa lo publicado y remite al SEACE para confirmarlo.
2. **Competencia:** las adjudicaciones solo muestran a quienes ganaron. Medir qué tan difícil es ganar requiere el listado de ofertantes, aún por explorar.
3. **Adjudicado no es pagado**, y cada fila de adjudicaciones es un ítem. Los indicadores se calculan por proceso o RUC distintos.
4. **Los números los calcula código**, y el modelo solo redacta la lectura.
5. **Origen de las preguntas:** formuladas por el equipo; en proceso de validación con documentos públicos y consultas a MYPE.

El detalle de estos hallazgos está en la review de la primera semana de exploración.

## Referencias

- Portal de Datos Abiertos del OECE: https://www.gob.pe/14272-acceder-al-portal-de-datos-abiertos-del-oece
- Portal de Contrataciones Abiertas: https://contratacionesabiertas.osce.gob.pe/
- Ley 32069, Ley General de Contrataciones Públicas, y su Reglamento (D.S. 009-2025-EF): https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=25
- Repositorio del proyecto: https://github.com/veliz-a/ContratAI

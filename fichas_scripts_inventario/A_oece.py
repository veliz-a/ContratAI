
import pandas as pd
from pathlib import Path

# Ubicacion de los archivos
carpeta = Path(__file__).resolve().parent
archivo = carpeta / "datos" / "CONOSCE_ADJUDICACIONES2025_0.xlsx"
salida = carpeta / "output" / "A_oece.txt"

print("Iniciando analisis de datos del OECE...")

try:
    # Leer el archivo Excel
    datos = pd.read_excel(archivo)

    # Obtener informacion general
    filas = len(datos)
    columnas = len(datos.columns)
    vacios = datos.isnull().sum()
    duplicados = datos.duplicated().sum()

    # Preparar el reporte
    reporte = []
    reporte.append("ANALISIS DE DATOS DEL OECE - 2025")
    reporte.append("=" * 40)
    reporte.append(f"Archivo: {archivo.name}")
    reporte.append(f"Total de registros: {filas}")
    reporte.append(f"Total de columnas: {columnas}")
    reporte.append(f"Filas duplicadas exactas: {duplicados}")

    reporte.append("\nCOLUMNAS DISPONIBLES:")
    for columna in datos.columns:
        reporte.append(str(columna))

    reporte.append("\nVALORES VACIOS POR COLUMNA:")
    for columna, cantidad in vacios.items():
        reporte.append(f"{columna}: {cantidad}")

    # Crear la carpeta de resultados
    salida.parent.mkdir(parents=True, exist_ok=True)

    # Guardar el reporte
    salida.write_text(
        "\n".join(reporte),
        encoding="utf-8"
    )

    print("\n".join(reporte))
    print("\nAnalisis finalizado correctamente.")
    print("Reporte guardado en:", salida)

except Exception as error:
    print("Ocurrio un error:", error)


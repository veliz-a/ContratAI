from pathlib import Path
import pandas as pd

# Ubicación de los archivos
carpeta = Path(__file__).parent
archivo = carpeta / "datos" / "Lista-Procesos.xls"
salida = carpeta / "output" / "A_seace.txt"

try:
    # Leer el archivo Excel
    datos = pd.read_excel(archivo, engine="xlrd")

    # Preparar el reporte
    reporte = []
    reporte.append("ANALISIS DE DATOS DEL SEACE - 2026")
    reporte.append("=" * 40)
    reporte.append(f"Archivo: {archivo.name}")
    reporte.append(f"Total de registros: {len(datos)}")
    reporte.append(f"Total de columnas: {len(datos.columns)}")
    reporte.append(
        f"Filas duplicadas exactas: {datos.duplicated().sum()}"
    )

    reporte.append("\nCOLUMNAS DISPONIBLES:")
    for columna in datos.columns:
        reporte.append(str(columna))

    reporte.append("\nVALORES VACIOS POR COLUMNA:")
    for columna, cantidad in datos.isnull().sum().items():
        reporte.append(f"{columna}: {cantidad}")

    # Crear carpeta de resultados
    salida.parent.mkdir(parents=True, exist_ok=True)

    # Guardar reporte
    salida.write_text(
        "\n".join(reporte),
        encoding="utf-8"
    )

    # Mostrar resultados
    print("\n".join(reporte))
    print("\nAnalisis finalizado correctamente.")
    print("Reporte guardado en:", salida)

except Exception as error:
    print("Ocurrio un error:", error)
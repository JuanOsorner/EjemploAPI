# Importaciones de nuestros módulos
from ConsumoAPI import ConsumoAPI
from CrearDF import DataFrameFactory
from AnalisisAccesosFamiliares import AnalizadorAccesos
from GeneradorPDF import ReportePDF # <-- Nueva importación

def main():
    """
    Función principal que orquesta el análisis de datos y la generación de reportes.
    """
    # 1. Configuración de la API
    BASE_URL = "http://localhost:8080"
    ENDPOINT_ESTUDIANTES = "/estudiantes"
    ENDPOINT_ACCESOS = "/consultas/analiticas/accesos-por-estudiante"
    ENDPOINT_CONSULTAS = "/consultas"

    # 2. Consumo de la API
    print("Iniciando consumo de la API...")
    api_consumer = ConsumoAPI(BASE_URL)
    
    json_estudiantes = api_consumer.consumir_api(ENDPOINT_ESTUDIANTES)
    json_accesos = api_consumer.consumir_api(ENDPOINT_ACCESOS)
    json_consultas = api_consumer.consumir_api(ENDPOINT_CONSULTAS)

    if not all([json_estudiantes, json_accesos, json_consultas]):
        print("Error: No se pudieron obtener todos los datos de la API. Verifique que la API esté en funcionamiento.")
        return

    print("Datos obtenidos correctamente.")

    # 3. Creación de DataFrames
    print("Creando DataFrames...")
    factory = DataFrameFactory()
    df_estudiantes = factory.crear_df_estudiantes(json_estudiantes)
    df_accesos = factory.crear_df_accesos_por_estudiante(json_accesos)
    df_consultas = factory.crear_df_consultas(json_consultas)
    print("DataFrames creados.")

    # 4. Análisis de Datos
    print("Iniciando análisis de datos...")
    analizador = AnalizadorAccesos(df_estudiantes, df_accesos, df_consultas)

    reporte_accesos = analizador.analizar_accesos_por_estudiante()
    print("\n--- Análisis de Accesos por Estudiante (HUPF1) ---")
    print(reporte_accesos.to_string())

    reporte_horarios = analizador.analizar_horarios_acceso()
    print("\n--- Análisis de Horarios de Acceso (HUPF2) ---")
    print(reporte_horarios.to_string())
    print("\nAnálisis completado.")

    # 5. Generación de Reporte PDF
    print("\nGenerando reporte en PDF...")
    try:
        pdf = ReportePDF(reporte_accesos, reporte_horarios)
        pdf.generar_reporte("reporte_analisis.pdf")
        print("\nReporte 'reporte_analisis.pdf' generado exitosamente en la carpeta del proyecto.")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")

if __name__ == "__main__":
    main()

from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt
import os

class ReportePDF(FPDF):
    """
    Clase para generar un reporte en PDF a partir de los análisis de datos.
    Hereda de FPDF para facilitar la personalización.
    """

    def __init__(self, df_accesos, df_horarios):
        super().__init__()
        self.df_accesos = df_accesos
        self.df_horarios = df_horarios
        self.grafico_path = 'reporte_horarios.png'

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Reporte de Análisis de Acceso Familiar', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def _generar_grafico_horarios(self):
        """Genera y guarda un gráfico de barras para el análisis de horarios."""
        plt.figure(figsize=(10, 6))
        plt.bar(self.df_horarios['hora'], self.df_horarios['numeroDeAccesos'], color='skyblue')
        plt.xlabel('Hora del Día')
        plt.ylabel('Número de Accesos')
        plt.title('Distribución de Accesos por Hora')
        plt.xticks(self.df_horarios['hora'])
        plt.grid(axis='y', linestyle='--')
        plt.savefig(self.grafico_path)
        plt.close()

    def _crear_tabla(self, df):
        """Crea una tabla en el PDF a partir de un DataFrame."""
        # Ancho de las celdas
        col_widths = {
            'nombre': 70,
            'programa': 60,
            'numeroDeAccesos': 40,
            'hora': 80
        }
        
        # Header
        self.set_font('Arial', 'B', 10)
        for col in df.columns:
            width = col_widths.get(col, 50) # Ancho por defecto
            self.cell(width, 10, col, 1, 0, 'C')
        self.ln()

        # Data
        self.set_font('Arial', '', 10)
        for index, row in df.iterrows():
            for col in df.columns:
                width = col_widths.get(col, 50)
                self.cell(width, 10, str(row[col]), 1, 0, 'L')
            self.ln()

    def generar_reporte(self, nombre_archivo='reporte_analisis.pdf'):
        """Ensambla y guarda el reporte PDF final."""
        self.add_page()

        # Sección 1: Accesos por Estudiante
        self.set_font('Arial', 'B', 11)
        self.cell(0, 10, '1. Análisis de Accesos por Estudiante (HUPF1)', 0, 1, 'L')
        self.ln(5)
        self._crear_tabla(self.df_accesos)
        self.ln(10)

        # Sección 2: Horarios de Acceso
        self.set_font('Arial', 'B', 11)
        self.cell(0, 10, '2. Análisis de Horarios de Acceso (HUPF2)', 0, 1, 'L')
        self.ln(5)
        
        # Generar y añadir gráfico
        self._generar_grafico_horarios()
        self.image(self.grafico_path, x=None, y=None, w=150)
        os.remove(self.grafico_path) # Limpiar la imagen después de usarla
        self.ln(5)

        # Añadir tabla de horarios
        self._crear_tabla(self.df_horarios)

        self.output(nombre_archivo)

import pandas as pd

class AnalizadorAccesos:
    """
    Clase para analizar los datos de acceso de familiares a perfiles de estudiantes.
    """

    def __init__(self, df_estudiantes, df_accesos, df_consultas):
        """
        Inicializa el analizador con los DataFrames necesarios.

        :param df_estudiantes: DataFrame con la información de los estudiantes.
        :param df_accesos: DataFrame con el número de accesos por estudiante.
        :param df_consultas: DataFrame con el detalle de las consultas.
        """
        self.df_estudiantes = df_estudiantes
        self.df_accesos = df_accesos
        self.df_consultas = df_consultas

    def analizar_accesos_por_estudiante(self):
        """
        HUPF1: Analiza cuántos familiares consultan el perfil del estudiante.
        
        - Agrupa por ID de estudiante.
        - Cuenta el número de accesos.
        - Detecta estudiantes sin interacción.

        :return: DataFrame con el nombre del estudiante, su programa y el número de accesos.
        """
        # Unir el DataFrame de estudiantes con el de accesos
        df_merged = pd.merge(self.df_estudiantes, self.df_accesos, left_on='id', right_on='estudianteId', how='left')

        # Rellenar con 0 los accesos para estudiantes que no tienen ninguno
        df_merged['numeroDeAccesos'] = df_merged['numeroDeAccesos'].fillna(0).astype(int)

        # Seleccionar y renombrar las columnas para el reporte final
        reporte_final = df_merged[['nombre', 'programa', 'numeroDeAccesos']]
        
        return reporte_final

    def analizar_horarios_acceso(self):
        """
        HUPF2: Analiza en qué horarios acceden más los familiares.

        - Extrae la hora de la columna de fecha.
        - Agrupa por franja horaria y cuenta los accesos.
        
        :return: DataFrame con el conteo de accesos por hora.
        """
        if self.df_consultas.empty:
            return pd.DataFrame(columns=['hora', 'numeroDeAccesos'])

        # Extraer la hora de la columna fechaConsulta
        df_copy = self.df_consultas.copy()
        df_copy['hora'] = df_copy['fechaConsulta'].dt.hour

        # Agrupar por hora y contar el número de accesos
        accesos_por_hora = df_copy.groupby('hora').size().reset_index(name='numeroDeAccesos')
        
        return accesos_por_hora
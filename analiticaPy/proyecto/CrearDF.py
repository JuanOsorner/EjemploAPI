import pandas as pd

class DataFrameFactory:
    """
    Clase encargada de crear DataFrames a partir de datos JSON.
    """

    def crear_df_estudiantes(self, json_data):
        """
        Crea un DataFrame de estudiantes a partir de una lista JSON.

        :param json_data: Lista de diccionarios con datos de estudiantes.
        :return: DataFrame de pandas con la información de los estudiantes.
        """
        if not json_data:
            return pd.DataFrame()
        
        df = pd.DataFrame(json_data)
        return df

    def crear_df_accesos_por_estudiante(self, json_data):
        """
        Crea un DataFrame del número de accesos por estudiante.

        :param json_data: Lista de diccionarios con el conteo de accesos.
        :return: DataFrame de pandas con los accesos por estudiante.
        """
        if not json_data:
            return pd.DataFrame()
            
        df = pd.DataFrame(json_data)
        return df

    def crear_df_consultas(self, json_data):
        """
        Crea un DataFrame con el historial de consultas de familiares.

        :param json_data: Lista de diccionarios con los datos de las consultas.
        :return: DataFrame de pandas con la información de las consultas.
        """
        if not json_data:
            return pd.DataFrame()
        
        df = pd.DataFrame(json_data)
        # Convertir la columna de fecha a formato datetime para análisis posteriores
        df['fechaConsulta'] = pd.to_datetime(df['fechaConsulta'])
        return df
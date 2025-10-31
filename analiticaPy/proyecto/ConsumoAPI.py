import requests

class ConsumoAPI:
    def __init__(self, base_url):
        if not base_url:
            raise ValueError("No se ha proporcionado ninguna URL base")
        self.base_url = base_url.rstrip("/")

    def consumir_api(self, endpoint="", method="GET", data=None):
        """
            Este metodo se encarga de consumir una api de manera especifica

            parametros: string-parametros, string-method, json-data

            retorna: un json

            excepciones: un error al conectar con la api
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}" # ejemplo http://localhost:8080/
        try:
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url, json=data)
            elif method == "PUT":
                response = requests.put(url, json=data)
            elif method == "DELETE":
                response = requests.delete(url)
            else:
                raise ValueError("Método HTTP no soportado")

            response.raise_for_status()  # Lanza excepción si el código no es 2xx
            return response.json()

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error al conectar con la API: {e}")

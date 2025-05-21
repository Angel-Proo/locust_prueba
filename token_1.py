from locust import HttpUser, task, constant
import pprint

class generate_token(HttpUser):
    wait_time = constant(3) # Tiempo de espera constante entre peticiones
    host = "https://reqres.in" # URL del servidor de pruebas
    token = None # Variable para almacenar el token

    @task
    def get_token(self):
        """
        Petición GET a la ruta /api/login para obtener el token
        """
        cuerpo = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        } # Diccionario de datos a enviar
        cabecera = {"x-api-key": "reqres-free-v1"} # Cabecera de la petición
        respuesta = self.client.post("/api/login", json=cuerpo, headers=cabecera) # POST a la ruta /account/v1/GenerateToken
        if respuesta.status_code == 200:
            self.token = respuesta.json()["token"] # Almacenar el token
            pprint.pprint(f"Token: {self.token}") # Imprimir el token
        pprint.pprint(f"{respuesta.json()}, metodo: {respuesta.request.method} {respuesta.status_code} solicitado por {respuesta.request.url}") # Imprimir el json de la respuesta
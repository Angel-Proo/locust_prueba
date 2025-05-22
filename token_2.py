from locust import HttpUser, task, constant
import pprint
from icecream import ic

class generate_token(HttpUser):
    wait_time = constant(3) # Tiempo de espera constante entre peticiones
    host = "https://reqres.in" # URL del servidor de pruebas
    token = None # Variable para almacenar el token

    @task # Decorador para indicar que esta función es una tarea
    def on_start(self):
        ic('desde on_start')
        self.get_token()

        # Cuando se obtiene el token, se realizan las siguientes peticiones en el orden indicado
        self.post()
        self.delete()

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
            self.token = respuesta.json().get("token") # Obtener el token
            pprint.pprint(f"Token: {self.token}") # Imprimir el token
        pprint.pprint(f"{respuesta.json()}, metodo: {respuesta.request.method} {respuesta.status_code} solicitado por {respuesta.request.url}") # Imprimir el json de la respuesta

    def post(self):
        """
        Petición POST a la ruta /api/users para crear un nuevo usuario
        """

        if self.token:
            ic('Existe el token desde post: ', self.token)

        cabeceras = {
            "x-api-key": "reqres-free-v1", 
            "Authorization": f"Bearer {self.token}"
        }
        cuerpo = {
            "name": "morpheus",
            "job": "leader"
        }
        respuesta = self.client.post("/api/users", json=cuerpo, headers=cabeceras)
        pprint.pprint(f"{respuesta.json()}, metodo: {respuesta.request.method} {respuesta.status_code} solicitado por {respuesta.request.url}")

    def delete(self):
        """
        Petición DELETE a la ruta /api/users/2 para eliminar un usuario
        """

        if self.token:
            ic('Existe el token desde delete: ', self.token)

        cabeceras = {
            "x-api-key": "reqres-free-v1", 
            "Authorization": f"Bearer {self.token}"
        }
        respuesta = self.client.delete("/api/users/2", headers=cabeceras)
        pprint.pprint(f"{respuesta.content},\n metodo: {respuesta.request.method} {respuesta.status_code} solicitado por {respuesta.request.url}")
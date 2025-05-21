from locust import HttpUser, task, between
from icecream import ic

class User(HttpUser): # Clase que hereda de HttpUser para realizar las peticiones
    wait_time = between(1, 5) # Tiempo random entre 1 y 5 segundos
    host = 'https://jsonplaceholder.typicode.com' # URL del servidor de pruebas

    @task # Peso de la petición (default: 1)
    def get_example(self): # Petición GET a la ruta /posts
        respuesta = self.client.get('/posts') # GET a la ruta /posts
        #print(f"Respuesta body: {respuesta.text}") # Imprimir el body de la respuesta
        #print(f"Respuesta status: {respuesta.json()}") # Imprimir el json de la respuesta
        #ic(respuesta.headers) # Imprimir los headers de la respuesta
        #ic(respuesta.elapsed.total_seconds()) # Imprimir el tiempo de respuesta
        ic(respuesta.url) # Imprimir la url de la respuesta
        ic(respuesta.status_code) # Imprimir el codigo de estado de la respuesta
        #ic(respuesta.content) # Imprimir el contenido de la respuesta
        ic(respuesta.encoding) # Imprimir el encoding de la respuesta
        ic(respuesta.cookies) # Imprimir los cookies de la respuesta
        ic(respuesta.history) # Imprimir el historial de la respuesta
        ic(respuesta.request) # Imprimir la petición de la respuesta
        ic(respuesta.reason) # Imprimir la razón de la respuesta
        ic(respuesta.request.method) # Imprimir el método de la petición de la respuesta
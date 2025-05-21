from locust import HttpUser, task, between
from icecream import ic
from pprint import pprint
import json

class User(HttpUser): # Clase que hereda de HttpUser para realizar las peticiones
    wait_time = between(1, 5) # Tiempo random entre 1 y 5 segundos
    host = 'https://jsonplaceholder.typicode.com' # URL del servidor de pruebas

    @task # Peso de la petición (default: 1)
    def get_example(self): # Petición GET a la ruta /posts
        respuesta = self.client.get('/posts/1') # GET a la ruta /posts
        diccionario = respuesta.json() # Convertir el json a un diccionario
        pprint(f"{diccionario} metodo: {respuesta.request.method} {respuesta.status_code}") # Imprimir el json de la respuesta
        
    @task # Peso de la petición (default: 1)
    def post_example(self): # Petición POST a la ruta /posts
        cabecera = {"Content-Type": "application/json; charset=utf-8"} # Cabecera de la petición
        diccionario = {
            "userId": 1,
            "title": "prueba",
            "body": "prueba"
        } # Diccionario de datos a enviar
        respuesta = self.client.post('/posts', json=diccionario, headers=cabecera, name="prueba POST") # POST a la ruta /posts
        pprint(f"{respuesta.json()} metodo: {respuesta.request.method} {respuesta.status_code}") # Imprimir el json de la respuesta

    @task # Peso de la petición (default: 1)
    def put_example(self): # Petición PUT a la ruta /posts
        cabecera = {"Content-Type": "application/json; charset=utf-8"} # Cabecera de la petición
        diccionario = {
            "id": 1,
            "userId": 1,
            "title": "prueba",
            "body": "prueba"
        } # Diccionario de datos a enviar
        respuesta = self.client.put('/posts/1', json=diccionario, headers=cabecera, name="prueba PUT") # PUT a la ruta /posts
        pprint(f"{respuesta.json()} metodo: {respuesta.request.method} {respuesta.status_code}") # Imprimir el json de la respuesta

    @task # Peso de la petición (default: 1)
    def delete_example(self): # Petición DELETE a la ruta /posts
        respuesta = self.client.delete('/posts/1', name="prueba DELETE") # DELETE a la ruta /posts
        pprint(f"{respuesta.json()} metodo: {respuesta.request.method} {respuesta.status_code}") # Imprimir el json de la respuesta
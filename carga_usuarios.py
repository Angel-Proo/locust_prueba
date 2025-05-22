from locust import HttpUser, TaskSet, task, between, LoadTestShape, constant
import pprint
from icecream import ic

class UserTasks(TaskSet): # Clase que hereda de TaskSet para agrupar las tareas
    @task # Peso de la petición (default: 1)
    def get_example(self): # Petición GET a la ruta /posts
        respuesta = self.client.get('/posts/1') # GET a la ruta /posts
        diccionario = respuesta.json() # Convertir el json a un diccionario
        del diccionario['body'] # Eliminar el campo body del diccionario
        print(f"{diccionario} metodo: {respuesta.request.method} {respuesta.status_code}") # Imprimir el json de la respuesta

class User(HttpUser): # Clase que hereda de HttpUser para realizar las peticiones
    wait_time = constant(0.5) # Tiempo de espera constante entre peticiones
    tasks = [UserTasks] # Asignar las tareas a la clase
    host = 'https://jsonplaceholder.typicode.com' # URL del servidor de pruebas

class CustomLoadTestShape(LoadTestShape): # Clase para definir la forma de carga personalizada
    stages = [
        {"duration": 15, "users": 10, "spawn_rate": 10}, # 10 usuarios en 15 segundos con una tasa de aparición de 10 usuarios por segundo
        {"duration": 30, "users": 20, "spawn_rate": 10}, # 20 usuarios en 30 segundos con una tasa de aparición de 10 usuarios por segundo
        {"duration": 60, "users": 30, "spawn_rate": 10}, # 30 usuarios en 60 segundos con una tasa de aparición de 10 usuarios por segundo
        {"duration": 90, "users": 100, "spawn_rate": 10}, # 100 usuarios en 90 segundos con una tasa de aparición de 10 usuarios por segundo
        {"duration": 120, "users": 40, "spawn_rate": 10}, # 40 usuarios en 120 segundos con una tasa de aparición de 10 usuarios por segundo
        {"duration": 105, "users": 10, "spawn_rate": 10} # 10 usuarios en 105 segundos con una tasa de aparición de 10 usuarios por segundo
    ]

    def tick(self): # Método que se llama en cada tick
        run_time = self.get_run_time() # Obtener el tiempo de ejecución
        ic(run_time) # Imprimir el tiempo de ejecución

        for stage in self.stages: # Iterar sobre las etapas
            if run_time < stage["duration"]: # Si el tiempo de ejecución es menor que la duración de la etapa
                ic(f"Tiempo de ejecución: {run_time}, duración de la etapa: {stage['duration']}") # Imprimir el tiempo de ejecución y la duración de la etapa
                return (stage["users"], stage["spawn_rate"]) # Retornar el número de usuarios y la tasa de aparición
            run_time -= stage["duration"] # Restar el tiempo de ejecución por la duración de la etapa
            ic(f"Tiempo de ejecución restante: {run_time}") # Imprimir el tiempo de ejecución restante
        return None
from locust import HttpUser, task, between

# inicializar locust -> locust -f locustfile.py
class EjemploUser(HttpUser):
    """
    Clase que hereda de HttpUser para realizar las peticiones
    """
    
    wait_time = between(1, 5) # Tiempo random entre 1 y 5 segundos
    host = "https://demoqa.com" # URL del servidor de pruebas

    @task(weight=1) # Peso de la petición
    def home(self):
        """
        Petición GET a la ruta /
        """
        self.client.get("/") # GET a la ruta /

    @task(weight=2) # Peso de la petición
    def books(self):
        """
        Petición GET a la ruta /about
        """
        self.client.get("/books") # GET a la ruta /about

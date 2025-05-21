# Proyecto de Pruebas de Carga con Locust

Este proyecto contiene ejemplos de scripts para realizar pruebas de carga y rendimiento utilizando [Locust](https://locust.io/).

## Estructura del proyecto

- `crud.py`: Ejemplo de pruebas CRUD (GET, POST, PUT, DELETE) sobre la API de jsonplaceholder.
- `print.py`: Ejemplo de impresión de información detallada de las respuestas HTTP.
- `locustfile.py`: Ejemplo básico de pruebas de carga sobre demoqa.com.
- `token_1.py`: Ejemplo de autenticación y obtención de token mediante una petición POST a la API de reqres.in. El script realiza una solicitud de login, almacena el token recibido y muestra la respuesta y el método utilizado.

## Requisitos

- Python 3.7+
- pip

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Ejecuta Locust con el archivo deseado, por ejemplo:

```bash
locust -f crud.py
```

Luego abre tu navegador en [http://localhost:8089](http://localhost:8089) para configurar y lanzar la prueba.

### Uso de la interfaz web de Locust

1. Ingresa la cantidad de usuarios simulados (Number of total users to simulate).
2. Define la tasa de generación de usuarios (Spawn rate, usuarios/segundo).
3. Haz clic en "Start swarming" para iniciar la prueba.
4. Visualiza en tiempo real estadísticas como peticiones por segundo, tiempos de respuesta, errores, etc.
5. Puedes detener la prueba en cualquier momento con "Stop".

### Parámetros principales de la interfaz web
- **Number of users**: Total de usuarios concurrentes simulados.
- **Spawn rate**: Usuarios nuevos que se agregan por segundo.
- **Host**: (opcional) URL base si no está definida en el script.

---

## Parámetros y configuraciones por terminal

Puedes personalizar la ejecución de Locust usando diferentes parámetros en la terminal:

- `-f`, `--locustfile`: Archivo de script a ejecutar (por defecto: locustfile.py).
- `-H`, `--host`: URL base del sistema bajo prueba (sobrescribe la del script).
- `-u`, `--users`: Número total de usuarios a simular (puede usarse en modo sin UI).
- `-r`, `--spawn-rate`: Tasa de generación de usuarios por segundo.
- `--headless`: Ejecuta Locust sin interfaz web (modo consola).
- `--run-time`: Duración total de la prueba (ejemplo: 1m, 10s, 1h).
- `--csv`: Prefijo para archivos de salida en formato CSV con estadísticas.
- `--html`: Genera un reporte HTML al finalizar la prueba.
- `--loglevel`: Nivel de log (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- `--stop-timeout`: Tiempo de espera para detener usuarios al finalizar.
- `--step-load`: Activa el modo de carga escalonada.
- `--step-users`: Número de usuarios a agregar en cada paso (con step-load).
- `--step-time`: Tiempo entre cada incremento de usuarios (con step-load).

#### Ejemplo de ejecución en modo headless:

```bash
locust -f crud.py --headless -u 100 -r 10 --run-time 1m --csv resultado --html reporte.html
```

Más opciones y detalles en la [documentación oficial de Locust](https://docs.locust.io/en/stable/running-locust.html).

## Dependencias principales

- locust
- icecream (para debug)
- pprint (incluido en la librería estándar de Python)

## Recursos
- [Documentación de Locust](https://docs.locust.io/en/stable/)
- [jsonplaceholder](https://jsonplaceholder.typicode.com/)
- [demoqa.com](https://demoqa.com/)
- [reqres.in](https://reqres.in/)

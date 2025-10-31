# API de Gestión Familiar y Cliente de Análisis de Datos

Este proyecto es una solución integral que consta de dos componentes principales: una **API RESTful desarrollada en Java con Spring Boot** para la gestión de perfiles de estudiantes y sus familiares, y un **cliente de análisis de datos en Python** que consume esta API para procesar la información y generar reportes visuales en formato PDF.

## 🚀 Características Principales

### Backend (API RESTful)
- **Gestión de Entidades:** Sistema completo para administrar `Usuarios`, `Estudiantes`, y `Familiares` con roles y perfiles diferenciados.
- **Modelo Relacional:** Lógica para crear y gestionar `Vínculos` entre estudiantes y familiares, así como registrar `Consultas` (accesos) a los perfiles.
- **Autenticación Segura:** Endpoints de registro y login con encriptación de contraseñas (`BCrypt`).
- **Endpoints Analíticos:** Consultas optimizadas en la base de datos para ofrecer métricas clave, como el número de accesos por estudiante y la distribución de accesos por hora del día.
- **Arquitectura Limpia:** Separación clara de responsabilidades en Controladores, Servicios, Repositorios y un mapeo eficiente entre entidades y DTOs con `MapStruct`.

### Cliente de Análisis (Python)
- **Consumo de API:** Un cliente robusto para realizar peticiones HTTP a la API y obtener los datos en formato JSON.
- **Procesamiento de Datos:** Uso de la librería **Pandas** para transformar los datos JSON en DataFrames, facilitando su limpieza y análisis.
- **Análisis Estadístico:** Implementación de lógica para analizar y agregar los datos, respondiendo a preguntas como "¿qué estudiantes reciben más consultas?" o "¿a qué horas hay más actividad?".
- **Generación de Reportes:** Creación automática de **reportes en PDF** con tablas y gráficos (usando `Matplotlib` y `FPDF`) que resumen los hallazgos del análisis.

## 🛠️ Tecnologías Utilizadas

| Componente          | Tecnología              | Propósito                                                |
| :------------------ | :---------------------- | :------------------------------------------------------- |
| **Backend** | Java 17                 | Lenguaje de programación principal.                      |
|                     | Spring Boot             | Framework para la creación de la API RESTful.            |
|                     | Spring Data JPA & Hibernate | Persistencia de datos y comunicación con la base de datos. |
|                     | MySQL                   | Sistema de gestión de bases de datos relacional.         |
|                     | Maven                   | Gestión de dependencias y construcción del proyecto.     |
|                     | MapStruct               | Mapeo de objetos entre Entidades y DTOs.                 |
| **Cliente de Análisis** | Python                  | Lenguaje para el scripting y análisis de datos.          |
|                     | Requests                | Cliente HTTP para consumir la API.                       |
|                     | Pandas                  | Manipulación y análisis de datos.                        |
|                     | Matplotlib              | Creación de gráficos y visualizaciones.                  |
|                     | FPDF                    | Generación de documentos PDF.                            |

## ⚙️ Instalación y Puesta en Marcha

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### Prerrequisitos
- JDK 17 o superior.
- Apache Maven.
- Python 3.8 o superior.
- Un servidor de base de datos MySQL en ejecución.

### 1. Configuración del Backend (API `familia-api`)

1.  **Clona el repositorio:**
    ```sh
    git clone [URL-DE-TU-REPOSITORIO]
    cd [NOMBRE-REPOSITORIO]/familia-api
    ```
2.  **Configura la base de datos:**
    Abre el archivo `src/main/resources/application.properties` y modifica las siguientes líneas con tus credenciales de MySQL. La API creará la base de datos `familia_db` si no existe.
    ```properties
    spring.datasource.url=jdbc:mysql://localhost:3306/familia_db?createDatabaseIfNotExist=true
    spring.datasource.username=root
    spring.datasource.password=
    ```
3.  **Ejecuta la aplicación:**
    Desde la raíz del directorio `familia-api`, ejecuta el siguiente comando:
    ```sh
    mvn spring-boot:run
    ```
    La API estará disponible en `http://localhost:8080`.

### 2. Configuración del Cliente de Análisis (`analiticaPy`)

1.  **Navega al directorio del cliente:**
    ```sh
    cd ../analiticaPy
    ```
2.  **Crea y activa un entorno virtual:**
    ```sh
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```
3.  **Instala las dependencias:**
    Crea un archivo `requirements.txt` con el siguiente contenido y luego instálalo.
    ```txt
    # requirements.txt
    requests
    pandas
    matplotlib
    fpdf
    ```
    Ejecuta el comando de instalación:
    ```sh
    pip install -r requirements.txt
    ```
4.  **Ejecuta el script principal:**
    Este script consumirá la API (que debe estar en ejecución) y generará el reporte.
    ```sh
    python main.py
    ```
    Al finalizar, se creará un archivo `reporte_analisis.pdf` en el directorio `analiticaPy`.

## 📖 Documentación de la API

A continuación se muestran algunos de los endpoints más relevantes.

| Método | Endpoint                                             | Descripción                                                              | Ejemplo de Body (Payload)                                                  |
| :----- | :--------------------------------------------------- | :----------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| `POST` | `/usuarios`                                          | Crea un nuevo usuario (Estudiante o Familiar).                           | `{"nombre":"Test User", "correo":"test@mail.com", "contra":"123456", "rol":"ESTUDIANTE"}` |
| `POST` | `/usuarios/login`                                    | Autentica a un usuario y devuelve sus datos.                             | `{"correo":"test@mail.com", "contra":"123456"}`                             |
| `POST` | `/vinculos`                                          | Crea una relación entre un estudiante y un familiar.                     | `{"estudiante":{"id":1}, "familiar":{"id":2}, "parentesco":"Padre"}`         |
| `POST` | `/consultas`                                         | Registra que un familiar ha consultado el perfil de un estudiante.       | `{"vinculoId": 1, "observaciones": "Revisión de calificaciones."}`          |
| `GET`  | `/consultas/analiticas/accesos-por-estudiante` | Devuelve el número total de consultas agrupadas por ID de estudiante.    | N/A                                                                        |
| `GET`  | `/consultas/analiticas/accesos-por-hora`       | Devuelve el número total de consultas agrupadas por hora del día.        | N/A                                                                        |
| `GET`  | `/estudiantes`                                       | Obtiene una lista de todos los estudiantes.                              | N/A                                                                        |

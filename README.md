# EduLeads

## Indice
1. Descripción del Proyecto
2. Requisitos del Sistema
3. Instalación y Configuración
4. Uso
5. Arquitectura del Proyecto
6. Patrones de Diseño Aplicados
7. Documentación Técnica


## Descripción del Proyecto
Este proyecto es una aplicación web completa que consta de un backend desarrollado en FastAPI y un frontend en HTML, CSS y JavaScript. El propósito de la aplicación es registrar leads (personas cursando materias en carreras) con funcionalidades para registrar personas, materias y carreras, así como para consultar la información de los leads registrados.

#### Objetivos
* Proveer una API RESTful para gestionar información de leads.
* Ofrecer una interfaz de usuario para la gestión de leads de manera intuitiva.
* Utilizar una base de datos PostgreSQL para la persistencia de datos.
* Dockerizar el frontend y el backend para facilitar la implementación y la escalabilidad.
## Requisitos del sistema
* Docker y Docker Compose instalados en el sistema.
* Python 3.11+ (si se desea ejecutar el backend localmente sin Docker).
* Node.js y npm (si se desea ejecutar el frontend localmente sin Docker).
* PostgreSQL (si se desea usar una base de datos externa).
## Instalacion y Configuracion
##### Paso 1: Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```
##### Paso 2: Configurar Variables de Entorno
Asegúrate de configurar las variables de entorno necesarias para conectar el backend con la base de datos PostgreSQL. Estas variables se encuentran en el archivo `docker-compose.yml`:


```bash
environment:
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: password
  POSTGRES_DB: mydatabase
  DATABASE_URL: postgresql://postgres:password@db:5432/mydatabase
```

##### Paso 3: Construir y Ejecutar los Contenedores
Ejecuta los siguientes comandos para construir y ejecutar los contenedores de Docker:
```bash
docker-compose build
docker-compose up
```
Esto levantará el backend en `http://localhost:8000` y el frontend en `http://localhost`.

 
## Uso
#### Acceder a la Aplicación
*  Frontend: Accede a `http://localhost` para interactuar con la interfaz de usuario.
* API de Backend: La API de FastAPI está disponible en `http://localhost:8000`. Puedes explorar la documentación interactiva de la API en `http://localhost:8000/docs`.

## Arquitectura del Proyecto
El proyecto está dividido en dos principales componentes:
1. Backend:
    
    * Desarrollado en FastAPI.
    * Expone una API RESTful para operaciones CRUD sobre personas, materias y carreras.
    * Utiliza SQLAlchemy para la interacción con la base de datos PostgreSQL.
2. Frontend:
    
    * Desarrollado en HTML, CSS y JavaScript.
    * Proporciona una interfaz de usuario amigable para gestionar leads y asignar materias a personas.
    * Consume la API RESTful del backend para todas las operaciones.

## Patrones de Diseño Aplicados
El proyecto aplica varios patrones de diseño para mantener la calidad del código y facilitar la escalabilidad y el mantenimiento. Algunos de estos patrones son:

* SOLID: Principios para mantener un código limpio y robusto.
    
    * S: Single Responsibility Principle (SRP): Cada módulo o clase tiene una única responsabilidad.
    * O: Open/Closed Principle (OCP): El código está abierto a la extensión pero cerrado a la modificación.
    * L: Liskov Substitution Principle (LSP): Los objetos de una clase derivada pueden sustituir a los de una clase base sin alterar el funcionamiento del programa.
    * I: Interface Segregation Principle (ISP): Muchas interfaces específicas son mejores que una interfaz general.
    * D: Dependency Inversion Principle (DIP): Las dependencias de un módulo deben abstraerse.
* DAO (Data Access Object): Se utiliza un patrón DAO para encapsular todas las interacciones con la base de datos, separando la lógica de negocio de la lógica de acceso a datos.
* DTO (Data Transfer Object): Los DTOs se utilizan para transferir datos entre las capas de la aplicación sin exponer la estructura interna del modelo de datos.

## Documentacion Tecnica 
Dentro de los archivos establecidos en este proyecto vamos a visualizar la utilizacion y la formacion de distintas practicas y tecnologias.

* Modelos de la base de datos usando SQLAlchemy
* Definición de DTOs con Pydantic
* Endpoints de la API
* Lógica de negocio
* Punto de entrada de la aplicación FastAPI



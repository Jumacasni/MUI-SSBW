# MUII-SSBW
Asignatura de Sistemas Software Basados en Web (SSBW) - Máster Profesional en Ingeniería Informática 2020/2021

# Descripción
Desarrollo de una aplicación web inspirada en [Turgranada](https://www.turgranada.es/cosas-que-hacer/turismo-activo-y-de-naturaleza/excursiones-y-senderismo/), en la que se puedan consultar senderos y rutas por Granada, añadir fotos, mapas y comentarios por parte de los visitantes.

<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#tarea0">Tarea 0: Entorno de desarrollo para django con docker-compose</a>
    </li>
    <li>
      <a href="#tarea1">Tarea 1: Bases de Datos NoSQL, ORMs</a>
      <ul>
        <li><a href="#tarea11">Base de datos</a></li>
        <li><a href="#tarea12">Script de la población de la BD</a></li>
      </ul>
    </li>
    <li>
      <a href="#tarea2">Tarea 2: Empezando con Django</a>
    </li>
    <li>
      <a href="#tarea3">Tarea 3: Frameworks CSS</a>
    </li>
  </ol>
      
<a name="tarea0"></a>
## Tarea 0: Entorno de desarrollo para django con docker-compose

Seguiremos los pasos de [Quickstart: Compose and Django](https://docs.docker.com/compose/django/). En principio no usamos un servicio aparte para la BD, por lo que el archivo [docker-compose.yaml](docker-compose.yaml) sólo contiene el servicio web.

El contenedor se inicia usando el comando ```docker-compose up```

<a name="tarea1"></a>
## Tarea 1: Bases de Datos NoSQL, ORMs

<a name="tarea11"></a>
### Base de datos

Se usa [mongodb](https://docs.mongodb.com/guides/) como base de datos, una BD NoSQL, que entre otras tiene la ventaja de la flexibilidad, pudiendo cambiar la extructura de los datos durante el desarrollo, sin tener que rehacer la BD. Se añaden los servicios ```mongo``` y ```mongo-express``` (cliente gráfico de mongodb) al [docker-compose.yaml](docker-compose.yaml).

<a name="tarea12"></a>
### Script de la población de la BD

Como ORM se usa [mongoengine](http://mongoengine.org/), un orm para python muy inspirado en el original de [django models](https://docs.djangoproject.com/en/3.1/topics/db/models/) pero para mongodb. Hay que instalarlo con pip, incluyéndolo en el archivo de [requirements.txt](requirements.txt)

El script creado es [populate.py](populate.py) y se ejecuta usando ```docker-compose run web python populate.py```, que muestra como salida lo siguiente:

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/populate.png" width="70%" height="">

<a name="tarea2"></a>
## Tarea 2: Empezando con Django

Una pequeña aplicación de consulta de la BD, siguiendo el tutorial de [Django girls](https://tutorial.djangogirls.org/es/django_start_project/) con algunas pequeñas modificaciones:

* Se ha creado el modelo Excursion en el archivo [models.py](senderos/models.py) y se han añadido dos excursiones a través de [http://localhost:8000/admin](http://localhost:8000/admin):

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/admin.png" width="100%" height="">

* Y se modifica el archivo [index.html](senderos/templates/senderos/index.html) para que muestre la salida a través de [http://localhost:8000](http://localhost:8000):

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/index.png" width="60%" height="">

<a name="tarea3"></a>
## Tarea 3: Frameworks CSS

Se va a usar un **Framework CSS** para facilitar la tarea, consiguiendo también un diseño *responsive* que se adapte automáticamente al tamaño de la pantalla. Se va a usar [Bootstrap](https://getbootstrap.com/).

Se ha creado el archivo [base.html](senderos/templates/senderos/base.html) que contiene el código mínimo copiado desde [Starter template](https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template).

Se ha modificado el archivo [index.html](senderos/templates/senderos/index.html) incluyendo el *starter template* e incluyendo una **búsqueda básica de excursiones**. Se ha añadido la url *buscar* en el archivo [urls.py](senderos/urls.py) y el método *buscar* que atiende esa petición se ha añadido al archivo [views.py](senderos/views.py). Para acceder a esta url hay que ir a [http://localhost:8000/buscar](http://localhost:8000/buscar).

Utilizando bootstrap, se ha añadido un formulario básico de búsqueda:

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/buscar1.png" width="100%" height="">

Por último, para cada excursión se ha usado bootstrap para crear una tarjeta [(cards)](https://getbootstrap.com/docs/5.0/components/card/) por cada una:

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/buscar2.png" width="60%" height="">
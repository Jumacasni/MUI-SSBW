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
    <li>
      <a href="#tarea4">Tarea 4: CRUD</a>
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

* No se usa la base de datos de Django, si no que usamos el serivico que hemos instalado con **MongoDB**. Se ha creado el modelo Excursion en el archivo [models.py](senderos/models.py) y se han añadido dos excursiones a través de [http://localhost:8081/db/senderos/excursion](http://localhost:8081/db/senderos/excursion):

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/admin.png" width="80%" height="">

* Y se modifica el archivo [index.html](senderos/templates/senderos/index.html) para que muestre la salida a través de [http://localhost:8000](http://localhost:8000):

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/index.png" width="60%" height="">

<a name="tarea3"></a>
## Tarea 3: Frameworks CSS

Se va a usar un **Framework CSS** para facilitar la tarea, consiguiendo también un diseño *responsive* que se adapte automáticamente al tamaño de la pantalla. Se va a usar [Bootstrap](https://getbootstrap.com/).

Se ha creado el archivo [base.html](senderos/templates/senderos/base.html) que contiene el código mínimo copiado desde [Starter template](https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template).

Se ha modificado el archivo [index.html](senderos/templates/senderos/index.html) incluyendo el *starter template* e incluyendo una **búsqueda básica de excursiones**. Se ha añadido la url *buscar* en el archivo [urls.py](senderos/urls.py) y el método *buscar* que atiende esa petición se ha añadido al archivo [views.py](senderos/views.py).

Utilizando bootstrap, se ha añadido un formulario básico de búsqueda:

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/buscar1.png" width="100%" height="">

Por último, para cada excursión se ha usado bootstrap para crear una tarjeta [(cards)](https://getbootstrap.com/docs/5.0/components/card/) por cada una:

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/buscar2.png" width="60%" height="">

<a name="tarea4"></a>
## Tarea 4: CRUD

Se va a proporcionar una vista de detalle para cada excursión, permitiendo **añadir**, **borrar** y **editar** registros.

En el archivo [forms.py](senderos/forms.py) se ha añadido una clase que contiene el formulario para añadir o editar una excursión. En el archivo [index.html](senderos/templates/senderos/index.html) se ha añadido una ventana modal para crear el formulario. La funcionalidad de este formulario se encuentra en [views.py](senderos/views.py).

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/aniadir.png" width="100%" height="">

A continuación, se ha añadido funcionalidad al botón de **Info** de cada excursión. Se ha añadido a [urls.py](senderos/urls.py) la url que captura las url del tipo *localhost:8000/info/id*, donde *id* es el identificador de la excursión en la base de datos.

Para la vista de cada excursión se ha creado el archivo [info.html](senderos/templates/senderos/info.html), que contiene el nombre y descripción de la excursión, las fotos, los comentarios, y dos botones para editar y borrar la excursión.

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/vista_detalle.png" width="100%" height="">

La funcionalidad del botón **editar** muestra una ventana modal con el mismo formulario que para añadir una nueva excursión.

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/editar.png" width="100%" height="">

La funcionalidad del botón **eliminar** muestra una ventana modal para confirmar la eliminación de la excursión.

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/borrar.png" width="100%" height="">

<a name="tarea5"></a>
## Tarea 5: Autentificación, autorización y registro de eventos

Se añade autentificación, autorización de los usuarios sobre la BD y un registro de eventos en la aplicación:

* Se ha utilizado el plugin **django-allauth**, cuyo tutorial puede encontrarse [aquí](https://learndjango.com/tutorials/django-allauth-tutorial)
* Para el registro de eventos se ha utilizado el [logger](https://docs.djangoproject.com/en/3.1/topics/logging/) y las [signals](https://docs.djangoproject.com/en/3.1/topics/signals/)

En esta tarea se debe:
* Añadir un enlace en el menú para hacer un login o registro
* En el caso de que el usuario esté autentificado, deberá aparecer el nombre de usuario y un enlace para el logout
* Limitar la modificación de la BD a los administradores

En la siguiente imagen se pueden ver los botones de login y registro, cuyas plantillas se han obtenido de bootstrap.
<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/login-registro.png" width="100%" height="">

En las dos siguientes imágenes se puede apreciar que sólo el usuario con privilegios de administrador puede añadir rutas (además de editarlas, eliminarlas y modificarlas).
<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/usuario-con-privilegios.png" width="100%" height="">

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/usuario-sin-privilegios.png" width="100%" height="">

<a name="tarea6"></a>
## Tarea 6: REST API
Se proporciona una API RESTFUL usando la extensión [Django REST framework](https://www.django-rest-framework.org/) usando **serializers**. Se habilitan los siguientes endpoints:

* **/api/excursiones**: **GET** con la lista de todas las excursiones
* **/api/excursiones**: **POST** para añadir una excursión
* **/api/excursion/<id>**: **GET** con la información de una excursión
* **/api/excursion/<id>**: **PUT** para modificar una excursión
* **/api/excursion/<id>**: **DELETE** para borrar una excursión

Vista de la api de excursiones:
<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/api-excursiones.png" width="100%" height="">

Vista de la api de una excursión:
<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/api-excursion-id.png" width="100%" height="">

<a name="tarea7"></a>
## Tarea 7: jQuery, AJAX

Se va a mejorar la experiencia de usuario añadiendo código **jQuery** a la aplicación:

* Se añaden dos botones (pulgares hacia arriba y abajo) para darle *like* a las excursiones. Este contador de *likes* va conectado con la base de datos.
* Se añade un botón **modo noche** para cambiar el CSS a colores oscuros.

<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/modo-noche.png" width="100%" height="">

<a name="tarea8"></a>
## Tarea 8: React

Se proporciona un frontend en React. Para ello, se ha seguido [este tutorial](https://www.youtube.com/watch?v=Ke90Tje7VS0). Se debe instalar **django-cors-header** para usarlo durante la fase de desarrollo, permitiendo que se hagan requerimientos al servidor desde una URL distinta a la propia del servidor.

Se ha implementado una búsqueda de excursiones que va filtrando las excursiones a medida que el usuario va insertando caracteres en el formulario de búsqueda:
<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/formulario-react.png" width="100%" height="">

También se ha implementado una vista básica de la información de una excursion:
<img src="https://github.com/Jumacasni/MUII-SSBW/blob/main/img/excursion-react.png" width="100%" height="">

<a name="tarea9"></a>
## Tarea 9: Despliegue en producción

La última tarea consiste en desplegar la aplicación en producción, es decir, funcionando con la **depuración en OFF** y conectada a un servidor **nginx** en el puerto 80.

Se han implementado los siguientes cambios:

* Se añade el servidor **nginx** al [docker-compose.yaml](docker-compose.yaml) y se cambia el servidor de desarrollo (runserver) por el de producción (guicorn)
* Se añade la configuración del servidor **nginx** al archivo [nginx.conf](nginx.conf)
* Se cambia la configuración de producción en [settings.py](mi_sitio_web/settings.py)

A partir de este momento se puede acceder al servidor a través del puerto 80.
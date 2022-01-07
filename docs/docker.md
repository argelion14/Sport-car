# Docker

## Elección de un contenedor base: slim
### Criterios de búsqueda
Como criterio de búsqueda de nuestro contenedor destacamos los siguientes:
* Que sea oficial para evitar posibles problemas.
* Versión más estable.
* Contendor base lo más simple posible en que no haya cosas de más necesarias para nuestro proyecto.
* Lo más rápido posible.

Por ello se consultaron las posibles variantes del contenedor **oficial** de Dockerhub (aquí)[https://hub.docker.com/_/python].

No se consideró alpine como primera opción debido a [información](https://pythonspeed.com/articles/alpine-docker-python/) que aportaba que era más lento usar este en un docker de python, por ello se probó con slim en su versión más estable y actual, la 3.10.1-slim y este resultó en varias pruebas ser el más rápido para mi projecto.

Se han seguido buenas prácticas que contruyen la imagen pues creamos un usuario y le damos permisos y le asignamos grupo para que pueda trabajar sin problema.

Se ha hecho, lo más simple posible, lo necesario para testear mi projecto en el contenedor y lo que ello incluye.

El workdir esta correctamente establecido en donde se lanzarán los test, siendo este: app/test
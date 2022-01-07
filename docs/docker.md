# Docker

## Elección de un contenedor base
### Criterios de búsqueda
Como criterio de búsqueda de nuestro contenedor destacamos los siguientes:
* Que sea oficial para evitar posibles problemas.
* Versión más estable.
* Contendor base lo más simple posible en que no haya cosas de más necesarias para nuestro proyecto.
* Lo más rápido posible.

Por ello se consultaron las posibles variantes del contenedor **oficial** de Dockerhub (aquí)[https://hub.docker.com/_/python].

No se consideró alpine como primera opción debido a [información](https://pythonspeed.com/articles/alpine-docker-python/) que aportaba que era más lento usar este en un docker de python, por ello se probó con slim en su versión más estable y actual, la 3.10.1-slim.

docker build . --file Dockerfile --tag argelion14/sport-car
docker run -t -v `pwd`:/app/test argelion14/sport-car
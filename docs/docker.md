# Docker

## Elección de un contenedor base: slim-bulleye
### Criterios de búsqueda
Como criterio de búsqueda de nuestro contenedor destacamos los siguientes:
* Que sea oficial para evitar posibles problemas, estas tienen preinstaladas múltiples versiones de python, además de varias variantes que elegir.
* Contendor base lo más simple posible en que no haya cosas de más necesarias para nuestro proyecto.
* Lo más rápido posible, tanto en tiempo de contrucción de la imagen como en ejecución de test.
* Versión ^3.8.10 que es con la que se ha trabajado a lo largo del proyecto y a ser posible la última versión a modo de optimización y mejora respecto a una versión anterior siguiente así buenas [prácticas](https://blog.sqreen.com/top-10-python-security-best-practices/).

Por ello se consultaron las posibles variantes del contenedor **oficial** de Dockerhub [aquí](https://hub.docker.com/_/python).

No se consideró alpine como primera opción debido a [información](https://pythonspeed.com/articles/alpine-docker-python/) que aportaba que era más lento usar este en un docker de python, por ello se probó con slim (variante de Debian 11)(por ser la oficial de python que se centra es ser la más 'delgada') y dentro de esta con slim a secas, con slim bulleye y con slim buster.

Las pruebas realizadas a continuación reflejan las imagenes que se probarón. Se realizarón tres veces las pruebas y se hizo una media de ellas

Para medir el tiempo se realizó: 
```shell
time docker build . --file Dockerfile --tag argelion14/sport-car
```
Para sacar el tamaño se uso docker desktop.

| Imagen | Tiempo de construcción de la imagen | Tamaño | Ejecución de test |
| ------ | ------ | ------ | ----------------- |
| python:3.10.1-slim | 6.313s | 186.25MB | 0.002s |
| python:3.10.1-slim-bulleye | 6.415s | 179.35MB | 0.002s |
| python:3.10.1-slim-buster | 6.364 | 171.96MB | 0.002s |
| python:3.10-alpine | 6.821s | 297.94MB | 0.002s |

Podemos comprobar que los tamaños de los diferentes tipos de slim son parecidos, mientras que alpine pesa más, por ello esta queda descartada al ser con diferencia la más pesada.
La contrucción de la imagen es parecida escasas diferencias que se pueden ver influenciadas por factores externos.
La ejecución de test es parecida.

Por último elegimos la slim-bulleye debido a que en la versión slim a secas encontramos vulterabilidades de riesgo [(+info)](https://snyk.io/test/docker/python%3A3.10.1-slim) al igual que slim-buster [(+info)](https://snyk.io/test/docker/python%3A3.10.1-slim-buster) y slim-bulleye no existen vulnerabilidades conocidas [(+info)](https://snyk.io/test/docker/python%3A3.10.1-slim-bulleye).

Se han seguido buenas prácticas que contruyen la imagen pues creamos un usuario y le damos permisos y le asignamos grupo para que pueda trabajar sin problema.

Se ha hecho, lo más simple posible, lo necesario para testear mi proyecto en el contenedor y lo que ello incluye.

El workdir esta correctamente establecido en donde se lanzarán los test, siendo este: app/test

Con la opción poetry config virtualenvs.create pueste a false conseguiremos que poetry instale las dependencias en nuestro contenedor python haciendo de este más ligero. [(+info)](https://github.com/python-poetry/poetry/edit/master/docs/configuration.md)

Tras esto se instalarán todas las dependencias con poetry install y se ejecutaran los test con invoke.
# Integración continua

Existen numerosos sistemas de integración continua, con los cuales se busca para este objetivo pasar los test, en diferentes ambientes, automaticamente, ejecución de los test en las diferentes versiones de Python con cada subida al repositorio de Github.

Se establecen así una serie de requisitos mínimos que tienen que tener estos sistemas de integración continua:
* Poder probar distintas versiones de nuestro lenguaje, que sea operativo en diferentes ambientes.
* Que pueda correr Python.
* Que el sistema se integre con nuestro repositorio de github.
* Que sea un sistema actualizado y que se use en la actualidad para proyectos similares.
* Que sea gratuito, pues es un proyecto educativo que pretende enseñar y que se aprendan conceptos de desarrollo ágil.
* Fácil de implementar, sin necesidad de realizar una instalación en un servidor.

Nos centraremos en la versión 3.8 de python pues es esta la que se ha usado para desarrollar el proyecto de manera local.
![Version de python local](/docs/imagenes/version_python_local.png "Version de python local")

Se quiere también testear en la última versión, la 3.10, como es lógico y siguiendo [buenas prácticas](https://blog.sqreen.com/top-10-python-security-best-practices/), y siguiendo la lógica testearemos en las versiones intermedias, la 3.9.

Se han tenido en cuenta así: 
[Travis](https://travis-ci.org/), 
[Semaphore CI](https://semaphoreci.com/), 
[Azure](https://azure.microsoft.com/es-es/), 
[Circle ci](https://circleci.com/), 
[Github Actions](https://github.com/argelion14/Sport-car/blob/Objetivo6/.github/workflows/testear.yml)

* [X] Especificar porque se testea cada versión
* [X] En un CI usar varios ambientes/versiones del lenguaje utilizado
* [X] En cada una, aplicar los test

Comenzamos probando con los sistemas mencionados en la documentación de la asignatura como son github action o los servicios freemiun, Circle CI o Semaphore CI.

### Github Actions

Realizamos una github action para pasar los test del repositorio cuando sea necesario.

Para configurar la herramienta de integración continua, lo primero y como hicimos en nuestra action que contruia el docker y lo subía a Dockerhub será especificar cuando se ejecutará la tarea, en este caso cuando se modifique algún archivo de código o de test. En este caso [sport-car](https://github.com/argelion14/Sport-car/tree/Objetivo6/sportcar) y [test](https://github.com/argelion14/Sport-car/tree/Objetivo6/test).

Configuraremos el job para que ejecute los test en diferentes versiones de Python
 
![CI Github action](/docs/imagenes/CI_Github-action.png "CI Github action")
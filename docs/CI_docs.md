# Integración continua

Existen numerosos sistemas de integración continua, con los cuales se busca para este objetivo pasar los test, en diferentes ambientes, automaticamente, ejecución de los test en las diferentes versiones de Python con cada subida al repositorio de Github.

Se establecen así una serie de requisitos mínimos que tienen que tener estos sistemas de integración continua:
* Poder probar distintas versiones de nuestro lenguaje, que sea operativo en diferentes ambientes.
* Que pueda correr Python.
* Que el sistema se integre con nuestro repositorio de github.
* Que sea un sistema actualizado y que se use en la actualidad para proyectos similares.
* Que sea gratuito, pues es un proyecto educativo que pretende enseñar y que se aprendan conceptos de desarrollo ágil.
* Fácil de implementar, sin necesidad de realizar una instalación en un servidor.

Se han tenido en cuenta así: 
[Travis](https://travis-ci.org/), 
[Semaphore CI](https://semaphoreci.com/), 
[Azure](https://azure.microsoft.com/es-es/), 
[Circle ci](https://circleci.com/), 
[Github Actions]()

* [] Especificar porque se testea cada versión
* [] En un CI usar varios ambientes/versiones del lenguaje utilizado
* [] En cada una, aplicar los test

Comenzamos probando con los sistemas mencionados en la documentación de la asignatura como son github action o los servicios freemiun, Circle CI o Semaphore CI.


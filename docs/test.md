# Biblioteca de aserciones y de framework de test

## Biblioteca de aserciones

Para ello se proponen una serie de criterios que ha de cumplir, nuestra biblioteca:

* Una alta media de descargas semanales, que en este caso es de 35.340.
* Una comunidad activa que que me proporcione respuesta rápida y ágil antes posibles issues en la realización del proyecto.
* Una valoración positiva en github (329 estrellas)
* Una serie de assert que me ayuden a la hora de desarrollar el código (en este caso se encontró uno que beneficiaba particularmente para las afirmaciones de fecha).

Para las assert se usa la bilioteca que viene por defecto con python además de assertpy la cual me permite unas opciones más que necesito para validar mi código y cumple con los criterios que buscamos como biblioteca de aserciones, con afirmaciones simples para pruebas unitarias en python y también con la que puedo escalar a futuro los assert del mismo, esta elección se ha realizado en base a búsquedas en diferentes web, la popularidad y uso de la comunidad de esta, su populariad radica en que se descangan una media de 35.340 descargas a la semana, la comunidad se puede observar en esta [web](https://snyk.io/advisor/python/assertpy) y fijandonos en su [repositorio de github](https://github.com/assertpy/assertpy) la cual se observa una comunidad activa, cuenta con numerosas estrellas en github (329) y númerosos contribuidores, en base a esto se decidió ver esta biblioteca de aserciones en primera instancia, luego leyendo la extensa [documentación](https://assertpy.github.io/docs.html) se pudo comprobar que se ajustaba a las necesidades básicas primarias que necesitaba mi código.

## Framework de test
Para resolver el issue #11 donde se comprueba que funcionan las clases de usuario así como de actividad en el PMV.

Para realizar los test, los cuales serviran para comprobar el correcto funcionamiento del PMV, se han barajado varias opciones entre las se incluyen unittest, pytest, Robot framework y redwoodHQ aunque este último no se vió más en profundida debido a la dificultad, pues se necesitan conocimientos previos en el testing para entender el framework, estos vienen a ofrecer un entorno sencillo que me permita desarrollar test facilmente, sin complicaciones de lenguaje python pues todavía se esta aprendiendo a manejarlo y que genere los informes de prueba lo antes posible para ahorrar tiempo de desarrollo entre tests.

Se ha decidido usar unittest pues por pruebas objetivos he verificado me tarda menos, haciendo la misma prueba en ambos marcos de prueba, de 0,21 en pytest y de 0,010 en unittest, Robot framework por la estructura que poseía no se realizó ninguna prueba de este debido a la difícil documentacion que presentaba , además de cara a realizar este proyecto es preferible una estructura que valide las estructuras más pequeñas, suficiente para enterder los conceptos de validar y poder proseguir, por ello se ha preferido respecto a pytest, también debido a que es más fácil para personas con conocimientos pocos avanzados de python. Unittest esta actualizado y realizan numerosos PRs a su [github](https://github.com/python/cpython/tree/main/Lib/unittest). También se comenta que es un modulo de python por lo que **no se tendría que descargar ninguna biblioteca externa, lo cual considero el motivo principal del uso de unittest.**

En referente a temas objetivos me resulta más fácil de entender la documentación de unittest, así como sus ejemplos de uso y su estructura de clases me ha ayudado para organizar mis test de manera más clara para mi.

[Repositorio github](https://github.com/python/cpython/tree/main/Lib/unittest)
[Documentación](https://docs.python.org/3/library/unittest.html)

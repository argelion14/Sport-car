# Test: 

Para resolver el issue #11 donde se comprueba que funcionan las clases de usuario así como de actividad en el PMV.

Para realizar los test, los cuales serviran para comprobar el correcto funcionamiento del PMV, se han barajado varias opciones entre las se incluyen unittest y pytest.

Se ha decidido usar unittest pues por pruebas objetivos he verificado me tarda menos, haciendo la misma prueba en ambos marcos de prueba, de 0,21 en pytest y de 0,010 en unittest, además de cara a realizar este proyecto es preferible una estructura que valide las estructuras más pequeñas, suficiente para enterder los conceptos de validar y poder proseguir, por ello se ha preferido respecto a pytest. Unittest esta actualizado y realizan numerosos PRs a su [github](https://github.com/python/cpython/tree/main/Lib/unittest). También se comenta que es un modulo de python por lo que no se tendría que descargar ninguna biblioteca externa

En referente a temas objetivos me resulta más fácil de entender la documentación de unittest, así como sus ejemplos de uso.

# Biblioteca de aserciones y de framework de test

Para las assert se ha decidido usar la bilioteca que viene por defecto con python para no tener que instalar bibliotecas externar evitando así problemas de dependencia
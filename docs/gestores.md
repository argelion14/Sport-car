# Instalación
He decidido usar poetry pues fue el primer gestor del que oí hablar, busqué información sobre este y vi lo sencillo que era sobre Invoke y la documentación que aportaba en su web me ayudo a entender el uso de los test y control de dependencias, además de su archivo clave pyproject.toml el cual contiene metadata del proyecto y de todas sus dependencias, esta cuenta con su propia CLI (Command line interface) el cual es una ventaja a largo plazo pues facilita entre muchas cosas acceso a diferentes configuraciones de manera rápida y sencilla.


[Instalar poetry](https://python-poetry.org/docs/#installation)
Comprobamos que se ha instalado ejecutando 
~~~
poetry --version
~~~

# Uso
Inicialización de un proyecto preexistente para crear de forma interactiva un pyproject.toml
~~~
cd pre-existing-project
poetry init 
~~~
Para comprobar que el archivo pyproject.toml es correcto ejecutamos
~~~
poetry check
~~~


Ahora podemos correr los test con poetry run

#### En caso de tener pytest
~~~
poetry run pytest
~~~
#### En caso de tener pylint
~~~
poetry run pylint
~~~
### Para ejecutar su secuencia de comandos, simplemente use: 
~~~
poetry run python your_script.py
~~~
### Nuevos test al directorio test y lanzarlos:
~~~
poetry run /test/nombre.py
~~~


Tras esto: Para instalar las dependencias definidas para su proyecto, simplemente ejecute el install comando.

[poetry install](https://python-poetry.org/docs/basic-usage/#installing-dependencies)

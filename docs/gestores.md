# Instalación
[Instalar poetry](https://python-poetry.org/docs/#installation)
Comprobamos que se ha instalado ejecutando 
~~~
poetry --version
~~~
En Unix se encuentra en $HOME/.poetry/bin

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

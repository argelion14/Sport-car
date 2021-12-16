# Gestor de tareas: Invoke


[Instalar Invoke](https://www.pyinvoke.org/installing.html)
He decidido usar invoke como gestor de tareas de python en mi proyecto, en un primer paso, por la simplicidad que supone usarlo, al tener tan buena documentación, además de tener un API, de alto nivel y claro que permite ejecutar comandos y definir/organizar las funciones de las tareas con un archivo tasks.py.

~~Usaremos pyflakes para la comprobación sintasis/compilación de los ficheros~~

Usaremos pylint, debido a que la otra opción pyflakes, me mostraba mejor donde se encontraban los fallos, pero con pylint, se me aclara mejores prácticas de programación como la falta de docstring o el caso de usar modulos que no necesito o de tener modulo que no uso, por ello y porque mi aplicación quiero aprender buenas prácticas, más que conocer más sobre posibles errores, además de que debido a la simplicidad de la aplicación lo errores serían fáciles de localizar.
[Instalación: sudo apt-get install pylint](https://pylint.org/#install)

# Instalación del gestor de dependencias
He decidido usar poetry pues fue el primer gestor del que oí hablar, busqué información sobre este y vi lo sencillo que era sobre Invoke y la documentación que aportaba en su web me ayudo a entender el uso de los test y control de dependencias, además de su archivo clave pyproject.toml el cual contiene metadata del proyecto y de todas sus dependencias, esta cuenta con su propia CLI (Command line interface) el cual es una ventaja a largo plazo pues facilita entre muchas cosas acceso a diferentes configuraciones de manera rápida y sencilla.

Se buscó también información sobre invoke como se mencionó, el cual hacia de gestor de tareas, y se podía usar de respaldo a Pip como gestor de dependencias, pero esto no se consideró pues la primera opción era más sencilla de realizar en un primer vistazo, otro criterio que se buscó fue el mantenimiento pero en el momento en que se visitó ambos gestores, estos estaban siendo mantenidos a diario.

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

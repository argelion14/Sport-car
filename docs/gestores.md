# Gestores

## Gestor de tareas: Invoke

A continuación se destacan una serie de factores que tiene que cumplir nuestro gestor de tareas.

* Ha de ser sencillo de instalar, que no genere muchas dependencias su instalación.
* Documentación amplia que apoye el desarrollo y uso de la herramienta.
* Una API sencilla de usar pues se quiere de un uso a nivel básico.
* Poder realizar varios comandos, y poder elaborar las tareas en un único archivo a ser posible para evitar complejidad.
* Pythonic way, debido a que todo el proyecto se quiere hacer de esta manera.

Para ello se han revisado diferentes test runner, como son Poethepoet, Invoke o Make.

El primero, [Poethepoet](https://github.com/nat-n/poethepoet), se combina bien con Poetry y sigue la manera pythonica pues es específico de python, para ello necesita del archivo pyproject.toml donde se definen las tareas y posteriormente se ejecuta con Poe, *poe test* , siendo definida la tarea previamente en nuestro pyproject.toml. Esta herramienta usaba a poetry para funcionar en vez de tener un único archivo como es el caso de otros donde se una un unico archivo tasks.py, y además era más confuso y te tenias que adentrar más en su estructura para poder desarrollarlo de un manera correcta, la documentación es escasa y no se encuentra bien organizada.

[Make](https://www.gnu.org/software/make/manual/make.html) es una herramienta muy versatíl, con una sintaxis no muy complicada y que se lleva trabajando desde hace tiempo para funciones como compilación de programas en linux, esta actualmente se encuentra respaldada por desarrolladores. No se ha considerado debido a que pese a ser muy sencilla y operativa para lo que se necesita, un uso básico, no se usa de una manera pythinica, ni se recomienda por la comunidad para python.

He decidido por tanto usar la herramienta externa invoke como gestor de tareas de python en mi proyecto, en un primer paso y a nivel objetivo por lo que ofrece, una API de alto nivel y clara que permite ejecutar comandos y definir/organizar las funciones de las tareas con un *único* archivo tasks.py, asi es, un fichero python lo cual ayuda, todo esto esta soporteado y actualizado en github con una ultima actualización hace menos de 3 meses, como criterios subjetivos he decidido usar invoke frente a otros como poetry, por la sencillez del uso de este, ya que para un uso de entender lo que se busca y para mi aplicación de ejemplo viene bien, así como la fácil comprensión de la [documentación](https://docs.pyinvoke.org/en/stable/) para poder realizar las tareas que se tienen que llevar a cabo con una aplicación por medio de la herramienta de construcción.

Se seguirá la [documentación](https://docs.pyinvoke.org/en/stable/) oficial para instalar invoke por lo que se usará el gestor de dependencias **poetry**.

Para comprobar la compilación del código simplemente correremos el comando python3 -m compileall sportcar/*.py dentro del fichero tasks.py en el apartado check.

Para realizar los test con invoke, correremos el comando python3 -m unittest -v test/test.py dentro del fichero tasks.py en el apartado test.

## Gestor de dependencias: poetry
Se ha decidido emplear un gestor de dependecias mejor que pip combinado con requirements debido a una mejor práctica y estandar de projecto.

Para ello se ha buscado entre varios gestores de dependencias como son Flit, Setuptools y poetry,([+info](https://packaging.python.org/en/latest/key_projects/)) decantandonos por este último por la facilidad de generar el archivo pyproject.toml, también porque hoy día está siendo el estandar en control de dependencias, poetry esta destinado a [respaladar el desarrollo de aplicaciones](https://news.ycombinator.com/item?id=26735227), lo cual es lo que nosotros estamos buscando.

A nivel subjetivo, también se ha elegido Poetry pues ya se había trabajado con el anteriormente, a parte de que la documentación es adecuada y cuenta con numerosos participantes en su repositorio de [github](https://github.com/python-poetry/poetry) lo cual da sensación de servicio rápido de ayuda o de encontrar lo que busco en caso de necesitarlo.

Realizaremos la instalación desde la [documentación oficial](https://python-poetry.org/docs/#installation)

Tras esto se realizará el poetry init y se pondrá en marcha el archivo pyproject.toml, se instalaran las dependencias con poetry install o con nuestro gestor de tareas, con la orden invoke installdeps y se chequeará todo con poetry check.

# Gestores

## Gestor de tareas: Invoke

He decidido usar la herramienta externa invoke como gestor de tareas de python en mi proyecto, en un primer paso y a nivel objetivo por lo que ofrece, una API de alto nivel y clara que permite ejecutar comandos y definir/organizar las funciones de las tareas con un archivo tasks.py, todo esto esta soporteado y actualizado en github con una ultima actualización hace menos de 3 meses, como criterios subjetivos he decidido usar invoke frente a otros como poetry, por la sencillez del uso de este, ya que para un uso de entender lo que se busca y para mi aplicación de ejemplo viene bien, así como la fácil comprensión de la documentación para poder realizar las tareas que se tienen que llevar a cabo con una aplicación por medio de la herramienta de construcción.

Se seguirá la documentación oficial para instalar invoke por lo que se usará el gestor de dependencias **poetry**.

Para comprobar la compilación del código simplemente correremos el comando python3 -m compileall sportcar/*.py dentro del fichero tasks.py en el apartado check.

Para realizar los test con invoke, correremos el comando python3 -m unittest -v test/test.py dentro del fichero tasks.py en el apartado test.

## Gestor de dependencias
Se ha decidido emplear un gestor de dependecias mejor que pip combinado con requirements debido a una mejor práctica y estandar de projecto.

Para ello se ha buscado entre varios gestores de dependencias como son Flit, Setuptools y poetry,([+info](https://packaging.python.org/en/latest/key_projects/)) decantandonos por este último por la facilidad de generar el archivo pyproject.toml, también porque hoy día está siendo el estandar en control de dependencias, poetry esta destinado a [respaladar el desarrollo de aplicaciones](https://news.ycombinator.com/item?id=26735227), lo cual es lo que nosotros estamos buscando.

A nivel subjetivo, también se ha elegido Poetry pues ya se había trabajado con el anteriormente, a parte de que la documentación es adecuada y cuenta con numerosos participantes en su repositorio de [github](https://github.com/python-poetry/poetry) lo cual da sensación de servicio rápido de ayuda o de encontrar lo que busco en caso de necesitarlo.

Realizaremos la instalación desde la [documentación oficial](https://python-poetry.org/docs/#installation)

Tras esto se realizará el poetry init y se pondrá en marcha el archivo pyproject.toml, se instalaran las dependencias con poetry install y se chequeará todo con poetry check.
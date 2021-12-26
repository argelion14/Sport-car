# Gestor de tareas: Invoke


He decidido usar la herramienta externa invoke como gestor de tareas de python en mi proyecto, en un primer paso y a nivel objetivo por lo que ofrece, una API de alto nivel y clara que permite ejecutar comandos y definir/organizar las funciones de las tareas con un archivo tasks.py, todo esto esta soporteado y actualizado en github con una ultima actualización hace menos de 3 meses, como criterios subjetivos he decidido usar invoke frente a otros como poetry, por la sencillez del uso de este, ya que para un uso de entender lo que se busca y para mi aplicación de ejemplo viene bien, así como la fácil comprensión de la documentación para poder realizar las tareas que se tienen que llevar a cabo con una aplicación por medio de la herramienta de construcción.

Se seguirá la documentación oficial para instalar invoke por lo que se usará el gestor de dependencias pip.

[Instalar Invoke](https://www.pyinvoke.org/installing.html).

Para comprobar la compilación del código simplemente correremos el comando python3 -m compileall sportcar/*.py dentro del fichero tasks.py en el apartado check

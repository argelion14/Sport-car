from invoke import task, run

@task
def installdeps(c):
    """
    Instala todas las dependencias
    """
    print("Instalar las dependencias")
    run ("pip3 install -r requirements.txt")
    print("Se han instalado correctamente las dependencias")

@task
def check(c):
    print("Comprobar la compilación")
    run ("python3 -m compileall sportcar/*.py")
    print("Compilacion nice!")

@task
def test(c):
    print("Lanzamos los test de unittest")
    run("python3 -m unittest -v test/test.py")
    print("Todo correcto")
from invoke import task, run

@task
def installdeps(c):
    """
    Instala todas las dependencias
    """
    print("Instalar las dependencias")
    run ("poetry install")
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

@task 
def docker(c):
    print("Contruimos y ejecutamos los test en el contenedor docker")
    run("docker build . --file Dockerfile --tag argelio14/sport-car && docker run -t -v `pwd`:/app/test argelion14/sport-car")
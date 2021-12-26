from invoke import task, run

@task
def check(c):
    print("Comprobar la compilación")
    run ("python3 -m compileall sportcar/*.py")
    print("Compilacion nice!")

@task
def test(c):
    print("Lanzamos los test")
    run("pytest test/")
    print("Todo correcto")
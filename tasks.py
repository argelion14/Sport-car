from invoke import task, run

@task
def check(c):
    print("Comprobar la compilación")
    run ("python3 -m compileall sportcar/*.py")
    print("Compilacion nice!")
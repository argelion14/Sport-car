from invoke import task, run

@task
def check(c, docs=False):
    #c.run("python setup.py build")
    print("Comprobar sintasis/compilación")
    run ("pylint sportcar")
    print("Compilacion nice!")
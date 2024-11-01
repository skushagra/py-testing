from veritas import Veritas

def add(a, b):
    return a + b

veritas = Veritas()
veritas.on(add, 3, a=1, b=2)
veritas.runAll(descriptive=True)
"""
Funções def em python
"""
def hello(word='fulano', name='gui'):
    return f'Hello {word}, {name}'


print(hello('gui'))
print(hello())
print(hello(name='deia'))

"""
toda função retorna um valor mesmo sem passar return
"""
def funcao(var):
    print(var)

variavel = funcao('blabla')
print(variavel)


def divisao(n1, n2):
    if n2 == 0:
        return 'Conta inválida!'
    return n1 / n2


print(divisao(8, 0))


def dumb():
    return divisao


print(id(dumb()), id(divisao), dumb() == divisao)

"""
Retornam tuplas - lista inalteravel
"""
def tupla():
    return 'gui', 'almeida', 1


print(tupla(), type(tupla()))


def lista():
    return ['gui', 'almeida', 1]


print(lista(), type(lista()))

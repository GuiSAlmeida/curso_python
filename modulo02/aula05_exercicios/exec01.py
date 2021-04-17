"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""


def func(fn):
    return fn()


def func2():
    return 'valor da função 2'


print(func(func2))

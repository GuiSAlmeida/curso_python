"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def master(fn, *args, **kwargs):
    print(args)
    print(kwargs)
    return fn(*args, **kwargs)


def hello(nome):
    return f'Olá {nome}'


def gretting(nome, saudacao):
    return f'{saudacao} {nome}'


print(master(hello, 'gui'))
print(master(gretting, 'gui', 'bom dia'))

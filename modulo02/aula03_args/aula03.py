"""
*args = argumentos vão ser empacotados dentro de uma tupla
**kwargs = keyword arguments - argumentos com plavra chave
"""


def func(*args, **kwargs):
    print(args)
    n1, n2, *n = args  # desempacotamento
    print(n)
    args = list(args)  # casting para list
    print(kwargs['nome'], kwargs.get('nome'))  # acessar propriedades objeto kwargs - *get mais seguro
    return args, kwargs


lista = [1, 2, 3, 4, 5]
print(func(*lista, nome='gui'))  # *lista desempacota lista

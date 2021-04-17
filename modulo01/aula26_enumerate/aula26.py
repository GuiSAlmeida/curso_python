"""
enumerate - enumera elementos de uma lista
"""

lista = [
    'gui',
    'deia'
]

enum = enumerate(lista, 10)
print(list(enum))
# [(10, 'gui'), (11, 'deia')]

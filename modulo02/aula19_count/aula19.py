"""
count([start], [step]) - itertools
retorna um iterador
"""
from itertools import count

contador = count(start=5, step=1)
index = count()

for valor in contador:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break

nomes = ['gui', 'deia', 'chokito', 'bulma']
lista_indexada = zip(index, nomes)
print(list(lista_indexada))

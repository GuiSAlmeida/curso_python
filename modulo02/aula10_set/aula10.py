"""
SETs - conjuntos
add(adiciona), update(atualiza), clear, discard(remove)
union(une) |
intersection & (todos elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

*não possui indices e nem ordemde posições
"""

# criando sets
set1 = {1, 2, 3, 4, 5}
set2 = set()

set2.add('python')
# update itera sobre valor passado
# e adiciona cada um em uma posição no set
set2.update('python')

print(f'set1: {set1}')
print(f'set2: {set2}')

# não aceita valores duplicados
lista = [1, 1, 2, 2, 2, 4, 4, 5, 6, 'gui', 6, 6, 7, 7, 8, 8]
lista = set(lista)
lista = list(lista)
print(f'lista: {lista}')

# union
set3 = set1 | set(lista)
print(f'union set1 | set(lista): {set3}')

# intersection
set3 = set1 & set(lista)
print(f'intersection set1 & set(lista): {set3}')

# difference *ordem importa vai pegar o elemento diferente da esquerda
set3 = set1 - set(lista)
print(f'difference set1 - set(lista): {set3}')

# symmetric_difference - elementos que não são intersecção nas duas listas
set3 = set1 ^ set(lista)
print(f'symmetric_difference set1 ^ set(lista): {set3}')

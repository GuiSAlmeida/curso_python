"""
Combinations | Permutations | Product - Itertools
Combinação - ordem não importa
Permutação - ordem importa
Ambos não repetem valores únicos
Produto - ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Gui', 'Deia', 'Chokito', 'Bulma']
# for grupo in combinations(pessoas, 2):
#     print(grupo)

# for grupo2 in permutations(pessoas, 2):
#     print(grupo2)

for grupo2 in product(pessoas, repeat=2):
    print(grupo2)

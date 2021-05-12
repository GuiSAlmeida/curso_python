"""
list comprehension
"""
# ex1
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [v for v in l1]  # copia toda lista l1
l3 = [v * 2 for v in l1]  # multiplica cada item por 2 e adiciona na nova lista
l4 = [(v, v2) for v in l1 for v2 in range(1, 10, 2)]
print(l4)

# ex2
nomes = ['gui', 'deia', 'chokito', 'bulma']
arroubas = [v.replace('a', '@').upper() for v in nomes]
print(arroubas)

# ex3
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
inverted = [(y, x) for x, y in tupla]
print(inverted)
dict_inverted = dict(inverted)
print(dict_inverted)

# ex4
nums = list(range(100))
pares = [v for v in nums if v % 2 == 0 and v % 8 == 0]
print(pares)
impares = [v if v % 3 == 0 else 1 for v in nums]  # se v não for impar vai atribuir valor 1 no else
print(impares)

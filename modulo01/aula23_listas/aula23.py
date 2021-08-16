"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, min, max
range, list
"""
# indices    0  1  2    3     4
lista = [1, 2, 3, 'gui', True]
# indices   -5 -4 -3   -2    -1

print(lista)  # mostra toda lista
print(lista[4])  # mostra valor que está na posição do indice passado
lista[4] = False
print(lista[4])  # aceita reatribuição de valor na variavel

# Fatiamento (mesmas regras para strings)
print(lista[1:5:2])

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l2.append('add')        # add no final da lista
l2.insert(0, 'banana')  # add no indice da lista
l1.extend(l2)           # add valor o objeto passado
l1.pop()                # remove valor ultimo indice

del (l1[0:3])
del (l1[0])

print(l1)
print(max(l1))

l3 = range(1, 10)
l3 = list(l3)
print(l3)

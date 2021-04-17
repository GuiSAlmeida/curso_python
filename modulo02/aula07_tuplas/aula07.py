"""
Tuplas - elementos não podem ser editados, adicionados ou removidos.
"""

t1 = ('gui', 24, 'Março')
t2 = ('deia', 22, 'janeiro')
t3 = t1 + t2
nome1, dia1, mes, *n = t3

for v in t1:
    print(v)

print(type(t1))
print(t1[1])
print(t1[0:2])
print(nome1)
print(n)

t4 = (1, 2, 3) * 20
print(len(t4))

# tupla para lista
t1 = list(t1)
t1[0] = 'Guilherme'
print(t1)

# lista de volta para tupla
t1 = tuple(t1)
print(t1)

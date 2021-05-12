"""
iteraveis - é um objeto que pode ser iterado mas não é um iterador, não vai retornar um valor de cada vez.
iterador - vai retornar um valor de cada vez.
geradores -
"""
import sys
import time

# iterável
# Para saber se é iterável "hasattr(<objeto>, '__iter__')"
nums = [1, 3, 5]
num = 135
string = "gui"

print(hasattr(nums, '__iter__'))
print(hasattr(num, '__iter__'))
print(hasattr(string, '__iter__'))

# iterador
# Para saber se é iterador "hasattr(<objeto>, '__next__')"
iterador = iter(nums)
print(hasattr(iterador, '__next__'))
print(next(iterador))
print(next(iterador))
print(next(iterador))


# gerador
# exemplo sem gerador
# def gera1():
#     arr = []
#     for n in range(100):
#         arr.append(n)
#         time.sleep(0.1)
#     return arr
#
#
# lista = gera1()
# for numero in lista:
#     print(numero)


# exemplo com gerador
def gera2():
    for n in range(100):
        yield n
        time.sleep(0.1)


gerador = gera2()
for v in gerador:
    print(v)


# gerar gerador na mão
def gera_manual():
    vari = 'Valor 1'
    yield vari
    vari = 'Valor 2'
    yield vari
    vari = 'Valor 3'
    yield vari


manual = gera_manual()
for m in manual:
    print(m)

# diferença tamanhos no sistema
l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))  # comprehension dentro de paranteses cria um gerador

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

# iterar em gerador
for v in l2:
    print(v)

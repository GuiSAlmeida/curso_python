"""
lists, tuples, str -> sequences -> Iterables
**Itaradores e geradores são feitos para consumir os valores uma unica vez
"""

nome = 'guilherme'
iterador = iter(nome)
print(next(iterador))  # g
print('-' * 100)
for valor in iterador:
    print(valor)  # uilherme

gerador = (letra for letra in nome)
print(next(gerador))  # g
print('-' * 100)
for letra in gerador:
    print(letra)  # uilherme

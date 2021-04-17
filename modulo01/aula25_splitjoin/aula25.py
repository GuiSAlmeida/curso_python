"""
Split, join, enumerate
* split - dividi uma string (string)
* join - junta uma lista (string)
* enumerate - enumerar elementos da lista (iteráveis)
"""

string = 'guilherme almeida'

lista_nome = string.split(' ')
print(lista_nome)
for palavra in lista_nome:
    print(palavra)

string2 = '-'.join(lista_nome)
print(string2)

for index, valor in enumerate(lista_nome):
    print(index, valor)

lista = [
    'gui',
    'deia',
]
# desenpacotamento
nome1, nome2 = lista
print(nome1, nome2)

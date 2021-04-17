"""
desempacotamento de lista
"""

lista_nomes = ['gui', 'deia', 'bulma', 'chokito', 'flora']
n1, n2, *resto, ultimo_nome = lista_nomes
print(n1, n2)
print(resto)
print(ultimo_nome)

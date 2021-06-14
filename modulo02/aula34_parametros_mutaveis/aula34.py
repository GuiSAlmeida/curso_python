"""
mutaveis: listas, dicionarios...
imutaveis: tuplas, strings, numeros, booleanos, none...
"""


def lista_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


lista_clientes1 = ['gui', 'deia']
clientes1 = lista_clientes(['joao', 'maria', 'eduardo'], lista_clientes1)
print(clientes1)

# nestes casos a função vai ter comportamento estranho porque o parametro lista passado é mutavel
clientes2 = lista_clientes(['marcos', 'jonas', 'Zico'])
clientes3 = lista_clientes(['chokito', 'bulma'])

print(clientes2)
print(clientes3)


# FORMA CORRIGIDA
def lista_clientesok(clientes_iteravel, lista=''):
    if not lista:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes4 = lista_clientesok(['marcos', 'jonas', 'Zico'])
clientes5 = lista_clientesok(['chokito', 'bulma'])
print(clientes4)
print(clientes5)

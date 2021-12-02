"""
dicionario - estrutura de dados que suporta um par de chave e valor
*chaves são únicas*
"""
# criar dicionario:
import copy
dict1 = {'chave1': 'valor1'}
dict2 = dict(chave3='valor3')

# podem ser usados qualquer dados imutaveis nas chaves
dict3 = {
    'str': 'string',
    123: 'número',
    (1, 2, 3): 'tupla'
}

# criar nova chave e valor:
dict1['chave2'] = 'valor2'
dict1.update({'navachave': 'novovalor'})

# acessar valores passando nome da chave
print(dict1['chave2'])

# checar chave está no dict
if 'não existe' in dict1:
    print('existe')

if dict1.get('str') is not None:
    print(dict1.get('str'))

# excluir chave
del dict3['str']

# consultar apenas as chaves do dict
print(dict3.keys())

# consultar apenas os valores do dict
print(dict3.values())

# quantidade de pares
print(len(dict1))

# loops em dicts
for k in dict1:  # pega as chaves
    print(f'Chave: {k}')
for k in dict1.values():  # pega os valores
    print(f'Chave: {k}')
for k in dict1.items():  # pega os os pares
    print(f'Chave: {k[0]} e valor: {k[1]}')
for k, v in dict1.items():  # desempacotando os pares
    print(f'Chave: {k} e valor: {v}')

# dicionarios dentro de dicionarios
clientes = {
    'cliente1': {
        'nome': 'Gui',
        'sobrenome': 'Almeida'
    },
    'cliente2': {
        'nome': 'Deia',
        'sobrenome': 'Leite'
    }
}

for key, value in clientes.items():
    print(f'Exibindo {key}')
    for dados_key, dados_value in value.items():
        print(f'\t{dados_key} = {dados_value}')


# copiando dicionarios:

# não cria novo dicionario, cria apontamento/referência
# para os mesmos valores no memoria.
novo_dict1 = dict1

# cria uma cópia rasa em um novo dicionario.
# (cópia rasa porque se os dados do dicionario copiado foram mutáveis,
# eles também serão alterados.)
novo_dict2 = dict2.copy()

# Para copiar realmente um novo dicionario
# sem estar linkado com dicionario que foi copiado usa-se:
novo_dict3 = copy.deepcopy(dict3)

# casting para dicionario (listas, tuplas)
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3]
]
dict4 = dict(lista)
print(dict4)

# remover pares do dicionario
dict4.pop('c1')  # remove par de acordo com chave
print(dict4)
dict4.popitem()  # remove sempre o último par
print(dict4)

# concatenar dicionarios
dict4.update(dict3)
print(dict4)

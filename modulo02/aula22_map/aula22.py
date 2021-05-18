"""
map retorna um iterador
"""
from dados import produtos, pessoas, nums


def aumenta_preco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p


new_nums = map(lambda x: x * 2, nums)  # tbm pode ser usado list comprehension para isso
print(list(new_nums))

novos_produtos = map(aumenta_preco, produtos)
for produto in novos_produtos:
    print(produto)

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 2, 2)
    return p


nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)

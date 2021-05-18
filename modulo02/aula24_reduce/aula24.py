from dados import produtos, pessoas, nums
from functools import reduce

soma_lista = reduce(lambda acc, num: num + acc, nums, 0)
print(soma_lista)

soma_precos = reduce(lambda acc, prd: prd['preço'] + acc, produtos, 0)
print(soma_precos)

soma_idades = reduce(lambda acc, pessoa: pessoa['idade'] + acc, pessoas, 0)
media_idades = soma_idades / len(pessoas)
print(media_idades)



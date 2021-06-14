# import vendas.calcs  # importando do pacote vendas e arquivo calcs
# from vendas import calcs  # importando arquivo calcs diretamente de do pacote vendas
from vendas.calcs import aumento, reducao  # importando as funções diretamente arquivo calcs

import vendas.format.preco as formata

preco = 49.9
preco_aumento = aumento(valor=preco, porcentagem=15, formata=True)
preco_reduzido = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_aumento)
print(preco_reduzido)
print(formata.real(preco))

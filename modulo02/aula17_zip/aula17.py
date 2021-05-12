"""
Zip - unindo iteráveis em um iterador que possui next(), *uni até a menor lista.
Zip_longest - no módulo itertools
"""
from itertools import zip_longest, count
from types import GeneratorType

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))
# checa se é uma instancia de um gerador
print(isinstance(variavel, GeneratorType))

indice = count()
cidades = ['São Paulo', 'Florianópolis', 'Salvador', 'Porto Alegre', 'Curitiba']
estados = ['SP', 'SC', 'BA', 'RS']

cidades_estados = zip(
    indice,
    cidades,
    estados
)
# print(list(cidades_estados))
for indice, cidade, estado in cidades_estados:  # usando desempacotamento
    print(indice, cidade, estado)

cidades_estados2 = zip_longest(
    cidades,
    estados,
    fillvalue="Sem Estado"  # fillvalue seta valor padrão para propriedade da lista que faltar
)
print(list(cidades_estados2))

"""
dict comprehension
"""

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

dict1 = {x: y for x, y in tupla}
print(dict1)
dict2 = {x.upper(): y.upper() for x, y in tupla}
print(dict2)
dict3 = {x: y for x, y in enumerate(range(5))}
print(dict3)

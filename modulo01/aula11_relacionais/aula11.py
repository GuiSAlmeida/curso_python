"""
Operadores relacionais
== > >= < <= !=
"""
# print(2 == 2)  # igualdade
# print(2 > 2)  # maior
# print(2 >= 2)  # maior ou igual
# print(2 < 2)  # igualdade
# print(2 <= 2)  # menor ou igual
# print(2 != 2)  # diferente

idade = int(input('Digite sua idade: '))

if idade >= 18 and idade <= 40:
    print('Vc é adulto')
elif idade < 18:
    print('Vc é criança')
else:
    print('Vc é idoso')


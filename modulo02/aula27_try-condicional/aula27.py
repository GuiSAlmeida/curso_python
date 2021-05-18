"""
try except com condicionais
"""


def converte_num(val):
    try:
        val = int(val)
        return val
    except ValueError as error:
        try:
            val = float(val)
            return val
        except ValueError:
            pass  # vai retornar none


num = input('Digite um numero:')
valor = converte_num(num)

if valor is None:
    print('Erro: isso não é um número!')
else:
    print(valor * 5)

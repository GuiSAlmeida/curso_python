"""
Formatando valores com modificadores
:s - texto (string)
:d - Inteiro (int)
:f - Números de ponto flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d ou f)
    > - esquerda
    < - direita
    ^ - centro
"""

nome = 'guilherme'
print(f'{nome:.3s}')
print(f'{nome:#^50}')

num = 1
print(f'{num:0>10}')
print(f'{num:0>10.2f}')

num1 = 10
num2 = 3
div = num1 / num2
print(f'{div:.2f}')



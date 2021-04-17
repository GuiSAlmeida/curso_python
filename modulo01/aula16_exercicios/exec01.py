"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

int_num = input('Digite numero inteiro: ')

try:
    int_num = int(int_num)
    result = int_num % 2 == 0
    if result:
        print(f'{int_num} é par.')
    else:
        print(f'{int_num} é impar.')
except:
    print('Valor digitado está fora do padrão!')

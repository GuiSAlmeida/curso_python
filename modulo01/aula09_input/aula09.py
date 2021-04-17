"""
Entrada de dados
input() sempre retorna string
"""
from datetime import date

nome = input('Qual seu nome? ')
nascimento = input('Qual seu ano de nscimento? ')
ano_atual = date.today().year
idade = ano_atual - int(nascimento)
print(f'{nome} tem {idade} anos.')

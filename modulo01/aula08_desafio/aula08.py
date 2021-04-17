from datetime import date

nome = 'Gui'
idade = 34
altura = 1.80
peso = 74
anoAtual = date.today().year
anoNasc = anoAtual - idade
imc = peso/(altura**2)

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso}Kg.\n'
      f'O IMC de {nome} é {imc:.2f}.\n'
      f'{nome} nasceu em {anoNasc}.')

"""
VARIAVEIS
Iniciar com letra, pode conter números, separar _, letras maiusculas
"""

nome = 'Gui'
idade = 34
altura = 1.80
maior = idade > 18
peso = 74

print('Nome:', nome, type(nome))
print('Idade:', idade, type(idade))
print('Altura:', altura, type(altura))
print('É maior:', maior, type(maior))

print('IMC', peso/(altura**2))

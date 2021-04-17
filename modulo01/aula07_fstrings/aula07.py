nome = 'Gui'
idade = 34
altura = 1.80
maior = idade > 18
peso = 74

print(f'Nome: {nome}', type(nome))
print(f'Idade: {idade}', type(idade))
print(f'Altura: {altura}', type(altura))
print(f'É maior: {maior}', type(maior))

imc = peso/(altura**2)
print(f'IMC é: {imc}')
# imc formatado
print(f'IMC é: {imc:.2f}')

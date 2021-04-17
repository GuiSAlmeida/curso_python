"""
len() - quantidade caracteres strings
string.__len__() método do objeto string
"""

usuario = input('Digite usuario: ')
qtde = len(usuario)

if qtde < 6:
    print('Você precisa digitar pelo menos 6 caracteres!')
else:
    print('Cadastrado no sistema!')

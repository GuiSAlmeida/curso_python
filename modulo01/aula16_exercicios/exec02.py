"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário
descrito, exiba a saudação apropriada.
Exemplo: bom dia 0-11, boa tarde 12-17 e boa noite 18-23.
"""

hora = input('Digite a hora(0-23): ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Hora deve estar entre 0 e 23!')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print('Hora deve estar entre 0 e 23!')

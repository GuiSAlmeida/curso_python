# try:
#     file = open('text.txt', 'w+')
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

with open('text.txt', 'w+') as file:  # gerenciador de contexto, com python funciona assim
    file.write('Linha 1\n')
    file.write('Linha 2\n')

    file.seek(0)
    print(file.read())

with open('text.txt', 'a+') as file:  # append mode | adiciona no final
    file.write('Outra linha\n')

    file.seek(0)
    print(file.read())

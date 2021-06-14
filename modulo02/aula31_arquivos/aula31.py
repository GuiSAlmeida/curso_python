"""
https://docs.python.org/3/library/functions.html#open

file = open('nome arquivo', 'modo')

modos:
'r' - open for reading (default)
'w' - open for writing, truncating the file first
'x' - open for exclusive creation, failing if the file already exists
'a' - open for writing, appending to the end of the file if it exists
'b' - binary mode
't' - text mode (default)
'+' - open for updating (reading and writing)
"""

file = open('text.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')

print('Lendo linhas:')
file.seek(0, 0)  # retorn para inicio do arquivo
print(file.read())
print('-'*20)

file.seek(0, 0)
print(file.readline(), end='')  # lê linha por linha
print(file.readline(), end='')
print('-'*20)

file.seek(0, 0)
print(file.readlines())  # retorna lista com linhas

file.seek(0, 0)
for linha in file:
    print(linha)

file.close()

import os
os.remove('text.txt')  # para apagar arquivo criado

from zipfile import ZipFile
import os

path = r'/home/guilhermedasilva/Documents/'

# criar arquivo zip adicionando arquivos
with ZipFile('./modulo04/aula_compactar/arquivo.zip', 'w') as zip:
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        zip.write(full_path, file)

# ler arquivo zipado
with ZipFile('./modulo04/aula_compactar/arquivo.zip', 'r') as zip:
    for file in zip.namelist():
        print(file)

# descompactar arquivo
with ZipFile('./modulo04/aula_compactar/arquivo.zip', 'r') as zip:
    zip.extractall('./modulo04/aula_compactar/descompactados')

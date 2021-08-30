#!/usr/bin/env python3
import sys
import os

arguments = sys.argv
qtd_args = len(arguments)

if qtd_args <= 1:
    print('Faltando argumentos:')
    print('-a', 'Para listar todos os arquivos nessa pasta.', sep='\t')
    print('-d', 'Para listar todos os diretórios nessa pasta.', sep='\t')
    sys.exit()

only_files = False
only_dirs = False

if '-a' in arguments:
    only_files = True

if '-d' in arguments:
    only_dirs = True

for file in os.listdir('.'):
    if only_files:
        if os.path.isfile(file):
            print(file)

    if only_dirs:
        if os.path.isdir(file):
            print(file)

# path_windows = r'C:\programas\foo'

import os
# import shutil

path = '/home/guilhermedasilva/Workspace/development/teste_python'
path_new = '/home/guilhermedasilva/Workspace/development/curso_python/modulo04/files'

try:
    os.mkdir(path_new)
except FileExistsError:
    print(f'Pasta {path_new} já existe.')

for root, dirs, files in os.walk(path_new):
    for file in files:
        old_path = os.path.join(root, file)
        new_path = os.path.join(path_new, file)

        # Copiando arquivos .py
        # if '.py' in file:
        #     shutil.copy(old_path, new_path)
        #     print(f'Arquivo {file} copiado com sucesso!')

        # Movendo arquivos de uma pasta para outra
        # shutil.move(old_path, new_path)
        # print(f'Arquivo {file} movido com sucesso!')

        # Removendo arquivos .py de uma pasta
        if '.py' in file:
            os.remove(new_path)
            print(f'Arquivo {file} removido com sucesso!')

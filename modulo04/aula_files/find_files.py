import os
from aula_files.utils import size_format

path_find = input('Enter a path: ')
term = input('Enter a term: ')
count = 0
print(path_find)
print(term)


for folder, dirs, files in os.walk(path_find):
    for file in files:
        if term in file:
            try:
                count += 1
                path_file = os.path.join(folder, file)
                name_file, ext_file = os.path.splitext(file)
                size_file = os.path.getsize(path_file)

                print()
                print('File found:', file)
                print('Path:', path_file)
                print('Name:', name_file)
                print('Size:', size_file)
                print('Formated size:', size_format(size_file))
            except PermissionError:
                print('Permission denied!')
            except FileNotFoundError:
                print('File not found!')
            except Exception as e:
                print('Error:', e)

print()
print(f'{count} arquivo(s) encontrado(s).')

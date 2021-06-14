"""
Módulos padrão python
Módulos são arquivos .py (que contém código python)
e servem para expandir as funcionalidades padrão da linguagem.
Veja todos os módulos padrão em:
https://docs.python.org/3/py-modindex.html
"""
# import sys
import random
from sys import platform as so  # cria um alias

print(so)

for i in range(10):
    print(random.randint(0, 10))

"""
Escopo variaveis dentro de funções
"""

variavel = 'var_global'


def func():
    print(variavel)


def func2():
    global variavel  # muda escopo da variavel local para o global
    variavel = 'var_local'
    print(variavel)

func()
func2()
print(variavel)

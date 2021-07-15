"""
public, protected, private
_
__
"""


class BaseDados:
    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    # getter
    @property
    def dados(self):
        return self.__dados

    # setter
    @dados.setter
    def dados(self, valor):
        self.__dados = valor

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDados()
bd.inserir_clientes(1, 'João')
bd.inserir_clientes(2, 'Maria')
bd.lista_clientes()

bd.__dados = 'Outro dado'

print(bd.__dados)
# Outro dado
print(bd._BaseDados__dados)
# {'clientes': {1: 'João', 2: 'Maria'}}



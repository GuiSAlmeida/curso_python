from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.__conta = None

    @property
    def conta(self):
        return self.__conta

    def inserir_conta(self, conta):
        self.__conta = conta

from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=100):
        super().__init__(agencia, numero, saldo)
        self.__limite = limite

    def sacar(self, valor):
        if (self.saldo + self.__limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()

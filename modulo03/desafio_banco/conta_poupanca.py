from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.__saldo < valor:
            print('Saldo insuficiente')
            return

        self.__saldo -= valor
        self.detalhes()

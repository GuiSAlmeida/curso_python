from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.__agencia = agencia
        self.__numero = numero
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    def depositar(self, valor):
        self.__saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.__agencia}', end=' | ')
        print(f'Conta: {self.__numero}', end=' | ')
        print(f'Saldo: {self.__saldo}')

    @abstractmethod
    def sacar(self, valor): pass

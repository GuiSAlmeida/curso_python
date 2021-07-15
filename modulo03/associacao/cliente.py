class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def inseri_enderco(self, cidade, estado):
        self.__enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} foi APAGADO')


class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi APAGADO')

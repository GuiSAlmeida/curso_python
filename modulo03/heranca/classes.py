# superclasse
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_classe = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_classe} falando...')


# subclasses
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_classe} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_classe} estudando...')


# Sobreposição de métodos
class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        super().falar()
        print(f'{self.nome} {self.sobrenome} é vip...')

"""
Associação -> Usa outra classe
Agregação  -> Tem outra classe
Composição -> É dono de outra classe
Herança    -> É outra classe
"""

from classes import Cliente, Aluno, Pessoa, ClienteVip

c1 = Cliente('João', 34)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 20)
print(a1.nome)
a1.falar()
a1.estudar()
print(a1.__dict__)

p1 = Pessoa('Gui', 34)
p1.falar()

c2 = ClienteVip('Deia', 30, 'Leite')
c2.falar()

# multipla herança
from smartphone import Smartphone
cel = Smartphone('Iphone')
cel.conectar()
cel.desligar()
cel.ligar()
cel.conectar()
cel.conectar()
cel.conectar()
cel.desligar()
cel.conectar()
cel.desconectar()
cel.desconectar()


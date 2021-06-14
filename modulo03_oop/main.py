from pessoa import Pessoa

gui = Pessoa('Gui', 34)
deia = Pessoa('Deia', 30)

gui.falar('skate')
deia.falar('filmes')
gui.comer('fruta')

print(Pessoa.ano_atual)
print(gui.get_ano_nasc())

p1 = Pessoa.pessoa_nasc('gui', 1987)
print(p1.nome)
print(p1.gera_id())

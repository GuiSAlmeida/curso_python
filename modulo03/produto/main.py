from produto import Produto

camiseta = Produto('CAMISETA', 50)
camiseta.desconto(10)
print(camiseta.nome)

bone = Produto('BONE', 'R$15')
bone.desconto(10)
print(bone.nome)


class Cls:
    num = 1

inst = Cls()
print(inst.num)
# 1
print(inst.__dict__)
# {}

inst.num = 2
print(inst.num)
# 2
print(inst.__dict__)
# {'num': 2}
print(Cls.num)
# 1

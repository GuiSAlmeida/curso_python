class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')


class D(B, C):
    pass


d = D()
d.falar()
# Falando... Estou em B.
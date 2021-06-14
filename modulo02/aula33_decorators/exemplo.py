from time import time, sleep


def velocidade(fn):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = fn(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA função levou {tempo:.2f}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(1000):
        print(i, end='')


demora()

import math
PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]

def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

if __name__ == '__main__':
    print('MÓDULO CALCULOS')

print(f'Módulo: {__name__}')

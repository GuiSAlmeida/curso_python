# https://docs.python.org/3/library/exceptions.html

def div(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('log: ', error)
        raise  # relança exceção


try:
    print(div(2, 0))
except ZeroDivisionError as error:
    print(error)


def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0!")
    return n1 / n2


print(divide(2, 1))

# capturar exceção customizada
try:
    print(divide(2, 0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
    print('Log:', error)

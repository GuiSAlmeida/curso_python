"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def fizzbuzz(num=0):
    if num == 0:
        return num

    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'

    if num % 3 == 0:
        return 'fizz'

    if num % 5 == 0:
        return 'buzz'

    return num


print(fizzbuzz())
print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(50))
print(fizzbuzz(7))

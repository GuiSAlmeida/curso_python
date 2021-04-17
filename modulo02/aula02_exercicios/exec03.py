"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def percentual(num=0, percent=0):
    return num + (num * percent / 100)


print(percentual(10, 25))

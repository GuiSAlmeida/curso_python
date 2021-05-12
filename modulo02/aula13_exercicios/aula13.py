strings = '01234567890123456789012345678901234567890123456789'

lista = [strings[i: i + 10] for i in range(0, len(strings), 10)]

print(lista)

concat = '.'.join(lista)
print(concat)

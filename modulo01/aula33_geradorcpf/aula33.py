from random import randint

cpf = str(randint(100000000, 999999999))
cpf_novo = cpf
reverso = 10
total = 0
for i in range(19):
    if i > 8:
        i -= 9
    total += int(cpf_novo[i]) * reverso

    reverso -= 1

    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)
        if digito > 9:
            digito = 0
        total = 0
        cpf_novo += str(digito)

print(cpf_novo)

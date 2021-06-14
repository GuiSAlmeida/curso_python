import re
import random


def remove_caracteres(cnpj):
    return re.sub('[^0-9]', '', cnpj)


def is_sequence(cnpj):
    sequence = cnpj[0] * len(cnpj)
    if sequence == cnpj:
        return True
    return False


def remove_dig(cnpj):
    return cnpj[:-2:1]


def calculate_total(total):
    if 11 - (total % 11) > 9:
        return 0
    return 11 - (total % 11)


def total_dig(cnpj, regressivos):
    total = 0
    for index, num in enumerate(cnpj):
        total += int(num) * regressivos[index]
    return total


def generate_dig(cnpj, digito=1):
    regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if digito == 1:
        regressivos = regressivos[1:]

    total = total_dig(cnpj, regressivos)
    novo_cnpj = list(cnpj)
    novo_cnpj.append(str(calculate_total(total)))

    return ''.join(novo_cnpj)


def format_cnpj(cnpj):
    formated = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formated


def valida(cnpj):
    novo_cnpj = remove_caracteres(cnpj)
    novo_cnpj = remove_dig(novo_cnpj)

    if is_sequence(novo_cnpj):
        return False

    parsed_cnpj = generate_dig(novo_cnpj, digito=1)
    new_cnpj = generate_dig(parsed_cnpj, digito=2)

    print(format_cnpj(new_cnpj))
    if new_cnpj == remove_caracteres(cnpj):
        return print('CNPJ válido!')

    return print('CNPJ inválido!')


def generate_cnpj():
    dig1 = random.randint(0, 9)
    dig2 = random.randint(0, 9)
    bloc2 = random.randint(100, 999)
    bloc3 = random.randint(100, 999)
    bloc4 = '0001'

    init_cnpj = f'{dig1}{dig2}{bloc2}{bloc3}{bloc4}'
    new_cnpj = generate_dig(cnpj=init_cnpj, digito=1)
    new_cnpj = generate_dig(cnpj=new_cnpj, digito=2)

    return new_cnpj

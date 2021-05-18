from itertools import groupby, tee

alunos = [
    {'nome': 'Gui', 'nota': 'A'},
    {'nome': 'Deia', 'nota': 'B'},
    {'nome': 'Chokito', 'nota': 'A'},
    {'nome': 'Bulma', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
print(alunos)

alunos_agrupados = groupby(alunos, ordena)
for agrupamento, val_agrupados in alunos_agrupados:
    va1, va2 = tee(val_agrupados)

    print(f'Agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')

    qtde = len(list(va2))
    print(f'\t{qtde} alunos tiraram a nota {agrupamento}\n')

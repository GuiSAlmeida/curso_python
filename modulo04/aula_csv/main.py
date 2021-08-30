import csv

with open('./modulo04/aula_csv/data.csv', 'r') as file:
    data = [x for x in csv.DictReader(file)]
    # data = csv.reader(file)   # reader transforma em listas
    # data = csv.DictReader(file) # retorna dict ordenado

    # next(data)  # para pular primeira linha

    # for line in data:
    #     print(line['nome'], line['sobrenome'], line['telefone'])


with open('./modulo04/aula_csv/data_new.csv', 'w') as file:
    write = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    keys = list(data[0].keys())
    write.writerow(
        [
            keys[0],
            keys[1],
            keys[2],
        ]
    )

    for d in data:
        write.writerow(
            [
                d['nome'],
                d['sobrenome'],
                d['telefone'],
            ]
        )

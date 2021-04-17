"""
expressões lambdas - funções anonimas
"""

lista = [
    ['p1', 13],
    ['p2', 10],
    ['p3', 15],
    ['p4', 18],
    ['p5', 20]
]


# def sort_price(item):
#     return item[1]
#
# lista.sort(key=sort_price)

lista.sort(key=lambda item: item[1])            # altera lista original
print(lista)

nova_lista = sorted(lista, key=lambda i: i[1])  # não altera lista original
print(nova_lista)

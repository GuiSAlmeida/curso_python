"""
While em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores.
"""

count = 0
while count < 10:
    if count % 2 == 0:
        count = count + 1
        continue  # pula loop

    if count == 7:
        break  # finaliza o while

    print(f'>{count}')
    count = count + 1

print('Acabou!')

x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1

    x += 1


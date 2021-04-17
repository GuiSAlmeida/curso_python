"""
While / Else
contadores
acumuladores
"""

count = 0
accumulator = 1
while count <= 10:
    print(count, accumulator)

    if count > 5:
        break
    accumulator = accumulator + count
    count += 1
else:
    print('Cheguei no else!')  # só executa quando a expressão do while passa a ser falsa.

print('Acabou!')

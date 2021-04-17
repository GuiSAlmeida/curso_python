"""
For in em Python
    continue - pula para próxima iteração
    break - para o laço

iterando strings com for
função built-in range(start=0, stop, step=1)
"""
# ex1:
texto = 'python'
novo_texto = ''
for letra in texto:
    if letra == 't':
        novo_texto += letra.upper()
    elif letra == 'h':
        novo_texto += letra.upper()
        break
    else:
        novo_texto += letra

print(novo_texto)

# ex2:
for num in range(10):
    print(num)

# ex3
for num in range(20, 10, -1):
    print(num)

"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Vocẽ pode conferir tudo isso em:
    https://docs.python.org/3/library/stdtypes.html (tipos built-in)
    https://docs.python.org/3/library/functions.html (funções built-in)
"""

texto       = 'python_3'
# positivos   [01234567]
# negativos  -[87654321]

print(texto[0])     # p
print(texto[-8])    # p

# fatiamento string
print(texto[2:6])   # thon
print(texto[:2])    # py

# pular indices no fatiamento (step)
print(texto[1::2])  # yhn3


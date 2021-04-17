#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
count = 0
string = ''
while count < tamanho_frase:
    print(frase[count], count)
    if frase[count] == 'r':
        string += 'R'
    else:
        string += frase[count]
    count += 1

print(string)

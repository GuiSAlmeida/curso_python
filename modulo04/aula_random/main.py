import random
import string

# inteiro = random.randint(10, 20)
inteiro = random.randrange(900, 1000, 10)
print(inteiro)

# flut = random.uniform(10, 20)
flut = random.random()
print(flut)

lista = ['gui', 'deia', 'chokito', 'bulma']
random.shuffle(lista)  # embaralha a lista
print(lista)

# sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2) # repete valores iguais
sorteio = random.sample(lista, 2)  # não repete valores iguais
print(sorteio)

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres

senha = "".join(random.choices(geral, k=20))
print(senha)

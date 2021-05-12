carrinho = []

carrinho.append(('Prod 1', 30))
carrinho.append(('Prod 2', 20))
carrinho.append(('Prod 3', 50))

total = sum([valor[1] for valor in carrinho])
print(total)

class CarrinhoCompras:
    def __init__(self, ):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome}: R${produto.valor}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return f'R${total}'

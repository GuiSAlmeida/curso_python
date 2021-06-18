from escritor import Escritor
from caneta import Caneta
from maquina import MaquinaEscrever
from carrinho import CarrinhoCompras
from produto import Produto
from cliente import Cliente, Endereco

# Associação
escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaEscrever()
escritor.ferramenta = maquina
# escritor.ferramenta.escrever()

# Agregação
carrinho = CarrinhoCompras()
p1 = Produto('Bone', 50)
p2 = Produto('cueca', 20)
p3 = Produto('tenis', 150)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
# carrinho.lista_produtos()
# print(carrinho.soma_total())

# Composição
cliente1 = Cliente('João', 32)
cliente2 = Cliente('Maria', 22)
cliente1.inseri_enderco('Florianópolis', 'SC')
cliente2.inseri_enderco('Porto Alegre', 'RS')
print(cliente1.nome)
cliente1.lista_enderecos()
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente1
print('#'*30)



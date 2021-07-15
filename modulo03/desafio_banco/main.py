from banco import Banco
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

cc = ContaCorrente(111, 22, 0)
cp = ContaPoupanca(222, 22, 0)

gui = Cliente('Gui', 34)
deia = Cliente('Deia', 30)

gui.inserir_conta(cc)
deia.inserir_conta(cp)

itau = Banco()
itau.inserir_conta(cc)
itau.inserir_cliente(gui)
itau.inserir_cliente(deia)


if itau.autenticar(gui):
    gui.conta.depositar(40)
    gui.conta.sacar(60)
else:
    print('Cliente não autenticado')

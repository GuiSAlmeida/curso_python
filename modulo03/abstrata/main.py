from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente


poup = ContaPoupanca(123, 9999, 500)
poup.depositar(100)
poup.sacar(50)
poup.sacar(551)

corr = ContaCorrente(agencia=222, conta=3333, saldo=0, limite=500)
corr.depositar(100)
corr.sacar(250)

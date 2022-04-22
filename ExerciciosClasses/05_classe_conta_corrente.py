"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional,
com valor default zero e os demais atributos são obrigatórios.
"""

class ContaCorrente():
    def __init__(self, nome_correntista, numero_conta, saldo=0):
        self.nome_correntista = nome_correntista
        self.numero_conta = numero_conta
        self.saldo = saldo

    def mostra_conta(self):
        return self.nome_correntista, self.numero_conta, self.saldo

    def alterarNome(self, nome_correntista):
        self.nome_correntista = nome_correntista
        return self.nome_correntista

    def deposito(self, deposito):
        self.saldo += deposito
        return self.saldo

    def saque(self, saque):
        self.saldo -= saque
        return self.saldo

if __name__ == '__main__':
    conta_igor = ContaCorrente("Igor", 123456)
    print(conta_igor.mostra_conta())

    conta_igor.alterarNome("Cecilia")
    print(conta_igor.mostra_conta())

    conta_igor.deposito(100)
    print(conta_igor.mostra_conta())

    conta_igor.saque(50)
    print(conta_igor.mostra_conta())


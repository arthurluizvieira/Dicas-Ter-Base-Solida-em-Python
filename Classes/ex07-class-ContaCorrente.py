# Crie uma classe chamada ContaCorrente que modele uma conta corrente:
# atributos: número da conta saldo / métodos: depositar, sacar, exibir saldo

class ContaCorrente:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Valor de R${valor} depositado com sucesso! Seu saldo atual é de R${self.saldo}!')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'O valor de R${valor} foi sacado com sucesso! Seu novo saldo é de R${self.saldo}')
        else:
            print("Saldo insuficiente!")

    def exibir_saldo(self):
        print(f'Seu saldo atual é de R${self.saldo}!')

conta = ContaCorrente('190987', 250)
conta.exibir_saldo()
conta.depositar(650)
conta.exibir_saldo()
conta.sacar(200)
conta.exibir_saldo()
# Crie uma classe Conta Bancaria com os seguintes atributos: titular, saldo.
# Adicionar métodos para depositar e sacar dinheiro. 
# Crie uma instancia que faça alguns depositos e saques e mostre o saldo final

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'''O valor {valor} depositado, foi adicionado com sucesso na conta, seu saldo
              final é de R${self.saldo}!''')
        
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo - valor
            print(f'''O valor {valor} foi creditado com sucesso!
            seu saldo final é de R${self.saldo}!''')
        else:
            print('Saldo Insuficiente!')

conta = ContaBancaria('Arthur', 1000)
conta.depositar(1000)
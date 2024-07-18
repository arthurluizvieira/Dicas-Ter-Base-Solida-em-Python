# Criar duas classes Conta Corrente e Conta Poupança ambas derivadas de uma classe Conta 
# A classe base deve ter atributos numero e saldo e metodos para depositar e sacar dinheiro
# A classe conta corrente deve ter limite de cheque especial enquanto a classe ContaPoupanca 
# deve ter metodo para adicionar rendimento

class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    
    def consultar_saldo(self):
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, numero, saldo=0, limite=500):
        super().__init__(numero, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo e limite insuficientes.")

class ContaPoupanca(Conta):
    def adicionar_rendimento(self, percentual):
        self.saldo += self.saldo * (percentual / 100)

# Teste das classes
conta_corrente = ContaCorrente(1234, 1000)
conta_corrente.sacar(1300)
print("Saldo Conta Corrente:", conta_corrente.consultar_saldo())

conta_poupanca = ContaPoupanca(5678, 1000)
conta_poupanca.adicionar_rendimento(5)
print("Saldo Conta Poupança:", conta_poupanca.consultar_saldo())

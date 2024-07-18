class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, quantia):
        if quantia > 0:
            self.__saldo += quantia
        else:
            print("Quantia deve ser positiva")

    def sacar(self, quantia):
        if 0 < quantia <= self.__saldo:
            self.__saldo -= quantia
        else:
            print("Saldo insuficiente ou quantia inválida")

    def obter_saldo(self):
        return self.__saldo  # Método público para acessar o saldo

# Utilizando a classe ContaBancaria
conta = ContaBancaria(100)
print(conta.obter_saldo())  # 100

conta.depositar(50)
print(conta.obter_saldo())  # 150

conta.sacar(30)
print(conta.obter_saldo())  # 120

# Tentativa de acessar o saldo diretamente resulta em erro
# print(conta.__saldo)  # AtributoError: 'ContaBancaria' object has no attribute '__saldo'

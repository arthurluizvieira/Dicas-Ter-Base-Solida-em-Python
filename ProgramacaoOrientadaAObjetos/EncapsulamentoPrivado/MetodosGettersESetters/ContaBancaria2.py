class ContaBancaria:
        def __init__(self, nome: str, conta: str, saldo : float = 0.0) -> None:
            self.__nome = nome
            self.__conta = conta
            self.__saldo = saldo
        
        @property #representação do getter e setter
        def nome(self) -> str:
            return self.__nome
        
        @nome.setter # representação setter
        def nome(self, novoNome) -> None:
            self.__nome = novoNome
        
        @property
        def conta(self) -> str:
            return self.__conta
        
        @conta.setter
        def conta(self, novaConta) -> None:
            self.__conta = novaConta
        
        @property
        def saldo(self) -> float :
            return self.__saldo
        
        def depositar(self, valor : int) -> None:
            if isinstance (valor, int ):
                if valor > 0:
                    self.__saldo += valor
                else:
                    print('Valor deve ser maior que zero!')
            else:
                print('Por favor, digite um número!')
        
        
        def sacar(self, valor:int) -> None:
            if isinstance (valor, int):
                if valor <= self.__saldo:
                    self.__saldo -= valor
                else:
                    print('Saldo insuficiente!')
            else:
                print('por favor, digite um número válido!')

conta1 = ContaBancaria('Dev TH', '12345')
conta1.depositar(1000)
conta1.sacar(999)
print(conta1.saldo)
print(conta1.conta)
conta1.conta = '2'
print(conta1.conta)
class ContaBancaria:
    def __init__(self, titular:str, saldo:int) -> None:
        self.__titular = titular
        self.__saldo = saldo
    
    def get_titular(self) -> str:
        return self.__titular
    
    def set_titular(self, novo_nome:str) -> None:
        if isinstance(novo_nome, str):
            self.__titular = novo_nome

    def get_saldo(self) -> int:
        return self.__saldo

    def set_saldo(self, novoSaldo:int) -> None:
        if isinstance(novoSaldo, int):
            self.__saldo = novoSaldo
    
    def depositar(self, valor:int) -> None:
        if isinstance(valor, int):
            self.__saldo += valor
        else:
            print('Por favor, digite um valor válido!')
    
    def sacar(self, valor:int) -> None:
        if isinstance(valor, int):
            if self.__saldo >= valor:
                self.__saldo -= valor
            else: 
                print('Digite um valor que você possua em conta!')
        else: 
            print('Digite um valor válido!')


conta1 = ContaBancaria('Arthur Yokomizo', 1500)
conta1.depositar(650)
print(conta1.get_saldo())
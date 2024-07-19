class Carro:
    def __init__(self, marca:str, modelo:str, ano: int, preco: float) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__preco = preco
    
    @property
    def marca(self) -> str:
        return self.__marca
    
    @marca.setter
    def marca(self, marca:str)->None:
        self.__marca = marca
    
    @property
    def modelo(self)-> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo:str)->None:
        self.__modelo = modelo
    
    @property
    def ano(self) -> int:
        return self.__ano
    
    @ano.setter
    def ano(self, ano:int)->None:
        self.__ano = ano
    
    @property
    def preco(self)->float:
        return self.__preco
    
    def __calcularDesconto(self, porcentagem:int)->None:
        desconto = (porcentagem / 100) * self.__preco
        return self.__preco - desconto
    
    def aplicarDesconto(self, porcentagem):
        self.__preco = self.__calcularDesconto(porcentagem)

carro1 = Carro('Honda', 'Civic', 2012, 57400)
print(carro1.preco)
carro1.aplicarDesconto(10)
print(carro1.preco)
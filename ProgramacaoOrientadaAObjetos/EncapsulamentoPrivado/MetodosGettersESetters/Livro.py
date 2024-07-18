class Livro:
    def __init__(self, titulo: str, autor: str, preco:float)-> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__preco = preco
    
    @property
    def titulo(self)-> str: 
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo) -> None:
        self.__titulo = titulo
    
    
    @property
    def autor(self) -> str:
        return self.__autor
    
    @autor.setter
    def autor(self, autor)-> None:
        self.__autor = autor
    

    @property
    def preco(self) -> float:
        return self.__preco

    def desconto(self, porcentagem: float) -> float:
        if isinstance(porcentagem, float):    
            desconto = (self.__preco * porcentagem) / 100
            descontoFinal = self.__preco - desconto
            return descontoFinal
        else:
            print('Digite uma porcentagem válida!')

livro1 = Livro('POO Python', 'dev.ArthurYokomizo', 139.90)
print(livro1.desconto(10.0))

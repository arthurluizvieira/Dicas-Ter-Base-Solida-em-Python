class Produto:
    def __init__(self, nome: str, categoria: str, preco: float) -> None:
        self.__nome = nome
        self.__categoria = categoria
        self.preco = preco  # Utilize o setter para validar o preço

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: str) -> None:
        self.__categoria = categoria

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float) -> None:
        self.__validar_preco(preco)

    def __validar_preco(self, preco: float) -> None:
        if preco > 0:
            self.__preco = preco
        else:
            raise ValueError('O preço não pode ser abaixo ou igual a zero!')

    def __validar_desconto(self, desconto: int) -> float:
        if 0 <= desconto <= 100:
            desconto1 = (self.__preco * desconto) / 100
            desconto_final = self.__preco - desconto1
            return desconto_final
        else:
            raise ValueError('O desconto deve estar entre 0 e 100!')

    def aplicar_desconto(self, desconto: int) -> float:
        return self.__validar_desconto(desconto)

# Teste da classe Produto
try:
    produto1 = Produto('Teclado', 'Informatica', -1)
except ValueError as e:
    print(e)  # O preço não pode ser abaixo ou igual a zero!

produto2 = Produto('Teclado', 'Informatica', 150.00)
print(produto2.nome)          # Teclado
print(produto2.categoria)     # Informatica
print(produto2.preco)         # 150.00
print(produto2.aplicar_desconto(10))  # 135.00


try:
    print(produto2.aplicar_desconto(110))
except ValueError as e:
    print(e)  # O desconto deve estar entre 0 e 100!

# Crie uma classe chamada Livro com os seguintes atributos: titulo, autor, preco
# adicione um metodo aplicar desconto que aplica desconto ao preço do livro
# crie uma instancia e aplique um desconto

class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        desconto = self.preco * porcentagem / 100
        self.preco = self.preco - desconto
        print(f'Com o valor do desconto de {porcentagem}%, irá ficar R${self.preco}!')

compra1 = Livro('A saga das classes', 'emicith', 150)
compra1.aplicar_desconto(15)
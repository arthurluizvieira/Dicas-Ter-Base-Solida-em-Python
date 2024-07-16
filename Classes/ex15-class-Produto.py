# crie uma classe chamada Produto que possui os seguintes atributos: nome, preco, quantidade
# a classe deve ter os seguintes métodos: vender, repor

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def vender(self, quantidade):
        self.quantidade -= quantidade
    
    def repor(self, quantidade):
        self.quantidade += quantidade
    
    def exibirInformacoes(self):
        print('----------')
        print(f'''Produto: {self.nome} 
Preço = {self.preco} 
Quantidade = {self.quantidade}''')
        print('----------')
        
produto1 = Produto('Teclado', 150, 100)
produto1.vender(10)
produto1.repor(20)
produto1.exibirInformacoes()
produto1.vender(50)
produto1.exibirInformacoes()

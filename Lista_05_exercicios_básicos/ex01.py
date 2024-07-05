class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def apresentacao(self):
        print(f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}!')

pessoa = Pessoa('Arthur', '18', 'Arapongas')
pessoa.apresentacao()

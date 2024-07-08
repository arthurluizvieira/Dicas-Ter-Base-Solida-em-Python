# Exercicio 1 - Criar uma classe pessoa com os atributos de nome, idade e sexo
# e adicionar método mostrar informações e criar 2 instâncias da classe para 
# chamar o método mostrar informações para cada uma!

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome 
        self.idade = idade
        self.sexo = sexo

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}.')

pessoa1 = Pessoa('Arthur Luiz', '18', 'Masculino')
pessoa2 = Pessoa('Luiz Alberto', '62', 'Masculino')

pessoa1.mostrar_informacoes()
pessoa2.mostrar_informacoes()
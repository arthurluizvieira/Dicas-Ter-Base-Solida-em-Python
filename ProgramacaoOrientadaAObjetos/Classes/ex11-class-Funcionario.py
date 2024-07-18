# crie uma classe Funcionario que tenha os atributos: nome, salario , cargo
# implementar metodos para aumentar salario em porcentagem e exibir as informações na tela 

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, porcentagem):
        self.salario = self.salario * porcentagem / 100 + self.salario
        

    def exibir_informacoes(self):
        print(f'Funcionário: {self.nome}')
        print(f'Salário: {self.salario}')
        print(f'Cargo: {self.cargo}')

funcionario1 = Funcionario('Arthur', 1050, 'Estagiário')
funcionario1.aumentar_salario(10)
funcionario1.exibir_informacoes()
# Crie uma classe chamada Aluno com os seguintes atributos: nome , nota
# adicione um método mostrar_status que exibe se o aluno foi aprovado (nota >=7)
# ou reprovado (nota <=7) criar uma instancia e mostrar o status

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def mostrar_status(self):
        if self.nota >= 7:
            print(f'{self.nome} está aprovado!')
        else:
            print(f'{self.nome} está reprovado!')

aluno1 = Aluno('Arthur Luiz', 8)
aluno1.mostrar_status()
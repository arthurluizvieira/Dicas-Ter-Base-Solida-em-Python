# Crie uma classe Aluno que tenha os atributos: nome, lista de notas 
# implementar métodos para adicionar uma nota calcular média e verificar se foi aprovado ou não

class AlunoComNotas:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self,nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificacao_aprovacao(self):
        media = self.calcular_media()

        if media >= 6:
            print(f'Aluno {self.nome} aprovado com {media:.2f} de média!')
        else:
            print(f'Aluno {self.nome} reprovado com {media:.2f} de média!')

aluno1 = AlunoComNotas('Arthur Luiz')
aluno1.adicionar_nota(10)
aluno1.adicionar_nota(5)
aluno1.adicionar_nota(6)
aluno1.calcular_media()
aluno1.verificacao_aprovacao()

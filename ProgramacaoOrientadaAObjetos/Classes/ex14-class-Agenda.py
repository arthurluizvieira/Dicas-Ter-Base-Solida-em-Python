# Crie uma classe Agenda que pode armazenar contatos. Cada contato deve ter nome, telefone e email. 
# Implemente métodos para adicionar um contato, remover um contato e listar todos os contatos.

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir_contato(self):
        print(f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}")

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        self.contatos = [contato for contato in self.contatos if contato.nome != nome]

    def listar_contatos(self):
        for contato in self.contatos:
            contato.exibir_contato()

# Teste da classe
agenda = Agenda()
contato1 = Contato("Ana", "1234-5678", "ana@example.com")
contato2 = Contato("Pedro", "8765-4321", "pedro@example.com")
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
agenda.listar_contatos()
agenda.remover_contato("Ana")
agenda.listar_contatos()

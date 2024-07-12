# Crie uma classe chamada CLiente que modele um cliente de uma loja
# com os seguintes atributos: nome, idade, email
# métodos: atualizar email , mostrar dados

class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def atualizar_email(self, novo_email):
        self.email = novo_email
        print('Novo e-mail cadastrado com sucesso!')

    def mostrar_dados(self):
        print(f'''Os dados do cliente são:
Nome: {self.nome}
Idade: {self.idade}
E-mail: {self.email}''')
    
cliente1 = Cliente('Arthur Luiz', 18, 'arthurluizvieiray@gmail.com')
cliente1.mostrar_dados()
cliente1.atualizar_email('arthurluizvla@gmail.com')
cliente1.mostrar_dados()
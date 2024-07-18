# class Pessoa:
#     def __init__(self, nome, idade, cpf):
#         self.__nome = nome ## atributos privados
#         self.__idade = idade ## atributos privados
#         self.__cpf = cpf ## atributos privados

#     def exibirInformacoes(self):
#         print('-------')
#         print('Informações Pessoais:}')
#         print('-------')
#         print(f'''Nome: {self.__nome}
# Idade: {self.__idade}
# Cpf: {self.__cpf}''')
#         print('-------')
    
# pessoa1 = Pessoa('Arthur', 18, '000.000.000-00')
# pessoa1.exibirInformacoes()


class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    def __apresentarDocumento(self): # método e atributos privados, acesso somente pela classe!
        print(self.__cpf)
    
    def beber(self, bebida): 
        if bebida == 'cerveja':
            self.__apresentarDocumento() # chamando método privado para verificação de menor idade
        print('Bebendo...')

pessoa1 = Pessoa('Arthur', 18, 'xxx.xxx.xxx-xx')
pessoa1.beber('cerveja')

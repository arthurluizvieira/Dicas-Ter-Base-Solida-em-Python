# Criar classe Carro que modele um carro com os seguintes atributos: marca, modelo, ano, velocidade
# com os seguintes métodos: acelerar, frear, mostrar velocidade


class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valordesacelerar):
        self.velocidade -= valordesacelerar

    def mostrar_velocidade(self):
        return self.velocidade

carro = Carro('Chevrolet', 'Spin', 2012, 100)

carro.frear(20)
print(carro.mostrar_velocidade())
carro.acelerar(100)
print(carro.mostrar_velocidade())
carro.frear(30)
print(carro.mostrar_velocidade())
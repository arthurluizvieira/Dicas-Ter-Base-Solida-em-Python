# Crie uma classe chamada Bola com os seguintes atributos: cor, circunferencia , material
# com a funcionalidade de trocar e mostrar cor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor
    
bola1 = Bola('azul', '20cm', 'Couro')
print(bola1.cor)
bola1.trocar_cor('rosa')
print(bola1.mostrar_cor())
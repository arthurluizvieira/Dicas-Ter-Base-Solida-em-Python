# Crie uma classe Retângulo com os atributos: largura , altura
# Adicionar métodos para calcular a área e perímetro do retangulo
# criar uma instancia da classe e calcular a área e o perímetro do retangulo

# área = altura x largura
# perímetro = 2 x (base + altura)


class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.altura * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)
    
calcular_retangulo = Retangulo(5, 10)
print(f'''A área do Retângulo é de {calcular_retangulo.calcular_area()}
      O Perímetro do Retângulo é de {calcular_retangulo.calcular_perimetro()}''')
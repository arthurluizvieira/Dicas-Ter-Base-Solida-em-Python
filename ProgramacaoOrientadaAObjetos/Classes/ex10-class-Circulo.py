# Crie uma classe Circulo que contenha o atributo raio com métodos para calcular 
# área e circunferência do circulo

import math 

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2
    
    def circunferencia(self):
        return 2 * math.pi * self.raio
    
circulo1 = Circulo(5)
print(circulo1.area())
print(circulo1.circunferencia())
class Calculadora:
    def Soma(self, a, b):
        return a + b
    
    def Subtracao(self, a , b):
        return a - b
    
    def Multiplicacao(self, a , b):
        return a * b
    
    def Divisao(self, a , b):
        return a / b
    
calculadora = Calculadora()
print('Soma: ', calculadora.Soma(10, 10))
print('Soma: ', calculadora.Subtracao(100, 100))
print('Soma: ', calculadora.Multiplicacao(10, 10))
print('Soma: ', calculadora.Divisao(10, 2))

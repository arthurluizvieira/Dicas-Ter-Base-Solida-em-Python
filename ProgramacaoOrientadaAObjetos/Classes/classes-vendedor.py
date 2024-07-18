''''
vendedor = 'Th'
vendas = 1000
meta = 500

if vendas >= meta:
    print('Bateu a Meta!')
else:
    print('nÃO BATEU A META!')
'''

# TRANSFORMAR TUDO ISSO EM 1 CLASSE

#class Vendedor():
#    def __init__(self, nome):
#        self.nome = nome
#        self.vendas = 0

#    def vendeu(self, vendas):
#        self.vendas = vendas
    
#    def bateu_meta(self, meta):
#        if self.vendas > meta:
#            print(self.nome, 'Bateu a meta!')
#        else:
#            print(self.nome, 'Não bateu a meta!')

from vendedor import Vendedor

vendedor1 = Vendedor('Arthur')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(1000)

vendedor2 = Vendedor('Viviane')
vendedor2.vendeu(100)
vendedor2.bateu_meta(99)
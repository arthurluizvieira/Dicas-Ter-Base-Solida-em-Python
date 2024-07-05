'''
Exercício de Python 3: quem gastou mais dinheiro?
Neste exercício, você possui duas listas de Python. 
Cada lista representa os gastos do mês de dois amigos, João e Pedro. 
Cada valor na lista representa o gasto em uma das semanas do mês:

'''
gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)

if total_joao > total_pedro:
    print('João gastou mais do que Pedro.')
elif total_joao < total_pedro:
    print('Pedro gastou mais do que João.')
else:
    print('Pedro e João gastaram o mesmo valor.')
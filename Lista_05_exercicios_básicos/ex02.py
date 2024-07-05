# Exercício de Python 2: média de uma lista
# Seguimos agora para um exercício clássico de Python. Dada uma lista de números em Python: 
# numeros = [10, 20, 30, 40, 50]
# Calcule a média dos valores dessa lista.

numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print("A média dos números é:", media)
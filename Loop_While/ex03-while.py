#3. Faça um programa, utilizando while e listas, 
# que permita o usuário escrever o nome de cinco pessoas e os mostre na tela.

c = 0
cinco_pessoas = []
while c < 5:
    pessoa = input(f'Digite o nome da {c+1}° pessoa: ')
    cinco_pessoas.append(pessoa)
    c += 1
    print(f'O nome das cinco pessoas cadastradas são: {cinco_pessoas}')
    
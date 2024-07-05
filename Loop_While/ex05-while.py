#5. Faça um programa, utilizando while e listas, 
# que permita o usuário realizar o cadastro de um número indeterminado de pessoas enquanto quiser 
# e os mostre na tela ao finalizar.

'''

print('-=' * 10)
print('Cadastro de Funcionários - Digite 0 para terminar o cadastro')
print('-=' * 10)


c = 0
funcionarios = []


while True:
    funcionario = input(f'Digite o nome do {c+1}° funcionário: ')
    funcionarios.append(funcionario)
    c += 1
    if funcionario == '0':
        print(f'Os funcionários cadastrados no sistema são: {funcionarios}!')
        print('-=' * 10)
        print('Fim do programa')
        print('-=' * 10)
        break

        '''


print('-=' * 10)
print('Cadastro de Funcionários - Digite 0 para terminar o cadastro')
print('-=' * 10)

c = 0
funcionarios = []

while True:
    funcionario = input(f'Digite o nome do {c+1}° funcionário: ')
    if funcionario == '0':
        break
    funcionarios.append(funcionario)
    c += 1

print('-=' * 10)
print('Os funcionários cadastrados no sistema são:')
for i, nome in enumerate(funcionarios, start=1):
    print(f'{i}° Funcionário: {nome}')
print('-=' * 10)
print('Fim do programa')
print('-=' * 10)

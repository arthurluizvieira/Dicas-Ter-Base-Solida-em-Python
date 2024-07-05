#4. Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

print('-=' * 10)
print('Operação - Adição')
print('-=' * 10)

while True:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é de {soma}!')
    continuar = input('Deseja calcular a soma de mais algum número?[S/N]: ').upper()
    if continuar != 'S':
        print('-=' * 10)
        print('Fim do Programa!')
        print('-=' * 10)
        break
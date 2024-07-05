# Escreva um programa que solicite ao usuário dois números e a operação desejada 
# (adição, subtração, multiplicação, divisão) e exiba o resultado da operação.

print('-=' * 10)
print('Calculadora Simples!')
print('-=' * 10)


while True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    soma = n1 + n2
    sub = n1 - n2 
    multiplicacao = n1 * n2 
    divisao = n1 / n2

    escolha = int(input('''Escolha uma opção para iniciar!
                        1 - Adição
                        2 - Subtração
                        3 - Multiplicação
                        4 - Divisão
                        0 - Sair
                        Sua escolha: '''))
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é de: {soma}')
    elif escolha == 2:
        print(f'A subtração entre {n1} e {n2} é de: {sub}!')
    elif escolha == 3:
        print(f'A multiplicação entre {n1} e {n2} é de: {multiplicacao}!')
    elif escolha == 4:
        print(f'A divisão entre {n1} e {n2} é de: {divisao}!')
    elif escolha == 0:
        print('Fim do Programa!')
        break

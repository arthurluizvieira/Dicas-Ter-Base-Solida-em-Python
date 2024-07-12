from random import choice

print('-=' * 10)
print('Bem vindo ao jogo: Pedra, Papel e Tesoura!')
print('-=' * 10)

opcoes = ['Pedra', 'Papel', 'Tesoura']
Pedra = 0
Papel = 1
Tesoura = 2

computador = choice(opcoes)

jogador = int(input('''Faça sua jogada: 
[0] Pedra
[1] Papel
[2] Tesoura
Escolha uma opção acima: '''))

# Caso jogador faça uma escolha inválida
if jogador not in [0, 1, 2]:
    print('Escolha inválida!')

else:
    jogador_escolha = opcoes[jogador]

    # Caso computador jogue Pedra
    if computador == 'Pedra' and jogador_escolha == 'Pedra':
        print(f'O computador escolheu {computador}')
        print('Empate')
    elif computador == 'Pedra' and jogador_escolha == 'Papel':
        print(f'O computador escolheu {computador}')
        print('Vitória do jogador')
    elif computador == 'Pedra' and jogador_escolha == 'Tesoura':
        print(f'O computador escolheu {computador}')
        print('Vitória do Computador')

    # Caso computador jogue Papel
    elif computador == 'Papel' and jogador_escolha == 'Pedra':
        print(f'O computador escolheu {computador}')
        print('Vitória do Computador')
    elif computador == 'Papel' and jogador_escolha == 'Papel':
        print(f'O computador escolheu {computador}')
        print('Empate')
    elif computador == 'Papel' and jogador_escolha == 'Tesoura':
        print(f'O computador escolheu {computador}')
        print('Vitória do jogador')

    # Caso computador jogue Tesoura
    elif computador == 'Tesoura' and jogador_escolha == 'Pedra':
        print(f'O computador escolheu {computador}')
        print('Vitória do jogador')
    elif computador == 'Tesoura' and jogador_escolha == 'Papel':
        print(f'O computador escolheu {computador}')
        print('Vitória do Computador')
    elif computador == 'Tesoura' and jogador_escolha == 'Tesoura':
        print(f'O computador escolheu {computador}')
        print('Empate')

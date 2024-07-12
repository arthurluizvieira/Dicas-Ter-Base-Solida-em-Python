from random import randint

print('-=' * 10)
print('Bem-vindo ao game: Adivinhe o Número!')
print('-=' * 10)

adivinhe = randint(1, 10)

while True:
    
    numero = int(input('Escolha um número de 1 a 10: '))
    if numero != adivinhe:
        print('Ah que pena, não é esse! Tente Novamente!')
    else:
        print('Parabéns, você acertou o número!')
        break


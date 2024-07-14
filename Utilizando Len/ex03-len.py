# escreva um programa que leia uma frase do usuário e conte quantas palavras tem essa frase

frase = input('Digite uma frase: ')
palavras = frase.split()
print(f'A frase {frase} tem {len(palavras)} palavras!')

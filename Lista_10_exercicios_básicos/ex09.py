frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contagem = sum(1 for letra in frase if letra in vogais)
print(f"A frase contém {contagem} vogais.")

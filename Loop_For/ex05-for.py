# Contar ocorrencias de um caractere

string = "abracadabra"
caractere = "a"
contador = 0
for char in string:
    if char == caractere:
        contador += 1
print(f"O caractere '{caractere}' aparece {contador} vezes na string.")

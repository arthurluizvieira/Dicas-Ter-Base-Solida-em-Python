lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
tamanho_lista1 = len(lista1)
tamanho_lista2 = len(lista2)

if tamanho_lista1 > tamanho_lista2:
    print('Lista 1 maior que lista 2')
elif tamanho_lista2 > tamanho_lista1:
    print('Lista 2 maior que lista 1')
elif tamanho_lista1 == tamanho_lista2:
    print('Listas iguais!')
n1 = int(input('Digite um número para verificar o maior: '))
n2 = int(input('Digite um número para verificar o maior: '))
n3 = int(input('Digite um número para verificar o maior: '))

if n1 > n2 and n1 > n3: # se o 1 for maior
    print(f'O maior número inserido é de valor {n1}!') 
elif n2 > n1 and n2 > n3: # se o 2 for maior
    print(f'O maior número é de valor {n2}!')
elif n3 > n2 and n3 > n1: # se o 3 for maior
    print(f'O maior número é de valor {n3}')
elif n1 == n2 and n1 > n3: # se o 1 for igual a 2 
    print(f'Maiores valores é de {n1}')
elif n1 == n3 and n1 > n2: # se o 1 for igual a 3
    print(f'Maiores valores é de {n1}')
elif n2 == n3 and n2 > n1: # se o 2 for igual a 3
    print(f'Maiores valores é de {n2}')


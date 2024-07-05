num = int(input('Digite um número para ver sua tabuada: '))

print(f'Tabuada do {num}:')
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')

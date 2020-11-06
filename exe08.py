# Exercicio 08

palavra = str(input('Digite uma palavra: '))

if palavra == palavra[::-1]:
    print(f'A palavra digitida foi {palavra}\n'
          f'Ao contrario {palavra[::-1]}\n'
          f'A palavra é um palindromo')
else:
    print('A palavra digitada não é um palindromo!')


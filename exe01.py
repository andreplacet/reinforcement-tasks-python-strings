# Exercicio 01

print('Comparador de strings')

string_1 = str(input('Digite uma frase: ')).strip().split()
print(f'String 1: {string_1}')
string_1 = ''.join(string_1)

string_2 = str(input('Digite uma frase: ')).strip().split()
print(f'String 2: {string_2 = }')
string_2 = ''.join(string_2)

print(f'Tamanho da String 1 :{len(string_1)}\n'
      f'Tamanho da String 2: {len(string_2)}')

if string_1 == string_2:
    print('As strings possuem o mesmo conteudo!')
else:
    print('As strings não possuem o mesmo conteudo!')

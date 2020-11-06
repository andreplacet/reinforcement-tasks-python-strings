# Exercicio 07

lista = []

frase = str(input('Digite uma frase: '))

espacos = frase.count(' ')

for i in frase:
    if i in ('a', 'e', 'é', 'i', 'o', 'u'):
        lista.append(i)

print(f'A frase digitada foi:{frase}\n'
      f'a frase contém {espacos} espaços em branco\n'
      f'e {len(lista)} vogais')

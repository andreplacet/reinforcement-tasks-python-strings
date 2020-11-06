# Exercicio 10

numeros = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte',
           ]

while True:
    n = int(input('Digite um número entre 1 a 20: '))
    if 1 <= n <= 20:
        break

print(f'O número digitado foi {numeros[n]}')

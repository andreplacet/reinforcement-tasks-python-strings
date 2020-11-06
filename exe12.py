# Exercicio 12

print('Valida e corrige número de telefone')

numero = int(input('Telefone: '))
novoNumero = ''

if len(str(numero)) < 8:
    diferenca = 8 - len(str(numero))
    novoNumero = '3' * diferenca

numeroFormatado1 = novoNumero + str(numero)
numeroFormatado = numeroFormatado1[0:4] + '-' + numeroFormatado1[5:]


print(f'Telefone possui {len(str(numero))} dígitos. Vou acrescentar o digito três na frente.')
print(f'Telefone corrigido sem formatação: {numeroFormatado1}')
print(f'Telefone corrigido com formatação: {numeroFormatado}')

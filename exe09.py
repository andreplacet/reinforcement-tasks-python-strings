# Exercicio 09

cpf = str(input('Digite o CPF no formato xxx.xxx.xxx-xx: '))

if len(cpf) == 14:
    if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        print(f'O cpf digitado foi {cpf}')
    else:
        print('CPF INVALIDO!')
else:
    print('dados invalidos')
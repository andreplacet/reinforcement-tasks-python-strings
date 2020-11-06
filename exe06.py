# Exercicio 06

def data_extenso(dia, mes, ano):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
             'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    mes_resultado = meses[mes - 1]
    print(f'Dia {dia} de {mes_resultado} de {ano}')


dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

data_extenso(dia, mes, ano)

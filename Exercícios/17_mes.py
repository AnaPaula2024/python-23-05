'''
Autor: Julio Miranda
Data: 17/06/2024
Versão: 1.0
Descrição: Faça um programa que receba o número do mês e apresente ele por extenso:
            !Sem utilizar condicional!
            exemplo:
            if mes == 0
                print('Mes não existe')
            else if mes == 1
                print('Janeiro')

'''

meses_do_ano = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

while True:
    nr_mes = 0
    nr_mes = int(input('Digite o número do mês: '))
    print(meses_do_ano[nr_mes])

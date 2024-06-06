#================================================================
#Autor: Júlio Miranda
#Data: 24/05/2024
#Versão: 1.0
#Descrição: Faça um algoritmo que receba um valor na moeda real (R$),
#           a cotação da conversão REAL para DÓLAR, e apresente 
#           a quantidade desse valor em dolar ($)
#           ----------------------------------------------------
#           Exemplo de execução:
#           Insira o valor em real: 5000
#           Insira cotação do dia: 5
#           R$5000,00 equivalem $1000,00
#================================================================
#variaveis
real = 0 #recebe o valor em reais
cotacao = 0 #valor da cotação 1 dolar xreais
dolar = 0 #valor convertido real para dolar
#entrada
print('======================================')
#necessário fazer o casting(conversão de tipos de dados)
#float <= string
#5000,00 <= '5000'
real = float(input('Insira o valor em reais (R$): '))
cotacao = float(input('Insira o valor da cotação: '))
#processamento
dolar = real/cotacao
#saida
print('R$',real,'equivale','$', dolar)
print('======================================')
#================================================================

# real = float(input('insira o valor em real: '))
# conversaoRealParaDolar =  float(input('Insira cotação do dia: '))
# valorEmDolar = 1000

# valorEmDolar = real/conversaoRealParaDolar

# print('R$',real, 'equivalem', '$', valorEmDolar)


#================================================================
#Autor: Júlio Miranda
#Data: 24/05/2024
#Versão: 1.0
#Descrição: Faça um algoritmo que um valor na moeda real (R$),
#           a cotação da conversão REAL para DÓLAR, e apresente 
#           a quantidade desse valor em dolar ($)
#           ----------------------------------------------------
#           Exemplo de execução
#           Insira o valor em real: 5000
#           Insira cotação do dia: 5
#           R$5000,00 equivalem $1000,00
#================================================================


real = input('insira o valor em real: ')
conversaoRealParaDolar =  input('Insira cotaçãodo dia: ')
valorEmDolar = 1000

valorEmDolar = 5000 / 5

print('R$',real, 'equivalem', '$', valorEmDolar)


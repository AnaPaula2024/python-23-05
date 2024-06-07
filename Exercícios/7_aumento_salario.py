'''
Algoritmo "Aumento de salário"
Autor: Julio Miranda
Data: 04/06/2024
Descrição   : Faça um programa que receba o salário de um funcionário, calcule e mostre o
              novo salário, sabendo-se que:
                Salário < R$ 1000,00 aumento de 25%.
                Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
                Salário >= R$ 2000,00 aumento de 10%.

'''
#==================================================================================================
#variaveis
salario = 0
salario_aumento = 0
porcentagem = ''
#entrada
salario = float(input('Por favor, insira o seu salário:'))
#processamento
if(salario < 1000):
    porcentagem = '25%'
    salario_aumento = salario * 1.25
elif(salario >= 1000 and salario < 2000): #as duas condições tem que ser verdadeiras
    porcentagem = '15%'
    salario_aumento = salario * 1.15
elif(salario >=2000):
    porcentagem = '10%'
    salario_aumento = salario * 1.1
    salario_aumento = round(salario_aumento,2)#função nativa do python para arrendondar os valores o '2' seria duas casas decimais depois.
#saida
print ('O seu salario de', salario, 'sofreu um reajuste de', porcentagem, 'sendo agora no valor de',salario_aumento)
#==============================================================================================================================================
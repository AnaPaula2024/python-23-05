#================================================================
#Autor: Júlio Miranda
#Data: 28/05/2024
#Versão: 1.0
#Descrição: Faça um algoritmo que receba o raio em metros de um circulo
#           e apresente a sua área
#           ----------------------------------------------------
#           Exemplo de execução:
#           Insira o raio em metros: 5
#           Área do círculo: 78.5m^2
#           --------------------------------------------------

#           a = área
#           pi = 3.14
#           r = raio
#           a = pi*(r^2)
#         
#           --------------------------------------------------
#
#================================================================
#variaveis
a = 0 #área
pi = 3.14  #constante pi 
r = 0 #raio
#entrada
r = float(input('Insira o raio em metros: '))
#processamento
a = pi*(r**2) #os dois asteriscos seria o exponencial para o cálculo
#saida
print('A área do círculo é', a, 'm^2')
#================================================================
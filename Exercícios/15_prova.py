'''
Descrição: Faça um programa que receba dois valores, sendo que o 
            primeiro deve ser menor que o segundo.
            O programa deve apresentar todos os números impares
            contidos nesta sequência.
            (Modulo %. Exemplo: 7%2 = 1)
'''
#==========================================================================
num_A = 0
num_B = 0

num_A = int(input('Insira o valor inicial do seu range: ')) # 5
num_B = int(input('Insira o valor final do seu range: ')) # 10

# for alguma_coisa in range(5,10):
for nr_dentro_range in range(num_A,num_B): # 5 -> 6 -> 7 -> 8 -> 9
   resto = nr_dentro_range % 2 # 0(par) ou 1(impar)
#    print(f'{nr_dentro_range} % 2 = {resto}')
   if resto == 1:
      print(nr_dentro_range)
#===========================================================================


# Recebendo os valores do usuário
# primeiro_valor = int(input("Digite o primeiro valor: "))
# segundo_valor = int(input("Digite o segundo valor (maior que o primeiro): "))

# # Verificando se o primeiro valor é realmente menor que o segundo
# if primeiro_valor >= segundo_valor:
#     print("Erro: O primeiro valor deve ser menor que o segundo.")
# else:
#     print(f"Números ímpares entre {primeiro_valor} e {segundo_valor}:")
#     # Iterando sobre os números entre o primeiro e o segundo valor
#     for numero in range(primeiro_valor, segundo_valor + 1):
#         # Verificando se o número é ímpar usando o operador módulo (%)
#         if numero % 2 != 0:
#             print(numero)
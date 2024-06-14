'''
Descrição: Faça um programa que receba dois valores, sendo que o 
            primeiro deve ser menor que o segundo.
            O programa deve apresentar todos os números impares
            contidos nesta sequência.
            (Modulo %. Exemplo: 7%2 = 1)
'''

valor_um = 0
valor_dois = 0
impar = 0

valor_um = int(input('Insira o número menor: \n'))
valor_dois = int(input('Insira o número maior: \n'))

if(valor_um < valor_dois):
    ('Esses são os números impares entre {valor_um} e {valor_dois}')
else:
    print('Erro! Digite um valor menor que o segundo')
    

for i in range(valor_um):
    for j in range(valor_dois):
        if valor_um % valor_dois = 1:
            print(impar)
        

     









#     # Recebendo os valores do usuário
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
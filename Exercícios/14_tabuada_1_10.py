'''
Autor: Julio Miranda
Data: 13/06/2024
Algoritmo "Tabuada 1 ao 9"
Dscrição: Faça um programa que apresente a tabuada 1 ao 10;

'''
#==========================================================

# numero = 1
# resultado = 0

# print('Acione a tabuada do 1 ao 10: ')

# for numero in range(1,11):
#     for i in range(11):
#         resultado = numero * i
#         print(numero, "x", i, "=", resultado)
        
#==========================================================

# # Função para calcular e imprimir a tabuada de 1 a 9
# def tabuada():
#     print("Tabuada de 1 a 9:\n")
#     for i in range(1, 10):  # Loop de 1 a 9
#         print(f"Tabuada do {i}:\n")
#         for j in range(1, 11):  # Loop de 1 a 10
#             print(f"{i} x {j} = {i * j}")
#         print()  # Adiciona uma linha em branco entre as tabuadas

# # Chamando a função tabuada
# tabuada()
print('-------------------------------------------')
for l in range(11): #0-> 1 -> 2 ...
    for c in range(11): #0 -> 10
        print(f'{l} X {c} = {l * c}')
    print('--------------------------------')
#================================================
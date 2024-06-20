
'''
Algoritmo "Tabuada"
Descrição: Faça  um programa que calcule a tabuada de um número digitado
            pelo usuário;

'''
numero = 0
resultado = 0

numero = int(input('Digite um número: '))

for i in range(11): #i < 11 (0 até 10)
    # resultado = numero * 1
    print(f'{numero} x {i} = {numero * 1}') #interpolação f(format) ('f': Isso indica que a string é
    #uma f-string, permitindo a formatação de variáveis diretamente dentro da string.)
    # print(numero,'X', i, '=',resultado)


# Função para calcular e imprimir a tabuada de um número
# def tabuada(numero): # 'def' é uma palavra-chave usada para definir funções.
#     print("Tabuada de", numero, ":\n") #"\n" é um caractere de escape que representa uma quebra 
# de linha. Quando você vê "\n", isso indica que a próxima parte do texto será impressa
# em uma nova linha.
#     for i in range(1, 11): ':' indica o fim do cabeçalho da função e o início do bloco de código.
#         resultado = numero * i
#         print(numero, "x", i, "=", resultado)

# # Pedir ao usuário para inserir o número
# numero = int(input("Digite um número para ver a tabuada: "))

# # Chamar a função tabuada com o número inserido
# tabuada(numero)

#O laço for é usado quando você sabe previamente quantas vezes deseja executar um bloco de código. 
# Ele itera sobre uma sequência (como uma lista, tupla, string, etc.) ou outro objeto iterável.

#O laço while é usado quando você não sabe previamente quantas vezes deseja executar um bloco de código,
#  mas você sabe a condição que deve ser verdadeira para continuar a execução.
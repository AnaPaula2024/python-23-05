'''
Abertura comentário

Autor: Julio Miranda
Data: 28/05/2024
Versão: 1.0
Descrição: Estudos do condicional IF ... ELSE

Fechamento comentário
'''
#===============================================================
#variavel
nota = 0
#entrada
nota = int(input('Insira uma nota: '))
#processamento
if (nota >= 6):
    print('Aluno aprovado')
    #saida
    print(nota)
    # print('dentro do if')#Está identado
else:# if(nota < 6):
    print('Aluno reprovado')
# print('fora do if')#não está identado
#===============================================================
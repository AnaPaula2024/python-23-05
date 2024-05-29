'''
Abertura comentário

Autor: Julio Miranda
Data: 28/05/2024
Versão: 1.0
Descrição: Estudos do condicional IF ... ELiF

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
elif(nota < 4):# else if(nota < 4):
    print('Aluno reprovado')
else:
    print('Aluno recuperação')
#===============================================================
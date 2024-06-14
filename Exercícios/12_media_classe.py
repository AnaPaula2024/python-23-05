'''
Algoritmo "Média turma"
Descrição   : Faça um programa que receba duas notas de seis alunos. 
                Calcule e mostre:
            	A média aritmética das duas notas de cada aluno; e
            	A mensagem que está na tabela a seguir:
                    Média Aritmética	Mensagem
                    Até 3	            Reprovado 
                    Entre 4 e 7 	    Exame
                    De 8 para cima	    Aprovado

            	O total de alunos aprovados;
            	O total de alunos de exame;
            	O total de alunos reprovados;
            	A média da classe.
'''

aluno = 0 
qtAlunos = 6
alunosAprovado = 0
alunosReprovados = 0
alunosExame = 0
somaMedia = 0
mediaFinal = 0

while aluno < qtAlunos:
    aluno = aluno + 1 # aluno += 1
    # Aluno x
    nota_um = 0
    nota_dois = 0
    media = 0
    # nota_um = float(input('Insira a nota 1 do aluno', aluno, ':'))
    nota_um = float(input(f'Insira a nota 1 do aluno {aluno}: '))
    nota_dois = float(input(f'Insira a nota 2 do aluno {aluno}:'))

    media = (nota_um + nota_dois)/2 # 10 -> 8 -> 5 -> 10 -> 7 -> 8
    somaMedia = somaMedia + media # 10 -> 18 -> 23 -> 33 -> 40 -> 48

    if(media <= 3):
        print('Reprovado')
        alunosReprovados += 1  # alunosReprovados = alunos Reprovados + 1
    elif(media >= 4 and media <= 7):
        print('Exame')
        alunosExame += 1  # alunosExame = alunos Exame + 1
    else:
        print('Aprovado')
        alunosAprovado += 1  # alunosAprovados = alunos Aprovados + 1

mediaFinal = round((somaMedia / qtAlunos),2)
print(f'Quantidade de alunos aprovados: {mediaFinal}')
print(f'Quantidade de alunos aprovados: {alunosAprovado}')
print(f'Quantidade de alunos reprovados: {alunosReprovados}')
print(f'Quantidade de alunos exame: {alunosExame}')


# alunos_aprovados = 0
# alunos_exame = 0
# alunos_reprovados = 0

# while True:
#     nota1 = float(input('Digite sua nota1: '))
#     nota2 = float(input('Digite sua nota2: '))
    
#     media = (nota1 + nota2) / 2

#     if media >= 8:
#         print('Aprovado')
#         alunos_aprovados += 1
#     elif 4 < media < 7:
#         print('Exame')
#         alunos_exame += 1
#     else:
#         print('Reprovado')
#         alunos_reprovados += 1

#     print('Total de alunos aprovados:', alunos_aprovados)
#     print('Total de alunos de exame:', alunos_exame)
#     print('Total de alunos reprovados:', alunos_reprovados)
#     print('A média da classe é:', media)
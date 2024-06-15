'''
Autor: Julio Miranda
Data: 14/06/2024
Versão: 1.0
Descrição: Estudos do tipo de dado Array
'''

aluno_A = 'Karina'
aluno_B = 'André'
aluno_C = 'Ana Claudia'
aluno_D = 'Delfina'
aluno_E = 'Mauricio'
aluno_F = 'James'


#array
#                   0      1       2          3        4         5       
turma_python = [ 'Karina',200,'Ana Claudia',aluno_D,'Mauricio','James'] #array

print(turma_python)
turma_python[1] = 'Maria'
print(turma_python)
print(f'posição 0 do vetor turma_python é igual {turma_python[0]}')
print(f'posição 1 do vetor turma_python é igual {turma_python[1]}')
print(f'posição 2 do vetor turma_python é igual {turma_python[2]}')
print(f'posição 3 do vetor turma_python é igual {turma_python[3]}')
print(f'posição 4 do vetor turma_python é igual {turma_python[4]}')
print(f'posição 5 do vetor turma_python é igual {turma_python[5]}')

#============================================================================

alunos_python_noturno = [4, 5, 3, 2, 0, 1]
print(alunos_python_noturno)#array velho
alunos_python_noturno[0] = 'André'
alunos_python_noturno[1] = 'Karina'
alunos_python_noturno[2] = 'Mauricio'
alunos_python_noturno[3] = 'Delfina'
alunos_python_noturno[4] = 'Ana Claudia'
alunos_python_noturno[5] = 'James'
print(alunos_python_noturno[3]) # array novo

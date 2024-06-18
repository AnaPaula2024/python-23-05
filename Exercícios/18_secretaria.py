'''
Autor: Julio Miranda
Data: 17/06/2024
Versão: 1.0
Descrição   : Faça um programa que adicione alunos ao sistema da escola 
              (array) ou remova um aluno especifico.
              Nesse sistema deve estar previsito um menu com três opções:
              #===================================
              Sistema SENAI
              1 - Adicionar aluno:
              2 - Remover aluno:
              3 - Apresentar alunos
              4 - Sair
              Insira a opção desejada: 
              #===================================   
              Adicionar aluno
              Insira o nome do aluno:
              #===================================   
              Remover aluno
              Insira o nome do aluno para ser removido:
              #===================================   
              Alunos no sistema
              ['João', 'Pedro','Luana']
              #===================================   
'''

opcao = 0 #numero
sistema_alunos = [] #array não coloque essa dentro do while
novoAluno = '' #string

while True:

    print('=-'*30)
    print('Sistema SENAI')
    print('1 - Adicionar aluno:')
    print('2 - Remover aluno:')
    print('3 - Apresentar alunos')
    print('4 - Sair')
    opcao =  int(input('Insira a opção desejada:'))
    print('=-'*30)
    print()

    if(opcao == 1):
        print('=-'*30) 
        novoAluno = input('Adicione o aluno: ')
        sistema_alunos.append(novoAluno)
        print('Aluno(a)',sistema_alunos, 'inserido com sucesso!')
        print()
        
    elif (opcao == 2): 
        print('=-'*30)
        deletar_aluno = input('Remova o aluno: ')
        sistema_alunos.remove(deletar_aluno)
        # print(f'Aluno(a)',deletar_aluno, 'removido com sucesso!')
        # print('Aluno(a) informado não existe no sistema')
        print('=-'*30)
        print()
            
    elif (opcao == 3):
        print('=-'*30)
        print('Alunos no sistema: ')
        print(sistema_alunos)
        # print('Aluno(a) informado não consta no sistema' )
        # print('=-'*30)
        # print()
        
    else:
        print('=-'*30)
        print('Saindo do sistema...')
        break
            # print('Opção inválida. Tente novamente! \n')
           
            # print('=-'*30)
        





    


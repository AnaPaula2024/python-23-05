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

alunos = ['João', 'Pedro', 'Luana']

while True:
    print("#===================================")
    print("Sistema SENAI")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Apresentar alunos")
    print("4 - Sair")
    opcao = input("Insira a opção desejada: ")

    if opcao == '1':
        print("#===================================")
        nome = input("Insira o nome do aluno: ")
        alunos.append(nome)
        print(f"Aluno {nome} adicionado com sucesso!")

    elif opcao == '2':
        print("#===================================")
        nome = input("Insira o nome do aluno para ser removido: ")
        if nome in alunos:
            alunos.remove(nome)
            print(f"Aluno {nome} removido com sucesso!")
        else:
            print(f"Aluno {nome} não encontrado no sistema.")

    elif opcao == '3':
        print("#===================================")
        print("Alunos no sistema:")
        print(alunos)

    elif opcao == '4':
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1 a 4).")

print("Programa encerrado.")
        





    


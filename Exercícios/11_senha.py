'''
Autor: Julio Miranda
Data: 07/06/2024
Versão: 1.0
Algoritmo: Senha
Descrição:  Faça um programa que solicite para o usuário
             a senha de acesso ao sistema, ele terá no máximo três tentativas para inserir a correta
             cadastrada (senai115), caso passe desse limite uma mensagem de erro deve aparecer.
'''

# senhaCorreta = 'senac115'
# limiteDetentativas = 3
#     while limiteDetentativas > 0:
#         senha = input("Digite sua senha de acesso: ")
#         if senha == senhaCorreta:
#             print("Senha correta! Acesso permitido.")
#             break
#         else:
#             limiteDetentativas -= 1
#             if limiteDetentativas > 0:
#                 print("Senha incorreta! Você tem {limiteDetentativas} tentativas restantes.")
#             else:
#                 print("Limite de tentativas excedido. Acesso negado.")
#                 break
#=============================================================================
senha = '' #var para receber a senha do usuario
senhaPadrao = 'senai115' #senha padrão do sistema
tentativas = 3 #numero de tentativas de acesso ao sistema
while True:
        senha = input('Digite a sua senha: ') #senai115 => numeros com letras então sem casting
        if senha == senhaPadrao:
            print('Acesso liberado!')
            break #quebra o loop while, ou seja finaliza o programa
        else:
            tentativas = tentativas - 1 #tentativas -= 1(mesma coisa)
            print('Você só possui mais', tentativas,'tentativas')
        if(tentativas <= 0):
            print('Sistema Bloqueado')
            break   
#=============================================================================

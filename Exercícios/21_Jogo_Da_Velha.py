'''
Autor: Julio Miranda
Data: 25/06/2024
Versão: 1.0
Descrição   : Faça um jogo da velha

'''

matriz_jogo =  [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9']]
rodadas = 0
jogador = 'X'
while rodadas < 9:
    posicao = input (f'jogador {jogador} escolha uma posição: ') 
    posicao_encontrada = False
    for linha in range(3):
        linha_completa = ''
        for coluna in range(3):
            if posicao == matriz_jogo[linha][coluna]:
                matriz_jogo[linha][coluna] = jogador
                posicao_encontrada = True
            linha_completa += ' | ' + matriz_jogo[linha][coluna] + ' | '
        print(f' {linha_completa}')  
    if posicao_encontrada == True:
        rodadas = rodadas + 1
    if jogador == 'X':
        jogador  = 'O'
    else:
        jogador = 'X'
else:
    print("posição não econtrada")


# def print_tabuleiro(tabuleiro):
#     """ Função para imprimir o tabuleiro do jogo da velha """
#     for linha in tabuleiro:
#         print(" | ".join(linha))
#         print("-" * 9)

# def verifica_vitoria(tabuleiro, jogador):
#     """ Função para verificar se um jogador venceu """
#     # Verifica linhas e colunas
#     for i in range(3):
#         if all([tabuleiro[i][j] == jogador for j in range(3)]):
#             return True
#         if all([tabuleiro[j][i] == jogador for j in range(3)]):
#             return True

#     # Verifica diagonais
#     if all([tabuleiro[i][i] == jogador for i in range(3)]):
#         return True
#     if all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
#         return True

#     return False

# def jogo_da_velha():
#     """ Função principal para o jogo da velha """
#     tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
#     jogadores = ['X', 'O']
#     jogador_atual = 0
#     rodada = 0

#     print("Bem-vindo ao Jogo da Velha!")
#     print_tabuleiro(tabuleiro)

#     while True:
#         print(f"Jogador {jogadores[jogador_atual]}, é sua vez.")
#         linha = int(input("Escolha a linha (0, 1, 2): "))
#         coluna = int(input("Escolha a coluna (0, 1, 2): "))

#         if tabuleiro[linha][coluna] == " ":
#             tabuleiro[linha][coluna] = jogadores[jogador_atual]
#             rodada += 1
#             print_tabuleiro(tabuleiro)

#             # Verifica se houve um vencedor
#             if verifica_vitoria(tabuleiro, jogadores[jogador_atual]):
#                 print(f"Parabéns! Jogador {jogadores[jogador_atual]} venceu!")
#                 break

#             # Verifica se deu empate
#             if rodada == 9:
#                 print("Empate!")
#                 break

#             # Troca para o próximo jogador
#             jogador_atual = 1 - jogador_atual
#         else:
#             print("Posição ocupada. Escolha outra.")

# if __name__ == "__main__":
#     jogo_da_velha()

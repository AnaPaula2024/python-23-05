'''
Autor: Julio Miranda
Data: 25/06/2024
Versão: 1.0
Descrição   : Crie uma matriz e apresente ela no final da execução, 
            aonde existe duas colunas [tipo, Nome] e 4 linhas preenchidas com 
            o tipo do animal e seu respectivo nome
            
            #  Tipo Nome
            0  Gato Frajola
            1  Cão Coragem
            2  Passarinho Pica-pau
            3  Urso Ursinho Pooh
              
'''

# tipo = ['Gato', 'Cão','Passarinho','Urso']
# nome_de_Personagem = ['Frajola','Coragem','Pica-pau','Ursinho Pooh']


# tabela = [tipo, nome_de_Personagem]
# print()
# print("Tipo", tipo)
# print("Nome", nome_de_Personagem)

tabela_petshop = [
                    ['#', 'Tipo','Nome'],
                    ['1', 'Gato','Frajola'],
                    ['2', 'Cão','Coragem'],
                    ['3', 'Passarinho','Pica-pau'],
                    ['4', 'Urso','Ursinho Pooh']
                ]
for linha in range(5):
    linha_completa = ''
    for coluna in range(3):
     linha_completa += tabela_petshop[linha][coluna] + ' | '
     print(f'{linha_completa}')   

# print(f'{tabela_petshop[0][0]} {tabela_petshop[0][1]} {tabela_petshop[0][2]}')
# print(f'{tabela_petshop[1][0]} {tabela_petshop[1][1]} {tabela_petshop[1][2]}')
# print(f'{tabela_petshop[2][0]} {tabela_petshop[2][1]} {tabela_petshop[2][2]}')
# print(f'{tabela_petshop[3][0]} {tabela_petshop[3][1]} {tabela_petshop[3][2]}')
# print(f'{tabela_petshop[4][0]} {tabela_petshop[4][1]} {tabela_petshop[4][2]}')


# Criando a matriz de animais
# matriz_animais = [
#     ['Gato', 'Frajola'],
#     ['Cão', 'Coragem'],
#     ['Passarinho', 'Pica-pau'],
#     ['Urso', 'Ursinho Pooh']
# ]

# Apresentando a matriz formatada
# print("#  Tipo         Nome")
# for i, animal in enumerate(matriz_animais):
#     print(f"{i}  {animal[0]:<12} {animal[1]}")

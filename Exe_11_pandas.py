#pip install pandas
import pandas as pd #importar biblioteca pandas para a variavel pd

cabecalho_alunos = ["Nome","Turno", "matricula"]

dados_alunos = [["Oswaldo", "Noturno", "1010"],
                ['Rosa', 'noturno', '1011'],
                ['Francisco', 'noturno', '1012'],
                ['Julia', 'noturno','1013'],
                ['Jenifer', 'matutino','1014']
                ]
#DataFrame
df = pd.DataFrame(dados_alunos, columns=cabecalho_alunos)
print(df.head(2))#apresentar as duas primeiras linhas do meu dataframe(tabela)

df.to_csv('Alunos_senai.csv')#exportando o meu dataframe para um arquivo.csv
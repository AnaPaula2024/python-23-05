#pip install selenium


#importar a biblioteca
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

#
chrome = webdriver.Chrome()
chrome.implicitly_wait(2)
chrome.get('https://webscraper.io/test-sites/tables')
titulo_pagina = chrome.title

#encontra elementos pela nome da tag td
tabela_dados = chrome.find_elements(By.TAG_NAME, 'td')#td = tabledata

linhas = []
celulas = []
nr_colunas = 4
contador_coluna = 0
for dados in tabela_dados:
    contador_coluna = contador_coluna + 1
    celulas.append(dados.text)
    if contador_coluna == nr_colunas:
        linhas.append(celulas)
        celulas = []
        contador_coluna = 0


df = pd.DataFrame(linhas, columns=['#', 'First Name', 'Last Name', 'User name'])
print(df)
df.to_csv('web.csv')
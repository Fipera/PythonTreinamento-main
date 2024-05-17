from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausa
import pyautogui as teclasAtalho
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import os

arquivo_tabela = "C:\\Users\\Win7\\Desktop\\Documents\\RPA\\tabelaWEB\\Dados_Tabela.xlsx"
planilhaDadosTabela = load_workbook(arquivo_tabela)

sheet_selecionada = planilhaDadosTabela['Dados']

browser = webdriver.Firefox()

browser.get('https://rpachallengeocr.azurewebsites.net/')

elementoTabela = browser.find_element(By.CSS_SELECTOR, '#tableSandbox')


linha = 1

i = 1
while i < 4:

    sheet_dados = planilhaDadosTabela['Dados']

    tempoPausa.sleep(2)
    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    tempoPausa.sleep(1)
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

    for linhaAtual in linhas:

        print(linhaAtual.text)
        linha += 1
        linha = len(sheet_dados['A']) + 1

        colunaA = "A" + str(linha)
        colunaB = "B" + str(linha)
        colunaC = "C" + str(linha)

        texto = linhaAtual.text
        texto2 = texto.split(" ")

        sheet_dados[colunaA] = texto2[0]
        sheet_dados[colunaB] = texto2[1]
        sheet_dados[colunaC] = texto2[2]

    i += 1
    tempoPausa.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '#tableSandbox_next').click()
    tempoPausa.sleep(2)
    
else:
    print("Pronto")

planilhaDadosTabela.save(filename=arquivo_tabela)

os.startfile(arquivo_tabela)
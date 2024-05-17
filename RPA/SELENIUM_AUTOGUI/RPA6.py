from openpyxl import load_workbook
import os

nome_arquivo_cep = 'C:\\Users\\Win7\\Desktop\\Documents\\RPA\\extrair endereço CEP\\PesquisaEndereco_1.xlsx'
planilhaDados = load_workbook(nome_arquivo_cep)

planilha_Cep_imprimir = planilhaDados["CEP"]


#------------------------------------


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausa
import pyautogui as teclasAtalho
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php')


for linha in range(2, len(planilha_Cep_imprimir['A']) + 1):

    cepPesquisa = planilha_Cep_imprimir['A%s' % linha].value
    tempoPausa.sleep(3)
    browser.find_element(By.ID, "endereco").send_keys(cepPesquisa)
    tempoPausa.sleep(3)
    browser.find_element(By.ID, "btn_pesquisar").click()
    tempoPausa.sleep(3)

    rua = browser.find_element(By.CSS_SELECTOR, '#resultado-DNEC > tbody > tr > td:nth-child(1)').text
    bairro = browser.find_element(By.CSS_SELECTOR, '#resultado-DNEC > tbody > tr > td:nth-child(2)').text
    cidade = browser.find_element(By.CSS_SELECTOR, '#resultado-DNEC > tbody > tr > td:nth-child(3)').text
    cep = browser.find_element(By.CSS_SELECTOR, '#resultado-DNEC > tbody > tr > td:nth-child(4)').text

    print(rua, bairro, cidade, cep)
    print("\n")

    planilha_Dados_imprimir = planilhaDados["Dados"]
    linhaCorrente = len(planilha_Dados_imprimir['A']) + 1
    colunaA = "A" + str(linhaCorrente)
    colunaB = "B" + str(linhaCorrente)
    colunaC = "C" + str(linhaCorrente)
    colunaD = "D" + str(linhaCorrente)

    planilha_Dados_imprimir[colunaA] = rua
    planilha_Dados_imprimir[colunaB] = bairro
    planilha_Dados_imprimir[colunaC] = cidade
    planilha_Dados_imprimir[colunaD] = cep
    
    tempoPausa.sleep(3)
    browser.find_element(By.ID, "btn_nbusca").click()
    tempoPausa.sleep(3)


browser.quit()

planilhaDados.save(filename=nome_arquivo_cep)

os.startfile(nome_arquivo_cep)
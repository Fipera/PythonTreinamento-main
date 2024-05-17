from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import os

browser = webdriver.Firefox()
browser.get('https://www.mercadolivre.com.br/')

elementoTabela = browser.find_element(By.CSS_SELECTOR, '#cb1-edit').send_keys("carteira")

import time
time.sleep(2)

browser.find_element(By.CSS_SELECTOR, 'body > header > div > div.nav-area.nav-top-area.nav-center-area > form > button').click()

time.sleep(6)

dadosProduto = browser.find_elements(By.CLASS_NAME, "ui-search-layout__item")

wb = Workbook()
ws = wb.active
ws.append(["Nome do Produto", "Preço", "Centavos", "URL"])

for informacoes in dadosProduto:
    nomeProduto = informacoes.find_element(By.CLASS_NAME, "ui-search-item__title").text
    precoProduto = informacoes.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
    
    try:
        centavosProduto = informacoes.find_element(By.CLASS_NAME, "andes-money-amount__cents andes-money-amount__cents--superscript-24").text
    except:
        centavosProduto = "0"

    urlProduto = informacoes.find_element(By.TAG_NAME, "a").get_attribute("href")

    ws.append([nomeProduto, precoProduto, centavosProduto, urlProduto])

file_path = "C:\\Users\\Win7\\Desktop\\Documents\\RPA\\tabelaWEB\\Dados_Tabela.xlsx"
wb.save(file_path)

browser.quit()

os.startfile(file_path)

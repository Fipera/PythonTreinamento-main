from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausa
import pyautogui as teclasAtalho
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CaminhoArquivo = "c:\\Users\\Win7\\Desktop\\Documents\\RPA\\PrenchendoFormularioWEB\\DadosFormulario.xlsx"

planilha_aberta = load_workbook(CaminhoArquivo)

sheet_selecionada = planilha_aberta["Dados"]

for linha in range(2, len(sheet_selecionada['A']) + 1):

    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'B{linha}'].value
    telefone = sheet_selecionada[f'C{linha}'].value
    sexo = sheet_selecionada[f'D{linha}'].value
    sobre = sheet_selecionada[f'E{linha}'].value

    browser = webdriver.Firefox()

    browser.get('https://pt.surveymonkey.com/r/WLXYDX2')

    espera = WebDriverWait(browser, 10)

    tempoPausa.sleep(5)

    
    campo_nome = espera.until(EC.presence_of_element_located((By.ID, "166517069")))
    campo_nome.send_keys(nome)

    campo_email = espera.until(EC.presence_of_element_located((By.ID, "166517072")))
    campo_email.send_keys(email)

    campo_telefone = espera.until(EC.presence_of_element_located((By.ID, "166517070")))
    campo_telefone.send_keys(telefone)

    campo_sobre = espera.until(EC.presence_of_element_located((By.ID, "166517073")))
    campo_sobre.send_keys(sobre)

    if (sexo == "Masculino"):
        botao_sexo = espera.until(EC.element_to_be_clickable((By.ID, "166517071_1215509812_label")))
    elif (sexo == "Feminino"):
        botao_sexo = espera.until(EC.element_to_be_clickable((By.ID, "166517071_1215509813_label")))


    botao_sexo.click()


    tempoPausa.sleep(3)

    botao_enviar = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#patas > main > article > section > form > div.survey-submit-actions.center-text.clearfix > button')))
    botao_enviar.click()   


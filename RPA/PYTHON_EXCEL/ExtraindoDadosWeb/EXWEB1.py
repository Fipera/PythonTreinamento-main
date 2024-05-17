from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausa
import pyautogui as teclasAtalho
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://rpachallengeocr.azurewebsites.net/')

elementoTabela = browser.find_element(By.CSS_SELECTOR, '#tableSandbox')


linha = 1

i = 1
while i < 4:

    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')

    for linhaAtual in linhas:

        print(linhaAtual.text)
        linha += 1

    i += 1
    tempoPausa.sleep(2)
    browser.find_element(By.CSS_SELECTOR, '#tableSandbox_next').click()
    tempoPausa.sleep(2)
    
else:
    print("Pronto")
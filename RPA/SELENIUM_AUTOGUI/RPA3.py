from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausa
import pyautogui as teclasAtalho
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://google.com')

tempoPausa.sleep(4)
browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys("Dólar hoje")
tempoPausa.sleep(4)
browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys(Keys.RETURN)
tempoPausa.sleep(4)

Dolar = browser.find_elements(By.XPATH, '/html/body/div[4]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]')[0].text
print(Dolar)


#EURO -------------------------------

tempoPausa.sleep(2)
browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys("")
tempoPausa.sleep(4)

teclasAtalho.press('tab')
teclasAtalho.press('enter')

browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys("Euro hoje")
tempoPausa.sleep(4)
browser.find_element(By.CSS_SELECTOR, '#APjFqb').send_keys(Keys.RETURN)
tempoPausa.sleep(4)

Euro = browser.find_elements(By.XPATH, '/html/body/div[4]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]')[0].text
print(Euro)



#browser.quit()
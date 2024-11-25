import pandas as pd
import time
from selenium import webdriver # navegador
from selenium.webdriver.common.by import By # elementos
from selenium.webdriver.common.keys import Keys # teclado web

nome_arquivo = "Contatos.xlsx"
url_forms = "https://docs.google.com/forms/d/1Y4BBAFGL9c-LNGkPaeYgIlbA_dj5KyX26mU4zuNfm0g/edit"
df = pd.read_excel(nome_arquivo)

for index, row in df.iterrows():
    print("Index: "+ str(index) + " Nome: " + row["NOME"])
    chrome = webdriver.Chrome()
    chrome.get(url_forms)

    time.sleep(3)

    elemento_nome = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    elemento_telefone = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    elemento_nota = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[' + str(row["NOTA"]) + ']/div[2]')

    elemento_nome.send_keys(row["NOME"])
    elemento_telefone.send_keys(row["TELEFONE"])
    elemento_nota.click()

    elemento_enviar = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    
    chrome.quit

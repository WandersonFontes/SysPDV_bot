import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_cm = (input(str('Por gentileza insira o para realizar o acesso:\n')))
senha_cm = (input(str('Digite sua senha:\n')))
cnpj_cm = (input(str('Agora informe o CNPJ:\n')))
serie_cm = (input(str('Qual número de serie?\n')))

def login():
    driver = webdriver.Chrome()
    driver.get("http://sistemas.casamagalhaes.com.br/home.cm")
    time.sleep(3)
    user = driver.find_element_by_id('usuario')
    user.send_keys(user_cm)
    time.sleep(3)
    senha = driver.find_element_by_id('senha')
    senha.send_keys(senha_cm)
    time.sleep(3)
    entrar = driver.find_element_by_id('enviar').click()
    time.sleep(3)

    #Inserção de dados para geração da chave de acesso
    
    suporte = driver.find_element_by_link_text('Suporte').click()
    time.sleep(2)
    chave  = driver.find_element_by_link_text('Chave').click()
    time.sleep(2)
    renovaChave  = driver.find_element_by_link_text('Renovação de Chave').click()
    time.sleep(2)
    cnpj = driver.find_element_by_id('chaveForm:cpfCnpj')
    cnpj.send_keys(cnpj_cm)
    time.sleep(2)
    confirmar = driver.find_element_by_id('chaveForm:j_id321').click()
    time.sleep(2)
    serie  = driver.find_element_by_id('chaveForm:j_id360')
    serie.send_keys()






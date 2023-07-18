from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import time
def restartModem():
    driver = webdriver.Chrome()

    # Abra a página web
    driver.get('http://192.168.18.1/')

    # Localize os elementos dos campos de texto
    campo1 = driver.find_element(By.ID,'txt_Username')
    campo2 = driver.find_element(By.ID, 'txt_Password')

    # Preencha os campos de texto
    campo1.send_keys('Epadmin')
    campo2.send_keys('Admin123')

    botao_entrar = driver.find_element(By.ID, 'loginbutton')

    botao_entrar.click()

    espera = WebDriverWait(driver, 10)
    iframe = espera.until(EC.presence_of_element_located((By.ID, 'menuIframe')))
    driver.switch_to.frame(iframe)


    botao_reiniciar = driver.find_element(By.ID, 'RestartIcon')
    botao_reiniciar.click()
    time.sleep(3)


    iframe2 = espera.until(EC.presence_of_element_located((By.ID, 'routermngtpageSrc')))
    driver.switch_to.frame(iframe2)

    botao_reiniciar2 = driver.find_element(By.ID, 'btnReboot')
    botao_reiniciar2.click()
    time.sleep(3)

    alerta = Alert(driver)
    alerta.accept()
    time.sleep(3)

    # Encerre o driver do Selenium
    driver.quit()

    # Inicialize o driver do Selenium (você precisará ter o driver correspondente ao seu navegador instalado)

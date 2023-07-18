from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

def adblock(driver):
        # Abra a página web
    driver.get('https://chrome.google.com/webstore/detail/adblock-%E2%80%94-best-ad-blocker/gighmmpiobklfepjocnamgkkbiglidom?hl=pt-BR')
    time.sleep(10)
    campo1 = driver.find_element("css selector", ".webstore-test-button-label")
    campo1.click()
    time.sleep(10)
    alert = Alert(driver)

# Verifique o texto do alerta
    if alert.text == "Add extension":
        # Aceite o alerta (pressione o botão "OK")
        alert.accept()
    time.sleep(20)

adblock(driver)

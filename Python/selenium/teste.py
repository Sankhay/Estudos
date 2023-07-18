from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
from restartModem import restartModem
from getCarInfo import getCarInfo


def reiniciar_pagina(driver):
    try:
        driver.refresh()
        print("REINICIOU COM SUCESSO")
    except:
        pass
driver = webdriver.Chrome()
link = 'fichadetalhe.asp?codigo=17966'
carrosNaWeb = 'https://www.carrosnaweb.com.br/'
try:
    driver.get(carrosNaWeb + link)
    time.sleep(5)
    url_atual = driver.current_url
    if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
        restartModem()
        time.sleep(120)
        driver.get(carrosNaWeb + link)
        time.sleep(5)
    else:
        print('não detecto')
    html = driver.page_source
    getCarInfo(html)
except TimeoutException:
    print('reiniciando pagina')
    reiniciar_pagina(driver)

    html = driver.page_source
    print(link)
    getCarInfo(html)

print("ELE FUNCIONOU CARALHO HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

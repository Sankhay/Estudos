from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from restartModem import restartModem
from bs4 import BeautifulSoup
from getCarInfo import getCarInfo

driver = webdriver.Chrome()
linksCarros = []

carrosNaWeb = "https://www.carrosnaweb.com.br/"

def reiniciar_pagina(driver):
    try:
        driver.refresh()
        print("REINICIOU COM SUCESSO")
    except:
        pass

links_completos = []
links_completos.append('catalogo.asp?fabricante=BMW&varnome=')
links_completos.append('catalogo.asp?fabricante=Chevrolet&varnome=')

for link2 in links_completos:
    try:
        while True:
            driver.get(carrosNaWeb + link2)
            time.sleep(5)
            url_atual = driver.current_url
            if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                restartModem()
                driver.quit()
                time.sleep(120)
                driver = webdriver.Chrome()
            else:
                break
    except TimeoutException:
        print("reiniciando pagina")
        reiniciar_pagina(driver)
    while True:
        html12 = driver.page_source
        doc = BeautifulSoup(html12, "html.parser")
        links = doc.find_all(["td"], bgcolor="#ffffff", align="left")
        for link in links:
            a_tags = link.find_all('a')
            for a_tag in a_tags:
                linksCarros.append(a_tag.get('href'))

        element = doc.find("b", string="Próxima")
        if element is not None:
            parent_element = element.parent
            link_real = parent_element.get('href')
            link_completo = carrosNaWeb + link_real
            try:
                driver.get(carrosNaWeb + link_real)
                time.sleep(1)
                url_atual = driver.current_url
                if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                    restartModem()
                    time.sleep(120)
                    driver.get(carrosNaWeb + link_real)
                    time.sleep(5)
            except TimeoutException:
                print("reiniciando pagina")
                reiniciar_pagina(driver)
        else:
            print('Não tem mais')
            break


for link in linksCarros:
    try:
        while True:
            driver.get(carrosNaWeb + link)
            time.sleep(5)
            url_atual = driver.current_url
            if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                restartModem()
                driver.quit()
                time.sleep(120)
                driver = webdriver.Chrome()
            else:
                break
    except TimeoutException:
        print('reiniciando pagina')
        reiniciar_pagina(driver)

    html = driver.page_source
    print(link)
    getCarInfo(html)


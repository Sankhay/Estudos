import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from restartModem import restartModem
from selenium.webdriver.chrome.options import Options
from getCarInfo import getCarInfo
from getLinks import getLinksYears
from getFabri import getFabri
from bs4 import BeautifulSoup

def reiniciar_pagina(driver):
    try:
        driver.refresh()
        print("REINICIOU COM SUCESSO")
    except:
        pass
# Configure ChromeOptions to set user agent
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

#linksFabricantes = []
linksCatalogo = []
linksYearsCar = []
linksCarros = []

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(10)
carrosNaWeb = "https://www.carrosnaweb.com.br/"

driver.get(carrosNaWeb + 'avancada.asp')
html = driver.page_source
linksFabricantes = getFabri(html)
for link in linksFabricantes:
    try:
        driver.get(carrosNaWeb + link)
        time.sleep(1)
        html = driver.page_source
        allModelLinks = getFabri(html)
        linksCatalogo.append(allModelLinks)
    except TimeoutException:
        print("reiniciando pagina")
        reiniciar_pagina(driver)
        time.sleep(1)
        html = driver.page_source
        allModelLinks = getFabri(html)
        linksCatalogo.append(allModelLinks)
        

for link1 in linksCatalogo:
    for link2 in link1:
        try:
            driver.get(carrosNaWeb + link2)
            time.sleep(1)
            html = driver.page_source
            allYearsLinks = getLinksYears(html)
            linksYearsCar.append(allYearsLinks)
        except TimeoutException:
            print("reiniciando pagina")
            reiniciar_pagina(driver)
            time.sleep(1)
            html = driver.page_source
            allYearsLinks = getLinksYears(html)
            if allYearsLinks != []:
                linksYearsCar.append(allYearsLinks)
                
for link1 in linksYearsCar:
    for link2 in link1:
        try:
            driver.get(carrosNaWeb + link2)
            time.sleep(1)
            url_atual = driver.current_url
            if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                restartModem()
                time.sleep(120)
                driver.get(carrosNaWeb + link2)
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
                except TimeoutException:
                    print("reiniciando pagina")
                    reiniciar_pagina(driver)
            else:
                print('Não tem mais')
                break
            

for link in linksCarros:
    try:
        driver.get(carrosNaWeb + link)
        time.sleep(1)
        url_atual = driver.current_url
        if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
            restartModem()
            time.sleep(120)
            driver.get(carrosNaWeb + link)
    except TimeoutException:
        print('reiniciando pagina')
        reiniciar_pagina(driver)

    html = driver.page_source
    print(link)
    getCarInfo(html)

print("ELE FUNCIONOU CARALHO HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")


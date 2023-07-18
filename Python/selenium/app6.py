import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from restartModem import restartModem
from selenium.webdriver.chrome.options import Options
from getCarInfo import getCarInfo
from getLinks import getLinksYears
from getFabri import getFabri
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--incognito")  # Adiciona a opção --incognito para abrir em modo anônimo

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(10)

def reiniciar_pagina(driver):
    try:
        driver.refresh()
        print("REINICIOU COM SUCESSO")
    except:
        pass

linksCarros = ['fichadetalhe.asp?codigo=6003', 'fichadetalhe.asp?codigo=9765', 'fichadetalhe.asp?codigo=5691', 'fichadetalhe.asp?codigo=5210', 'fichadetalhe.asp?codigo=1731', 'fichadetalhe.asp?codigo=23669', 'fichadetalhe.asp?codigo=23668', 'fichadetalhe.asp?codigo=1134', 'fichadetalhe.asp?codigo=21321', 'fichadetalhe.asp?codigo=23670', 'fichadetalhe.asp?codigo=17922', 'fichadetalhe.asp?codigo=5211', 'fichadetalhe.asp?codigo=1732', 'fichadetalhe.asp?codigo=5209', 'fichadetalhe.asp?codigo=10606', 'fichadetalhe.asp?codigo=21701', 'fichadetalhe.asp?codigo=22186', 'fichadetalhe.asp?codigo=24615', 'fichadetalhe.asp?codigo=21700', 'fichadetalhe.asp?codigo=22185', 'fichadetalhe.asp?codigo=5212', 'fichadetalhe.asp?codigo=5213', 'fichadetalhe.asp?codigo=10605', 'fichadetalhe.asp?codigo=10607', 'fichadetalhe.asp?codigo=1742', 'fichadetalhe.asp?codigo=1733', 'fichadetalhe.asp?codigo=1741', 'fichadetalhe.asp?codigo=8548', 'fichadetalhe.asp?codigo=8012', 'fichadetalhe.asp?codigo=8547', 'fichadetalhe.asp?codigo=7222', 'fichadetalhe.asp?codigo=7223', 'fichadetalhe.asp?codigo=5184', 'fichadetalhe.asp?codigo=5183', 'fichadetalhe.asp?codigo=6486', 'fichadetalhe.asp?codigo=3337', 'fichadetalhe.asp?codigo=3336', 'fichadetalhe.asp?codigo=5226', 'fichadetalhe.asp?codigo=5227', 'fichadetalhe.asp?codigo=5225', 'fichadetalhe.asp?codigo=5228', 'fichadetalhe.asp?codigo=1504', 'fichadetalhe.asp?codigo=1508', 'fichadetalhe.asp?codigo=5206', 'fichadetalhe.asp?codigo=1509', 'fichadetalhe.asp?codigo=17528', 'fichadetalhe.asp?codigo=5224', 'fichadetalhe.asp?codigo=1138', 'fichadetalhe.asp?codigo=22765', 'fichadetalhe.asp?codigo=22766', 'fichadetalhe.asp?codigo=19403', 'fichadetalhe.asp?codigo=19813', 'fichadetalhe.asp?codigo=19814', 'fichadetalhe.asp?codigo=18255', 'fichadetalhe.asp?codigo=18518', 'fichadetalhe.asp?codigo=13049', 'fichadetalhe.asp?codigo=10127', 'fichadetalhe.asp?codigo=8356', 'fichadetalhe.asp?codigo=7221', 'fichadetalhe.asp?codigo=4442', 'fichadetalhe.asp?codigo=4441', 'fichadetalhe.asp?codigo=3330', 'fichadetalhe.asp?codigo=3329', 'fichadetalhe.asp?codigo=3328', 'fichadetalhe.asp?codigo=3327', 'fichadetalhe.asp?codigo=1671', 'fichadetalhe.asp?codigo=1681', 'fichadetalhe.asp?codigo=1680', 'fichadetalhe.asp?codigo=5260', 'fichadetalhe.asp?codigo=5240', 'fichadetalhe.asp?codigo=5241']
carrosNaWeb = "https://carrosnaweb.com.br/"

for link in linksCarros:
    try:
        while True:
            print(carrosNaWeb + link)
            driver.get(carrosNaWeb + link)
            time.sleep(5)
            url_atual = driver.current_url
            if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                driver.quit()
                restartModem()
                time.sleep(120)
                driver = webdriver.Chrome(options=chrome_options)
                time.sleep(5)
            else:
                break
    except TimeoutException:
        print('reiniciando pagina')
        reiniciar_pagina(driver)

    html = driver.page_source
    print(link)
    getCarInfo(html)

print("ELE FUNCIONOU CARALHO HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
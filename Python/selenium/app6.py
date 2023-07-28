import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from restartModem import restartModem
from selenium.webdriver.chrome.options import Options
from getCarInfo import getCarInfo
from selenium.webdriver.common.proxy import Proxy, ProxyType

from getLinks import getLinksYears
from getFabri import getFabri
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--incognito")  # Adiciona a opção --incognito para abrir em modo anônimo

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f'43.130.35.101:11572'
options.add_argument("--proxy-server=http://{}".format(proxy.http_proxy))
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(60)

def reiniciar_pagina(driver):
    try:
        driver.refresh()
        print("REINICIOU COM SUCESSO")
    except:
        pass

linksCarros = ['fichadetalhe.asp?codigo=22552']
carrosNaWeb = "https://carrosnaweb.com.br/"

for link in linksCarros:
    driver.get(carrosNaWeb + link)
    url_atual = driver.current_url
    time.sleep(20)

    html = driver.page_source
    print(link)
    getCarInfo(html)

print("ELE FUNCIONOU CARALHO HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from restartModem import restartModem
from selenium.webdriver.chrome.options import Options
from getCarInfo import getCarInfo
from bs4 import BeautifulSoup
import random



completo = []




with open('linkYearsCar.txt', 'r') as file:
    for linha in file:
        separado = linha.split(" c")
        for linha2 in separado:
            completo.append(linha2)

for i in range(len(completo)):
    if "atalogo" in completo[i]:
        completo[i] = completo[i].replace("atalogo", "catalogo")

for i in range(len(completo)):
    if "ccatalogo" in completo[i]:
        completo[i] = completo[i].replace("ccatalogo", "catalogo")




def user_agent():
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/93.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/93.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/91.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/93.0"
    # Adicione mais User Agents aqui, se desejar
    ]


    return random.choice(user_agents)

options = Options()
options.add_argument("--disable-javascript")

# Desativar o uso de cookies
options.add_argument("--disable-cookies")

# Desativar plugins
options.add_argument("--disable-plugins")


def reiniciar_pagina(driver):
    try:
        driver.refresh()
        print("REINICIOU COM SUCESSO")
    except:
        pass
carrosNaWeb = "https://carrosnaweb.com.br/"

linksCarros = []
c = 0


for index, link2 in enumerate(completo[49:], start=49):
        options.add_argument(user_agent())
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(10)
        try:
            try:
                while True:
                    driver.get(carrosNaWeb + link2)
                    if c == 7:
                        restartModem()
                        time.sleep(60)
                        c = 0
                    else:
                        c = c+1
                    time.sleep(10)
                    url_atual = driver.current_url
                    if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                        print("Reinicia ai caralho")
                        restartModem()
                        time.sleep(60)
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
                        a_tag = a_tag.get('href')
                        try:
                            try:
                                while True:
                                    driver.get(carrosNaWeb + a_tag)
                                    if c == 10:
                                        restartModem()
                                        time.sleep(60)
                                        c = 0
                                    else:
                                        c = c+1
                                    url_atual = driver.current_url
                                    if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                                        print("Reinicia ai caralho")
                                        restartModem()
                                        time.sleep(60)
                                    else:
                                        break
                            except TimeoutException:
                                print('reiniciando pagina')
                                reiniciar_pagina(driver)

                            html = driver.page_source
                            getCarInfo(html)
                        except:
                            pass

                element = doc.find("b", string="Próxima")
                if element is not None:
                    parent_element = element.parent
                    link_real = parent_element.get('href')
                    link_completo = carrosNaWeb + link_real
                    try:
                        driver.get(driver, link_completo)
                        if c == 10:
                            restartModem()
                            time.sleep(60)
                            c = 0
                        else:
                            c = c+1
                        time.sleep(10)
                        url_atual = driver.current_url
                        if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                            print("REINICIA AI CARALHO")
                            restartModem()
                            time.sleep(60)
                    except TimeoutException:
                        print("reiniciando pagina")
                        reiniciar_pagina(driver)
                else:
                    print('Não tem mais')
                    driver.quit()
                    break
        except:
            pass

print("ELE FUNCIONOU CARALHO HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
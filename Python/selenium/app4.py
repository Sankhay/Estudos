import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from undetected_chromedriver import Chrome, ChromeOptions
from getCarInfo import getCarInfo
from bs4 import BeautifulSoup
from pegaproxy import pegar_proxy



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


def get_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f'170.106.117.131:11513'

options = Options()

def generate_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random

extension_path = '/home/davi/Downloads/adblock.crx'
options.add_argument("--window-size=800,600")
options.add_extension(extension_path)
options.add_argument("--disable-images")

options.add_argument("--no-first-run")
# Desativar o uso de cookies
options.add_argument("--proxy-server=http://{}".format(proxy.http_proxy))
prefs = {"profile.managed_default_content_settings.images": 2}  # 2 significa não carregar imagens
options.add_experimental_option("prefs", prefs)

# Desativar plugins
def reiniciar_proxy():
    global driver
    driver.quit()
    options = Options()
    print('reiniciando proxy')
    extension_path = '/home/davi/Downloads/adblock.crx'
    prefs = {"profile.managed_default_content_settings.images": 2}  # 2 significa não carregar imagens
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-first-run")
    ip, port = pegar_proxy()
    proxy.http_proxy = f'{ip}:{port}'
    options.add_argument("--proxy-server=http://{}".format(proxy.http_proxy))
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)


driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(60)


def reiniciar_pagina(driver):
    reiniciar_proxy()
    time.sleep(10)

carrosNaWeb = "https://carrosnaweb.com.br/"

linksCarros = []
c = 0
#1363
for index, link2 in enumerate(completo[3987:], start=3987):
        filename = "esta agora.txt"
        with open(filename, "a") as f:
                f.write(f'index: {index}' + "\n")
        print(link2)
        print(index)
        try:
            z = 0
            while z < 1:
                try:
                    while True:
                        if c == 10:
                            reiniciar_proxy()
                            c = 0
                        else:
                            c = c+1
                        driver.get(carrosNaWeb + link2)
                        time.sleep(3)
                        url_atual = driver.current_url
                        z = 10
                        if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                            reiniciar_proxy()
                            time.sleep(24)
                        else:
                            break
                except TimeoutException:
                    print("reiniciando pagina")
                    reiniciar_pagina(driver)
                    z = 0
            while True:
                html12 = driver.page_source
                doc = BeautifulSoup(html12, "html.parser")
                links = doc.find_all(["td"], bgcolor="#ffffff", align="left")
                for link in links:
                    a_tags = link.find_all('a')
                    for a_tag in a_tags:
                        a_tag = a_tag.get('href')
                        try:
                            x = 0
                            while x < 1:
                                try:
                                    while True:
                                        print('chegou aqui')
                                        driver.get(carrosNaWeb + a_tag)
                                        time.sleep(7)
                                        url_atual = driver.current_url
                                        x = 10
                                        if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                                            reiniciar_proxy()
                                            time.sleep(10)
                                        else:
                                            break
                                except TimeoutException:
                                    print('reiniciando pagina')
                                    x = 0
                                    reiniciar_pagina(driver)
                                    time.sleep(10)
                            html = driver.page_source
                            pegou = getCarInfo(html)
                            filename = "esta agora.txt"
                            with open(filename, "a") as f:
                                f.write(f'Esse carro deu certo' + "\n")
                            if pegou == 'error':
                                filename = "erro de carros.txt"
                                with open(filename, "a") as f:
                                        f.write(f'{carrosNaWeb + a_tag}' + "\n")
                        except:
                            filename = "esta agora.txt"
                            with open(filename, "a") as f:
                                    f.write(f'erro no link do carro que esta agora link {carrosNaWeb + a_tag}' + "\n")
                            pass

                element = doc.find("b", string="Próxima")
                if element is not None:
                    print('tem mais que 10')
                    parent_element = element.parent
                    link_real = parent_element.get('href')
                    link_completo = carrosNaWeb + link_real
                    try:
                        while True:
                            driver.get(link_completo)
                            time.sleep(10)
                            url_atual = driver.current_url
                            if url_atual == 'https://www.carrosnaweb.com.br/erro.asp':
                                reiniciar_proxy()
                                time.sleep(20)
                            else:
                                break
                    except TimeoutException:
                        print("reiniciando pagina")
                        reiniciar_pagina(driver)
                        time.sleep(20)
                else:
                    print('Não tem mais')
                    break
        except:
            filename = "esta agora.txt"
            with open(filename, "a") as f:
                f.write(f'Erro' + "\n")
            pass

print("ELE FUNCIONOU CARALHO HUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
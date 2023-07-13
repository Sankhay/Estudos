import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from restartModem import restartModem

All_Links = [
"catalogo.asp?fabricante=Adamo&",
"catalogo.asp?fabricante=Agrale&",
"catalogo.asp?fabricante=Alfa Romeo&",
"catalogo.asp?fabricante=Ariel&",
"catalogo.asp?fabricante=Asia&",
"catalogo.asp?fabricante=Aston Martin&",
"catalogo.asp?fabricante=Audi&",
"catalogo.asp?fabricante=Avallone&",
"catalogo.asp?fabricante=Bentley&",
"catalogo.asp?fabricante=Bianco&",
"catalogo.asp?fabricante=BMW&",
"catalogo.asp?fabricante=BRM&",
"catalogo.asp?fabricante=Bugatti&",
"catalogo.asp?fabricante=BYD&",
"catalogo.asp?fabricante=Cadillac&",
"catalogo.asp?fabricante=Caterham&",
"catalogo.asp?fabricante=CBT&",
"catalogo.asp?fabricante=Chamonix&",
"catalogo.asp?fabricante=Chana&",
"catalogo.asp?fabricante=Changan&",
"catalogo.asp?fabricante=Chery&",
"catalogo.asp?fabricante=Chevrolet&",
"catalogo.asp?fabricante=Chrysler&",
"catalogo.asp?fabricante=Citroen&",
"catalogo.asp?fabricante=Cross Lander&",
"catalogo.asp?fabricante=Daewoo&",
"catalogo.asp?fabricante=Daihatsu&",
"catalogo.asp?fabricante=DeLorean&",
"catalogo.asp?fabricante=Dodge&",
"catalogo.asp?fabricante=Effa&",
"catalogo.asp?fabricante=Engesa&",
"catalogo.asp?fabricante=Enseada&",
"catalogo.asp?fabricante=Envemo&",
"catalogo.asp?fabricante=Farus&",
"catalogo.asp?fabricante=Ferrari&",
"catalogo.asp?fabricante=Fiat&",
"catalogo.asp?fabricante=Ford&",
"catalogo.asp?fabricante=Geely&",
"catalogo.asp?fabricante=GMC&",
"catalogo.asp?fabricante=Gurgel&",
"catalogo.asp?fabricante=GWM&",
"catalogo.asp?fabricante=Hafei&",
"catalogo.asp?fabricante=Hennessey&",
"catalogo.asp?fabricante=Hofstetter&",
"catalogo.asp?fabricante=Honda&",
"catalogo.asp?fabricante=Hummer&",
"catalogo.asp?fabricante=Hyundai&",
"catalogo.asp?fabricante=Infiniti&",
"catalogo.asp?fabricante=Iveco&=",
"catalogo.asp?fabricante=JAC&=",
"catalogo.asp?fabricante=Jaguar&=",
"catalogo.asp?fabricante=Jeep&=",
"catalogo.asp?fabricante=Jinbei&=",
"catalogo.asp?fabricante=JPX&=",
"catalogo.asp?fabricante=Kia&=",
"catalogo.asp?fabricante=Koenigsegg&=",
"catalogo.asp?fabricante=KTM&=",
"catalogo.asp?fabricante=Lada&=",
"catalogo.asp?fabricante=Lafer&=",
"catalogo.asp?fabricante=Lamborghini&=",
"catalogo.asp?fabricante=Land Rover&=",
"catalogo.asp?fabricante=Lexus&=",
"catalogo.asp?fabricante=Lifan&=",
"catalogo.asp?fabricante=Lincoln&=",
"catalogo.asp?fabricante=Lobini&=",
"catalogo.asp?fabricante=Lotus&=",
"catalogo.asp?fabricante=Mahindra&=",
"catalogo.asp?fabricante=Maserati&=",
"catalogo.asp?fabricante=Mazda&=",
"catalogo.asp?fabricante=McLaren&=",
"catalogo.asp?fabricante=Mercedes-Benz&=",
"catalogo.asp?fabricante=Mercury&=",
"catalogo.asp?fabricante=MG&=",
"catalogo.asp?fabricante=Mini&=",
"catalogo.asp?fabricante=Mitsubishi&=",
"catalogo.asp?fabricante=Miura&=",
"catalogo.asp?fabricante=Nissan&=",
"catalogo.asp?fabricante=Pagani&=",
"catalogo.asp?fabricante=Peugeot&=",
"catalogo.asp?fabricante=Plymouth&",
"catalogo.asp?fabricante=Pontiac&",
"catalogo.asp?fabricante=Porsche&",
"catalogo.asp?fabricante=Puma&",
"catalogo.asp?fabricante=Ragge&",
"catalogo.asp?fabricante=Ram&",
"catalogo.asp?fabricante=Rely&",
"catalogo.asp?fabricante=Renault&",
"catalogo.asp?fabricante=Rolls-Royce&",
"catalogo.asp?fabricante=Saab&",
"catalogo.asp?fabricante=Saleen&",
"catalogo.asp?fabricante=Santa Matilde&",
"catalogo.asp?fabricante=Saturn&",
"catalogo.asp?fabricante=Seat&",
"catalogo.asp?fabricante=Shineray&",
"catalogo.asp?fabricante=Smart&",
"catalogo.asp?fabricante=Ssangyong&",
"catalogo.asp?fabricante=SSC&",
"catalogo.asp?fabricante=Subaru&",
"catalogo.asp?fabricante=Suzuki&",
"catalogo.asp?fabricante=TAC&",
"catalogo.asp?fabricante=Tesla&",
"catalogo.asp?fabricante=Toyota&",
"catalogo.asp?fabricante=Troller&",
"catalogo.asp?fabricante=Volkswagen&",
"catalogo.asp?fabricante=Volvo&",
"catalogo.asp?fabricante=W Motors&"
]
# Configure ChromeOptions to set user agent
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

for index, link in enumerate(All_Links):
    links_carros = []

    # Configure webdriver with ChromeOptions
    driver = webdriver.Chrome(options=options)

    carrosNaWeb = 'https://www.carrosnaweb.com.br/'
    link_completo = carrosNaWeb + link
    driver.get(carrosNaWeb + link)

    while True:
        html_content = driver.page_source
        doc = BeautifulSoup(html_content, "html.parser")

        while True:
            links = doc.find_all(["td"], bgcolor="#ffffff", align="left")
            if links:
                break
            else:
                restartModem()
                time.sleep(120)
                driver.get(link_completo)
                html_content = driver.page_source
                doc = BeautifulSoup(html_content, "html.parser")
                print("não tem")
        for link in links:
            a_tags = link.find_all('a')
            for a_tag in a_tags:
                links_carros.append(a_tag.get('href'))

        element = doc.find("b", string="Próxima")
        # Check if the element exists
        if element is not None:
            parent_element = element.parent
            link_real = parent_element.get('href')

            # Emulate human-like behavior
            sleep_interval = random.uniform(1.5, 3.5)
            time.sleep(sleep_interval)

            # Perform mouse movement relative to element
            actions = ActionChains(driver)
            actions.perform()

            # Press Page Down key to scroll
            actions = ActionChains(driver)
            actions.send_keys(Keys.PAGE_DOWN)
            actions.perform()

            link_completo = carrosNaWeb + link_real
            driver.get(carrosNaWeb + link_real)
        else:
            print('Não tem mais')
            break
    
    filename = "LinksCarros.txt"

    with open(filename, "a") as f:
        for car in links_carros:
            f.write(car + "\n")

    # Close the current tab instead of quitting the entire browser
    driver.close()

print("oi terminou não sei como funcionou mas foi")

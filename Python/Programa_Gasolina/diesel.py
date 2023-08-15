from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import pandas as pd


def extrair_numeros(texto):
    number = ""
    for char in texto:
        if char.isdigit():
            number += char
        elif char == ",":
            number += "."
    return float(number)


def abrev_to_nome_estado(abreviacao):
    estados = {
        'AC': 'ACRE',
        'AL': 'ALAGOAS',
        'AM': 'AMAZONAS',
        'AP': 'AMAPÁ',
        'BA': 'BAHIA',
        'CE': 'CEARÁ',
        'DF': 'DISTRITO FEDERAL',
        'ES': 'ESPÍRITO SANTO',
        'GO': 'GOIÁS',
        'MA': 'MARANHÃO',
        'MG': 'MINAS GERAIS',
        'MS': 'MATO GROSSO DO SUL',
        'MT': 'MATO GROSSO',
        'PA': 'PARÁ',
        'PB': 'PARAÍBA',
        'PE': 'PERNAMBUCO',
        'PI': 'PIAUÍ',
        'PR': 'PARANÁ',
        'RJ': 'RIO DE JANEIRO',
        'RN': 'RIO GRANDE DO NORTE',
        'RO': 'RONDÔNIA',
        'RR': 'RORAIMA',
        'RS': 'RIO GRANDE DO SUL',
        'SC': 'SANTA CATARINA',
        'SE': 'SERGIPE',
        'SP': 'SÃO PAULO',
        'TO': 'TOCANTINS'
    }

    nome_estado = estados.get(abreviacao.upper())
    if nome_estado:
        return nome_estado
    else:
        return "Abreviação de estado não reconhecida."

def getDiesel(Estado):
    estado = abrev_to_nome_estado(Estado)

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://frotas.localiza.com/blog/preco-do-diesel-no-brasil")

    doc = BeautifulSoup(driver.page_source, "html.parser")

    valor_diesel = doc.find(["td"], string=estado)

    valor_diesel = valor_diesel.find_next("td")

    valor_diesel = extrair_numeros(valor_diesel.get_text())

    return valor_diesel



def getEnergia(linha, roda):
    dados = pd.read_excel("dados_carros.xlsx")

    autonomiaDoCarro = dados.at[linha, "Autonomia Urbana"]

    tanque = dados.at[linha, "Tanque"]

    valorDaEnergia = 0.6988

    quantosKWHCarroGasta = extrair_numeros(tanque) / extrair_numeros(autonomiaDoCarro)

    total = quantosKWHCarroGasta * roda * valorDaEnergia


    texto = f"""Considerando que você percorre por mês ({roda} km), a autonomia do carro ({autonomiaDoCarro}) por carga completa, com a bateria do carro ({tanque}), valor médio de energia no Brasil (R$ {valorDaEnergia}), você terá aproximadamente um gasto médio de R$ {int(total)}."""

    return texto



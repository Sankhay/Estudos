from selenium import webdriver
from bs4 import BeautifulSoup
import customtkinter
from selenium.webdriver.chrome.options import Options
from diesel import getDiesel, getEnergia
import pandas as pd

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("APP")
root.geometry("500x350")

def abrev_to_nome_estado(abreviacao):

    estados = {
        'AC': 'Acre: ',
        'AL': 'Alagoas: ',
        'AM': 'Amazonas:',
        'AP': 'Amapá:',
        'BA': 'Bahia: ',
        'CE': 'Ceará: ',
        'DF': 'Distrito Federal:',
        'ES': 'Espírito Santo: ',
        'GO': 'Goiás: ',
        'MA': 'Maranhão:',
        'MG': 'Minas Gerais: ',
        'MS': 'Mato Grosso do Sul: ',
        'MT': 'Mato Grosso: ',
        'PA': 'Pará: ',
        'PB': 'Paraíba: ',
        'PE': 'Pernambuco: ',
        'PI': 'Piauí:',
        'PR': 'Paraná: ',
        'RJ': 'Rio de Janeiro: ',
        'RN': 'Rio Grande do Norte:',
        'RO': 'Rondônia: ',
        'RR': 'Roraima: ',
        'RS': 'Rio Grande do Sul: ',
        'SC': 'Santa Catarina: ',
        'SE': 'Sergipe: ',
        'SP': 'São Paulo:',
        'TO': 'Tocantins:'
    }

    nome_estado = estados.get(abreviacao.upper())
    if nome_estado:
        return nome_estado
    else:
        return "Abreviação de estado não reconhecida."
    
def extrair_numeros(texto):
    number = ""
    for char in texto:
        if char.isdigit():
            number += char
        elif char == ",":
            number += "."
    return float(number)

def trocarFloatBr(numero):
    numeroCerto = ""
    numero = str(numero)
    for char in numero:
        if char == ".":
            numeroCerto += ","
        else:
            numeroCerto += char
    
    return numeroCerto
            

def getGasosa(Estado):
    estado = abrev_to_nome_estado(Estado)

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://frotas.localiza.com/blog/preco-da-gasolina-no-brasil")

    doc = BeautifulSoup(driver.page_source, "html.parser")

    valor_gasosa = doc.find(["strong"], string=estado)

    valor_gasosa = valor_gasosa.find_parent("li").get_text()

    valor_gasosa = extrair_numeros(valor_gasosa)

    return valor_gasosa

def gasolina():
    linha = entry1.get()
    estado = entry2.get()
    kmPorMes = int(entry3.get())

    linha = int(linha)

    linha = linha - 2

    nome_arquivo = 'dados_carros.xlsx'

    df = pd.read_excel(nome_arquivo)

    combustivel = df.at[linha, "Propulsão"]

    if combustivel == "Diesel":
        valorDoCombustivel = getDiesel(estado)
        litrosPorKm = extrair_numeros(df.at[linha, "Consumo cidade (Km/L)"])
        km = (kmPorMes / litrosPorKm)
        total = valorDoCombustivel * km
        texto = f"""Considerando que você percorre por mês ({kmPorMes} km), o valor médio atual da gasolina (R$ {trocarFloatBr(valorDoCombustivel)}) e o consumo do veículo na cidade ({trocarFloatBr(litrosPorKm)} Km/l) seu custo mensal será de aproximadamente R$ {int(total)},00."""

    elif combustivel == "Eletricidade":
        texto = getEnergia(linha, kmPorMes)
    else:
        valorDoCombustivel = getGasosa(estado)
        litrosPorKm = extrair_numeros(df.at[linha, "Consumo cidade (Km/L)"])
        km = (kmPorMes / litrosPorKm)
        total = valorDoCombustivel * km
        texto = f"""Considerando que você percorre por mês ({kmPorMes} km), o valor médio atual da gasolina (R$ {trocarFloatBr(valorDoCombustivel)}) e o consumo do veículo na cidade ({trocarFloatBr(litrosPorKm)} Km/l) seu custo mensal será de aproximadamente R$ {int(total)},00."""
    
    app = customtkinter.CTk()
    # Adicione um texto à janela
    textbox = customtkinter.CTkTextbox(master=app, width=300)
    textbox.pack(pady=100, padx=100)

    app.title("Texto Completo")

    textbox.insert("0.0", texto)

    # Mostre a janela
    app.mainloop()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx= 60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pegar dados")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Linha do carro")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Abreviação do Estado")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Quanto a pessoa Roda ao Mes")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Pegar", command=gasolina)

button.pack(pady=12, padx=10)


root.mainloop()

    


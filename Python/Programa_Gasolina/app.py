from selenium import webdriver
from bs4 import BeautifulSoup
import customtkinter
from itens import checkarValores, string_to_list_without_spaces
from selenium.webdriver.chrome.options import Options
from diesel import getDiesel, getEnergia
import pandas as pd
import re

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("APP")
root.geometry("700x550")

def extract_kgfm(text):
    # Use regex to find the kgfm value
    pattern = r'([\d,.]+)\s*kgfm'
    match = re.search(pattern, text)
    
    if match:
        kgfm_value = match.group(1)
        return kgfm_value
    else:
        return None
    
def extract_text_between_A_and_G(input_text):
    start_marker = "(A)"
    end_marker = "(G)"
    
    start_index = input_text.index(start_marker) + len(start_marker)
    end_index = input_text.index(end_marker)
    
    extracted_text = input_text[start_index:end_index].strip()
    return extracted_text

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
    
def abrevParaPranilha(abrev):
    estados = {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AM': 'Amazonas',
        'AP': 'Amapá',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MG': 'Minas Gerais',
        'MS': 'Mato Grosso do Sul',
        'MT': 'Mato Grosso',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'PR': 'Paraná',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'RS': 'Rio Grande do Sul',
        'SC': 'Santa Catarina',
        'SE': 'Sergipe',
        'SP': 'São Paulo',
        'TO': 'Tocantins'
    }

    nome_estado = estados.get(abrev.upper())

    if nome_estado:
        return nome_estado
    else:
        return "Abreviação de estado não reconhecida"

    
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
    infotenimento = str(entry5.get())
    seguranca = str(entry6.get())
    conforto = str(entry7.get())

    linha = int(linha)

    linha = linha - 2

    nome_arquivo = 'dados_carros.xlsx'

    df = pd.read_excel(nome_arquivo)

    combustivel = df.at[linha, "Propulsão"]

    potencia = "X"
    motor = "Motor: X"
    autUrbana = df.at[linha, "Autonomia Urbana"]

    if combustivel == "Diesel":
        valorDoCombustivel = getDiesel(estado)
        litrosPorKm = extrair_numeros(df.at[linha, "Consumo cidade (Km/L)"])
        km = (kmPorMes / litrosPorKm)
        total = valorDoCombustivel * km
        texto = f"""Considerando que você percorre por mês ({kmPorMes} km), o valor médio atual do diesel é (R$ {trocarFloatBr(valorDoCombustivel)}) e o consumo do veículo na cidade ({trocarFloatBr(litrosPorKm)} Km/l) seu custo mensal será de aproximadamente R$ {int(total)},00."""
        consNaCidade = df.at[linha, "Consumo cidade (Km/L)"]
        consNaEstrada = df.at[linha, "Consumo Estrada (Km/L)"]
        autEstrada = df.at[linha, "Autonomia Estrada"]    
        texto3 = f"\n\n Consumo na cidade de {consNaCidade} \n Autonomia urbana de {autUrbana} \n\n Consumo na estrada de {consNaEstrada} \n Autonomia na estrada de {autEstrada}"

    elif combustivel == "Eletricidade":
        texto = getEnergia(linha, kmPorMes)
        bateria = df.at[linha, "Tanque"]
        motor = f"capacidade da beteria de {bateria}"
        potencia = df.at[linha, "Potência"]
        potencia = extrair_numeros(potencia)
        potencia = str(int(potencia)) + "cv"
        texto3 = f"\n\n Autonomia \n {autUrbana}"

    else:
        valorDoCombustivel = getGasosa(estado)
        litrosPorKm = extrair_numeros(df.at[linha, "Consumo cidade (Km/L)"])
        km = (kmPorMes / litrosPorKm)
        total = valorDoCombustivel * km
        texto = f"""Considerando que você percorre por mês ({kmPorMes} km), o valor médio atual da gasolina (R$ {trocarFloatBr(valorDoCombustivel)}) e o consumo do veículo na cidade ({trocarFloatBr(litrosPorKm)} Km/l) seu custo mensal será de aproximadamente R$ {int(total)},00."""
        consNaCidade = df.at[linha, "Consumo cidade (Km/L)"]
        consNaEstrada = df.at[linha, "Consumo Estrada (Km/L)"]
        autEstrada = df.at[linha, "Autonomia Estrada"]    
        texto3 = f"\n\n Consumo na cidade de {consNaCidade} \n Autonomia urbana de {autUrbana} \n\n Consumo na estrada de {consNaEstrada} \n Autonomia na estrada de {autEstrada}"
        if combustivel == "Flex (álcool/gasolina)":
            potencia = df.at[linha, "Potência"]
            potencia = extract_text_between_A_and_G(potencia)
    velocidade_maxima = df.at[linha, "Velocidade Máxima"]
    torque = df.at[linha, "Torque"]
    torque = extract_kgfm(torque)
    zeroAoCem = df.at[linha, "0-100"]

    texto2 = f"\n \n {motor}  \n Potência: {potencia} \n Velocidade máxima de {velocidade_maxima} \n Torque de {torque} kgfm \n 0 a 100 em {zeroAoCem} segundos"

    texto = texto + texto2
    texto = texto + texto3

    tamanhoDoPortaMalas = df.at[linha, "Litragem real do porta malas"]
    altura = df.at[linha, "Altura"]
    largura = df.at[linha, "Largura"]
    peso = ""
    entre_eixos = df.at[linha, "Entre Eixos"]
    pneus_dianteiros = df.at[linha, "Pneus Dianteiros"]
    comprimento = ""

    texto4 = f"\n\n Porta Malas: {tamanhoDoPortaMalas} \n Altura: {altura} \n Largura: {largura} \n Comprimento: {comprimento} \n Peso: {peso} \n Entre-eixos: {entre_eixos} \n Pneus Dianteiros: {pneus_dianteiros}"

    texto = texto + texto4

    #Quando for somente a gasolina não pegar torque
    #Quando for flex pegar Oque esta na frente de (G)

    
    df_metricas = pd.read_excel(nome_arquivo, sheet_name="Métricas", usecols=[12, 13])
    
    estado = df_metricas[df_metricas.iloc[:, 0] == abrevParaPranilha(estado)].iloc[0]

    valorDoCarro = float(entry4.get())

    texto = texto + "\n\n\n" + f"O valor do IPVA do carro sera de R${float(estado.iloc[1]) * valorDoCarro}"

    listaInfotenimento, listaSeguranca, listaConforto, listaInfotenimentoErrado, listaSegurancaErrado, listaConfortoErrado = checkarValores(linha, string_to_list_without_spaces(infotenimento), string_to_list_without_spaces(seguranca), string_to_list_without_spaces(conforto))
    # listaInfotenimentoErrado, listaSegurancaErrado, listaConfortoErrado
    listaInfotenimento = " , ".join(listaInfotenimento)

    listaSeguranca = " , ".join(listaSeguranca)

    listaConforto = " , ".join(listaConforto)

    listaInfotenimentoErrado = " , ".join(listaInfotenimentoErrado)

    listaSegurancaErrado = " , ".join(listaSegurancaErrado)

    listaConfortoErrado = " , ".join(listaConfortoErrado)

    texto5 = f"\n\n\n Infotenimento: {listaInfotenimento} \n\n Segurança: {listaSeguranca} \n\n Conforto: {listaConforto} \n\n Não tem Infotenimento: {listaInfotenimentoErrado} \n\n Não tem Segurança: {listaSegurancaErrado} \n\n Não tem Conforto: {listaConfortoErrado}"

    texto = texto + texto5

    app = customtkinter.CTk()
    # Adicione um texto à janela
    textbox = customtkinter.CTkTextbox(master=app, width=600)
    textbox.pack(pady=300, padx=200, fill="both", expand=True)

    app.title("Texto Completo")

    textbox.insert("0.0", texto)

    # Mostre a janela
    app.mainloop()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx= 10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pegar dados")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Linha do carro")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Abreviação do Estado")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Quanto a pessoa Roda ao Mes")
entry3.pack(pady=12, padx=10)

entry4 = customtkinter.CTkEntry(master=frame, placeholder_text="Qual o valor do carro?")
entry4.pack(pady=12, padx=10)

entry5 = customtkinter.CTkEntry(master=frame, placeholder_text="Itens de infotenimento")
entry5.pack(pady=12, padx=12)

entry6 = customtkinter.CTkEntry(master=frame, placeholder_text="Itens de segurança")
entry6.pack(pady=12, padx=10)

entry7 = customtkinter.CTkEntry(master=frame, placeholder_text="Itens de conforto")
entry7.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Pegar", command=gasolina)

button.pack(pady=12, padx=10)

root.mainloop()

    


import pandas as pd

def remove_non_digits(input_string):
    result = ''.join(filter(str.isdigit, input_string))
    return result

nome_arquivo = 'dados_carros.xlsx'

lista = []

df = pd.read_excel(nome_arquivo)


def getLista(linha):

    lista = []

    lista.append("Motorização ")

    combustivel = df.at[linha, "Propulsão"]
    combustivel = f"Combustível - {combustivel}"
    lista.append(combustivel)


    potencia = df.at[linha, "Potência"]
    potencia = f"Potência (CV) - {potencia}"
    lista.append(potencia)

    torque = df.at[linha, "Torque"]
    torque = f"Torque (kgf.m) - {torque}"
    lista.append(torque)

    velocidadeMax = df.at[linha, "Velocidade Máxima"]
    velocidadeMax = f"Velocidade Máxima (Km/h) - {velocidadeMax}"
    lista.append(velocidadeMax)

    zero_cem = df.at[linha, "0-100"]
    zero_cem = f"Aceleração de 0-100 (s) - {zero_cem}"
    lista.append(zero_cem)

    consCidAl = "Consumo cidade Álcool (km/l) - "
    lista.append(consCidAl)

    consCid = df.at[linha, "Consumo cidade (Km/L)"]
    consCid = f"Consumo cidade Gasolina (km/l) - {consCid}"
    lista.append(consCid)

    consEstAl = "Consumo estrada Álcool (km/l) - "
    lista.append(consEstAl)

    consEst = df.at[linha, "Consumo Estrada (Km/L)"]
    consEst = f"Consumo estrada Gasolina (km/l) - {consEst}"
    lista.append(consEst)

    autoUrbAlc = "Autonomia urbana Álcool - "
    lista.append(autoUrbAlc)

    autoUrbGas = df.at[linha, "Autonomia Urbana"]
    autoUrbGas = f"Autonomia urbana Gasolina - {autoUrbGas}"
    lista.append(autoUrbGas)

    autoEstAlc = "Autonomia estrada Álcool - "
    lista.append(autoEstAlc)

    autoEstGas = df.at[linha, "Autonomia Estrada"]
    autoEstGas = f"Autonomia estrada Gasolina - {autoEstGas}"
    lista.append(autoEstGas)

    tanque = df.at[linha, "Tanque"]
    tanque = f"Tanque de combustível - {tanque}"
    lista.append(tanque)

    cambio = df.at[linha, "Câmbio"]
    cambio = f"Câmbio - {cambio}"
    lista.append(cambio)

    tracao = df.at[linha, "Tração"]
    tracao = f"Tração - {tracao}"
    lista.append(tracao)

    direcao = df.at[linha, "Direção"]
    direcao = f"Direção - {direcao}"
    lista.append(direcao)

    susDia = df.at[linha, "Suspensão dianteira"]
    susDia = f"Suspensão dianteira - {susDia}"
    lista.append(susDia)

    susTra = df.at[linha, "Suspensão Traseira"]
    susTra = f"Suspensão traseira - {susTra}"
    lista.append(susTra)

    freDia = df.at[linha, "Freios Dianteiros"]
    freDia = f"Freios dianteiros - {freDia}"
    lista.append(freDia)

    freTra = df.at[linha, "Freios Traseiros"]
    freTra = f"Freios traseiros - {freTra}"
    lista.append(freTra)

    return lista

def getDimensoes(linha):

    lista_dimensoes = []

    altura = df.at[linha, "Altura"]
    altura = f"Altura (mm) - {altura}"
    lista_dimensoes.append(altura)

    largura = df.at[linha, "Largura"]
    largura = f"Largura (mm) - {largura}"
    lista_dimensoes.append(largura)

    comprimento = "Comprimento (mm) - "
    lista_dimensoes.append(comprimento)

    peso = "Peso (Kg) - "
    lista_dimensoes.append(peso)

    tanque2 = df.at[linha, "Tanque"]
    tanque2 = remove_non_digits(tanque2)
    tanque2 = f"{tanque2}L"
    tanque2 = f"Tanque (L) - {tanque2}"
    lista_dimensoes.append(tanque2)

    entEix = df.at[linha, "Entre Eixos"]
    entEix = f"Entre-eixos (mm) - {entEix}"
    lista_dimensoes.append(entEix)

    porMal = df.at[linha, "Litragem real do porta malas"]
    porMal = f"Porta-Malas (L) - {porMal}"
    lista_dimensoes.append(porMal)

    ocupantes = df.at[linha, "Lugares"]
    ocupantes = f"Ocupantes - {ocupantes} lugares"
    lista_dimensoes.append(ocupantes)

    return lista_dimensoes

def getPneus(linha):
    lista_pneus = []

    dianteiros = df.at[linha, "Pneus Dianteiros"]
    dianteiros = f"Dianteiros - {dianteiros}"
    lista_pneus.append(dianteiros)

    traseiros = df.at[linha, "Pneus Traseiros"]
    traseiros = f"Traseiros - {traseiros}"
    lista_pneus.append(traseiros)

    estepe = df.at[linha, "Estepe"]
    if estepe != "Não informado":
        estepe = f"Estepe - {estepe}"
        lista_pneus.append(estepe)

    return lista_pneus



import pandas as pd

def substituir_valor(lista, valor_antigo, valor_novo):
    for i in range(len(lista)):
        if lista[i] == valor_antigo:
            lista[i] = valor_novo
    return lista

def substituir_ar(lista, valor_antigo):
    for i in range(len(lista)):
        if lista[i] == valor_antigo:
            for c in range(5):
                lista.append(f"Zonas de ar-condicionado: {c+2}")
    return lista

def checkarValores(linha, infotenimento, seguranca, conforto):

    seguranca = substituir_valor(seguranca, "Camerá de ré", "Câmera traseira para manobras")

    conforto = substituir_ar(conforto, "Ar condicionado de mais de uma zona")

    df = pd.read_excel("dados_carros.xlsx")

    carroConforto = df.at[linha, "Direção"]

    carroConforto = f"Direção {carroConforto}"

    

    infotenimentoTotal = df.at[linha, "Itens de Infotenimento"]

    segurancaTotal = df.at[linha, "Itens de segurança"]

    confortoTotal = df.at[linha, "Itens de Conforto"]
    
    #infotenimentoTotal = ["Carregador de celular por indução", "Comandos ao veículo via aplicativo" ,"Espelhamento da tela do celular", "Head-up display", "Informações do veículo via aplicativo", "Navegador GPS" ,"Roteador Wi-Fi", "Volante multifuncional"]

    #segurancaTotal = ["Alerta de colisão frontal", "Alerta de mudança de faixa", "Alerta de ponto cego", "Alerta de tráfego cruzado traseiro", "Assistente de partida em rampa", "Assistente de permanência em faixa", "Câmera 360°", "Câmera de ré", "Controle de estabilidade", "Controle de tração", "Faróis de LED", "Frenagem automática de emergência", "ISOFIX para fixação de cadeira infantil", "Sensores de estacionamento dianteiro", "Sensores de estacionamento traseiro", "Tração integral"]

    #confortoTotal = ["Acionamento remoto do motor", "Ajuste elétrico dos retrovisores", "Apoio de braço para o motorista", "Ar condicionado automático", "Ar condicionado de mais de uma zona", "Auto Hold", "Bancos de couro", "Banco do motorista com memória de ajuste", "Chave presencial", "Direção elétrica", "Freio de estacionamento elétrico", "Limitador de Velocidade", "Retrovisores rebatíveis eletricamente", "Rodas de liga leve", "Sistema start stop", "Teto panorâmico", "Teto solar elétrico", "Troca de marcha no volante"]

    listaInfotenimentoCerto = []
    listaSegurancaCerto = []
    listaConfortoCerto = []

    listaInfotenimentoErrado = []
    listaSegurancaErrado = []
    listaConfortoErrado = []

    for info in infotenimento:
        if info in infotenimentoTotal:
            listaInfotenimentoCerto.append(info)
        else:
            listaInfotenimentoErrado.append(info)
    
    for segu in seguranca:
        if segu in segurancaTotal:
            listaSegurancaCerto.append(segu)
        else:
            listaSegurancaErrado.append(segu)

    if "Direção elétrica" in conforto:
        if carroConforto == "Direção Elétrica":
            listaConfortoCerto.append(carroConforto)
        else:
            listaConfortoErrado.append("Direção Elétrica")
        

    for conf in conforto:
        if conf in confortoTotal:
            listaConfortoCerto.append(conf)
        else:
            listaConfortoErrado.append(conf)

    listaConfortoErrado = [item for item in listaConfortoErrado if 'Zonas de ar-condicionado' not in item]

    contains_ar_condicionado = any(item.startswith('Zonas de ar-condicionado') for item in listaConfortoCerto)

    if not contains_ar_condicionado:
        listaConfortoErrado.append("Ar Condicionado com mais de uma zona")
    

    return listaInfotenimentoCerto, listaSegurancaCerto, listaConfortoCerto, listaInfotenimentoErrado, listaSegurancaErrado, listaConfortoErrado

def string_to_list_without_spaces(input_string):
    word_list = input_string.split(',')
    cleaned_list = [word.strip() for word in word_list]
    return cleaned_list

print(checkarValores(0, 
                     string_to_list_without_spaces("Carregador de celular por indução,Comandos ao veículo via aplicativo,Espelhamento da tela do celular,Head-up display,Informações do veículo via aplicativo,Navegador GPS,Roteador Wi-Fi,Volante multifuncional") ,
                     string_to_list_without_spaces("Alerta de Colisão Frontal,Alerta de mudança de faixa,Alerta de ponto cego,Alerta de tráfego cruzado traseiro,Assistente de partida em rampa,Assistente de permanência em faixa,Câmera 360°,Camerá de ré,Controle de estabilidade,Controle de tração,Faróis de LED,Frenagem automática de emergência,ISOFIX para fixação de cadeira infantil,Sensores de estacionamento dianteiro,Sensores de estacionamento traseiro,Tração Integral"), 
                     string_to_list_without_spaces("Acionamento remoto do motor,Ajuste elétricos dos retrovisores,Apoio de braço para o motorista,Ar condicionado automático,Ar condicionado de mais de uma zona,Auto Hold,Bancos de couro,Banco do motorista com memória de ajuste,Chave presencial,Direção elétrica,Freio de estacionamento elétrico,Limitador de Velocidade,Retrovisores rebatíveis eletricamente,Rodas de liga leve,Sistema start stop,Teto Panorâmico,Teto solar elétrico,Troca de marcha no volante")))
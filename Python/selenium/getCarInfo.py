from bs4 import BeautifulSoup
import re
import pandas as pd
import time

def getCarInfo(pagina):
        doc = BeautifulSoup(pagina, "html.parser")
        year_td = doc.find_all(["td"], bgcolor="#ffffff")
        for td in year_td:
            print(td.get_text())
        '''year = year_td.find_next_sibling('td').get_text(strip=True)
        print("Ano: " + year)'''
        '''
        name = doc.find(["font"], size="4", face="arial", color="darkred")
        name = name.get_text(strip=True)
        def separate_words(text):
            words = text.split()
            first_word = words[0]
            second_word = words[1]
            remaining_words = ' '.join(words[2:])
            return first_word, second_word, remaining_words
        def remover_letras(string):
            nova_string = ''
            for char in string:
                if char == '.' or not char.isalpha():
                    nova_string += char
            return nova_string


        marca, modelo, versão = separate_words(name)

        print("Marca: ", marca)
        print("Modelo: ", modelo)
        print("Versão: ", versão)
        motor = remover_letras(versão)
        print("Motor: " + motor)

        year_td = doc.find(["td"], string="Ano")
        year = year_td.find_next_sibling('td').get_text(strip=True)
        print("Ano: " + year)

        revisao_td = doc.find(["td"], string="Revisões")
        revisao = revisao_td.find_next_sibling('td').get_text()
        def remove_non_numeric(text):
            return re.sub(r'\D', '', text)

        def separate_text(text):
            index = text.find("até")
            if index != -1:
                before = text[:index].strip()
                after = text[index + 3:].strip()
                return before, after
            else:
                return None

        def trazerValores(text):
            if text != 'Preços não tabelados':
                valoresPrimario = separate_text(text)
                valor1 = remove_non_numeric(valoresPrimario[0])
                valor2 = remove_non_numeric(valoresPrimario[1])
                valorDividido = int(valor2) / 10000
                valorPrincial = int(valor1) / valorDividido
            else:
                valorPrincial = "Não informado"
            return valorPrincial

        revisao = trazerValores(revisao)
        print("Revisao: " + str(revisao))


        garantia_td = doc.find(["td"], string="Garantia")
        garantia = garantia_td.find_next_sibling('td').get_text(strip=True)
        print("garantia: " + garantia)

        try:
            câmbio_td = doc.find(["td"], string="Câmbio")
            câmbio = câmbio_td.find_next_sibling('td').get_text()
            def check_for_manual(text):
                if "Manual" in text:
                    return "Manual"
                else:
                    return "Automático"

            câmbio = check_for_manual(câmbio)

            print("Câmbio: " + câmbio)
        except:
            câmbio_td = doc.find(["td"], string="câmbio")
            câmbio = câmbio_td.find_next_sibling('td').get_text()
            def check_for_manual(text):
                if "Manual" in text:
                    return "Manual"
                else:
                    return "Automático"

            câmbio = check_for_manual(câmbio)

            print("Câmbio: " + câmbio)


        ##
        ## Categoria = Configuração
        ##

        categoria_td = doc.find(["td"], string="Configuração")
        categoria = categoria_td.find_next_sibling('td').get_text(strip=True)
        print("categoria: " + categoria)

        porte_td = doc.find(["td"], string="Porte")
        porte = porte_td.find_next_sibling('td').get_text(strip=True)
        print("porte: " + porte)

        ##
        ## Propulsão = Propulsão
        ##
        try:
            propulsão_td = doc.find(["td"], string="Combustível ")
            propulsão = propulsão_td.find_next_sibling('td').get_text(strip=True)
            print("Propulsão: " + propulsão)
        except:
            propulsão_td = doc.find(["td"], string="Preço")
            propulsão_td = propulsão_td.find_parent('tr')
            propulsão_td = propulsão_td.find_next('tr')
            propulsão_td = propulsão_td.find_next('tr')
            propulsão_td = propulsão_td.find_all("td")
            propulsão_c = []
            for t in propulsão_td:
                propulsão_c.append(t.get_text(strip=True))
            propulsão = propulsão_c[1]
            print("Propulsão: " + propulsão)



        ##
        ## Cilindros = Cilindros
        ##
        try:
            cilindros_td = doc.find(["td"], string="Cilindros")
            cilindros = cilindros_td.find_next_sibling('td').get_text(strip=True)
            print("Cilindros: " + cilindros)
        except:
            print('eletrico não tem cilindro')
            cilindros = "eletrico não tem cilindro"

        ##
        ## Potência = Potência máxima
        ##
        '''
        propulsão = 2
        if propulsão == 'Eletricidade/gasolina':
            potência_td = doc.find(["td"], string="Potência combinada")
            potência1 = potência_td.find_next_sibling('td').get_text(strip=True)

            potência_td = doc.find(["td"], string="Autonomia elétrica")
            potência2 = potência_td.find_next_sibling('td').get_text(strip=True)

            potência = "Potencia: " + potência1 + " Autonomia elétrica: " + potência2
            print(potência)

        else:
            try:
                potência_td = doc.find(["td"], string="Potência  máxima")
                potência = potência_td.find_next_sibling('td').get_text(strip=True)
                print("Potencia: " + potência)
            except:
                try:
                    potência_td = doc.find(["td"], string="Potência combinada")
                    potência = potência_td.find_next_sibling('td').get_text(strip=True)
                    print("Potencia: " + potência)
                except:
                    try:
                        potência_td = doc.find(["td"], string="Potência")
                        potência = potência_td.find_next_sibling('td').get_text(strip=True)
                        print("Potencia: " + potência)
                    except:
                        print("Chegou aqui no braço")
                        time.sleep(20)
                        potência_td = doc.find(["td"], string="Potência gráfico")
                        potência = potência_td.find_next_sibling('td').get_text(strip=True)
                        print("Potencia: " + potência)
            


        ##
        ## Torque = Torque máximo
        ##
        try:
            torque_td = doc.find(["td"], string="Torque  máximo")
            torque = torque_td.find_next_sibling('td').get_text(strip=True)
            print("Torque: " + torque)
        except:
            try:
                torque_td = doc.find(["td"], string="Torque combinado")
                torque = torque_td.find_next_sibling('td').get_text(strip=True)
                print("Torque: " + torque)
            except:
                try:
                    torque_td = doc.find(["td"], string="Torque")
                    torque = torque_td.find_next_sibling('td').get_text(strip=True)
                    print("Torque: " + torque)
                except:
                    torque_td = doc.find(["td"], string="Torque gráfico")
                    torque = torque_td.find_next_sibling('td').get_text(strip=True)
                    print("Torque: " + torque)

        ##
        ## Velocidade Máxima = Velocidade máxima
        ##
        '''
        velocidade_td = doc.find(["td"], string="Velocidade máxima")
        velocidade = velocidade_td.find_next_sibling('td').get_text(strip=True)
        print("velocidade: " + velocidade)

        ##
        ## 0-100 = Aceleração 0-100 km/h
        ##

        zero_cem_td = doc.find(["td"], string="Aceleração 0-100 km/h")
        zero_cem = zero_cem_td.find_next_sibling('td').get_text(strip=True)
        print("Zero ao cem: " + zero_cem)

        ##
        ## Consumo Cidade (Km/L) = ta foda mas considera o gasolina Urbano
        ##
        try:
            gasoCid_td = doc.find(["td"], string="Urbano")
            gasoCid_tr = gasoCid_td.find_next('tr')
            gasoCid_tr2 = gasoCid_tr.find_all('td')
            gasoCid = gasoCid_tr2[1].get_text()
            print("Consumo Cidade: " + gasoCid)
        except:
            try:
                gasoCid_td = doc.find(["td"], string="Urbano")
                gasoCid = gasoCid_td.find_next_sibling('td').get_text(strip=True)
                print("Consumo Cidade: " + gasoCid)
            except:
                gasoCid = "Carro eletrico não tem"

            


        ##
        ## Consumo Estrada (Km/L) = ta foda tambem Rodoviário
        ##
        try:
            gasoEst_td = doc.find(["td"], string="Urbano")
            gasoEst_tr = gasoEst_td.find_next('tr')
            gasoEst_tr2 = gasoEst_tr.find_all('td')
            gasoEst = gasoEst_tr2[3].get_text()
            print("Consumo Estrada: " + gasoEst)
        except:
            try:
                gasoEst_td = doc.find(["td"], string="Rodoviário")
                gasoEst = gasoEst_td.find_next_sibling('td').get_text(strip=True)

                print("Consumo Estrada: " + gasoEst)
            except:
                gasoEst = "Carro eletrico não tem"

            
        


        ##
        ## Autonomia Urbana = ta foda mas é o gasolina assim como todos os outros Urbana
        ##
        try:
            gasoAutUrb_td = doc.find(["td"], string="Urbana")
            gasoAutUrb_tr = gasoAutUrb_td.find_next('tr')
            gasoAutUrb_tr2 = gasoAutUrb_tr.find_all('td')
            gasoAutUrb = gasoAutUrb_tr2[1].get_text()
            print("Autonomia Urbana: " + gasoAutUrb)
        except:
            try:
                gasoAutUrb_td = doc.find(["td"], string="AUTONOMIA")
                gasoAutUrb_tr = gasoAutUrb_td.find_parent('tr')
                gasoAutUrb_tr2 = gasoAutUrb_tr.find_next('tr')
                gasoAutUrb_tr3 = gasoAutUrb_tr2.find_next('tr')
                gasoAutUrb_tr4 = gasoAutUrb_tr3.find(["td"], string="Urbana")
                gasoAutUrb_tr5 = gasoAutUrb_tr4.find_next("td")
                gasoAutUrb = gasoAutUrb_tr5.get_text()
                print("Autonomia Urbana: " + gasoAutUrb)
            except:
                gasoAutUrb_td = doc.find(["td"], string="Autonomia")
                gasoAutUrb = gasoAutUrb_td.find_next_sibling('td').get_text(strip=True)
                print("Autonomia Urbana: " + gasoAutUrb)


        



        ##
        ## Autonomia Estrada = Rodoviária
        ##
        try:
            gasoAutEst_td = doc.find(["td"], string="Urbana")
            gasoAutEst_tr = gasoAutEst_td.find_next('tr')
            gasoAutEst_tr2 = gasoAutEst_tr.find_all('td')
            gasoAutEst = gasoAutEst_tr2[3].get_text()
            print("Autonomia Estrada: " + gasoAutEst)
        except:
            try:
                gasoAutEst_td = doc.find(["td"], string="AUTONOMIA")
                gasoAutEst_tr = gasoAutEst_td.find_parent('tr')
                gasoAutEst_tr2 = gasoAutEst_tr.find_next('tr')
                gasoAutEst_tr3 = gasoAutEst_tr2.find_next("tr")
                gasoAutEst_tr4 = gasoAutEst_tr3.find(["td"], string="Rodoviária")
                gasoAutEst_tr5 = gasoAutEst_tr4.find_next('td')
                gasoAutEst = gasoAutEst_tr5.get_text()
                print("Autonomia Estrada: " + gasoAutEst)
            except:
                gasoAutEst = "carro eletrico não tem"
        # gasoAutEst = gasoAutEst_tr3.get_text()
        # print("Autonomia Estrada: " + gasoAutEst)



        ##
        ## Tração = Tração
        ##

        tração_td = doc.find(["td"], string="Tração")
        tração = tração_td.find_next_sibling('td').get_text(strip=True)
        print("Tração: " + tração)

        ##
        ## Direção = Assitência
        ##

        direção_td = doc.find(["td"], string="Assistência")
        direção = direção_td.find_next_sibling('td').get_text(strip=True)

        print("Assistencia: " + direção)

        ##
        ## Suspensão Dianteira = Dianteira
        ##

        susDia_td = doc.find(["tr"], string="SUSPENSÃO")
        susDia_td2 = susDia_td.find_next('tr')
        susDia_td3 = susDia_td2.find_next('tr')
        susDia_td4 = susDia_td3.find_all('td')
        susDia = susDia_td4[1].get_text()
        print("Suspensão Dianteira: " + susDia)

        ##
        ## Suspensão Traseira = Traseira
        ##
        susTra_td = doc.find(["tr"], string="SUSPENSÃO")
        susTra_td2 = susTra_td.find_next('tr')
        susTra_td3 = susTra_td2.find_next('tr')
        susTra_td4 = susTra_td3.find_next('tr')
        susTra_td5 = susTra_td4.find_all('td')
        susTra = susTra_td5[1].get_text()
        print("Suspensão Traseira: " + susTra)

        ##
        ## Freios Dianteiros = Dianteiros
        ##

        freDia_td = doc.find(["td"], string="Dianteiros")
        freDia = freDia_td.find_next_sibling('td').get_text(strip=True)
        print("Freios Dianteiros: " + freDia)


        ##
        ## Freios Traseiros = Traseiros
        ##

        freTra_td = doc.find(["td"], string="Traseiros")
        freTra = freTra_td.find_next_sibling('td').get_text(strip=True)
        print("Freios Traseiros: " + freTra)

        ##
        ## Itens de Segurança = Equipamentos Segurança
        ##
        try:
            def remove_chars(string):
                chars_to_remove = ["'", "[", "]"]
                for char in chars_to_remove:
                    string = string.replace(char, "")
                return string

            start_td = doc.find(["font"], string=" SEGURANÇA")
            end_td = doc.find(['font'], string=' CONFORTO') 
            start_td = start_td.find_next('tr')
            end_td = end_td.find_parent('tr')
            caixa = []
            while start_td != end_td:
                caixa.append(start_td)
                start_td = start_td.find_next_sibling('tr')

            dados = BeautifulSoup(str(caixa), "html.parser")
            dados = dados.find_all('td')
            dadosSeg = []
            for dado in dados:
                if dado.get_text(strip=True) != '':
                    dadosSeg.append(dado.get_text(strip=True))
            dadosSeg = remove_chars(str(dadosSeg))
            print("itens de Segurança: " + str(dadosSeg))

        ##
        ## Itens de Conforto = Equipamentos Conforto
        ##
            start_td = doc.find(["font"], string=" CONFORTO")
            end_td = doc.find(['font'], string=' INFOTENIMENTO') 
            start_td = start_td.find_next('tr')
            end_td = end_td.find_parent('tr')
            caixa = []
            while start_td != end_td:
                caixa.append(start_td)
                start_td = start_td.find_next_sibling('tr')

            dados = BeautifulSoup(str(caixa), "html.parser")
            dados = dados.find_all('td')
            dadosConf = []
            for dado in dados:
                if dado.get_text(strip=True) != '':
                    dadosConf.append(dado.get_text(strip=True))
            dadosConf = remove_chars(str(dadosConf))
            print("Itens de Conforto: " + str(dadosConf))





            ##
            ## Itens de infotenimento = Equipamentos Infotenimento
            ##

            start_td = doc.find(["font"], string=" INFOTENIMENTO")
            end_td = doc.find(["font"], string="     Fotos")
            print(end_td)
            end_td = end_td.find_parent('tr')
            end_td = end_td.find_previous('tr')
            end_td = end_td.find_previous('tr')
            start_td = start_td.find_next('tr')
            caixa = []
            i = 0
            while start_td != end_td:
                caixa.append(start_td)
                if start_td.find_next_sibling('tr'):
                    start_td = start_td.find_next_sibling('tr')
                else:
                    break

            dados = BeautifulSoup(str(caixa), "html.parser")
            dados = dados.find_all('td')
            dadosInfo = []
            for dado in dados:
                if dado.get_text(strip=True) != '':
                    dadosInfo.append(dado.get_text(strip=True))
            print(len(dadosInfo))
            dadosInfo = remove_chars(str(dadosInfo))
            print("Itens de infotenimento: " + str(dadosInfo))
        except:
            dadosSeg = ""
            dadosConf = ""
            dadosInfo = ""

        
        ##
        ## Portas = Portas
        ##

        portas_td = doc.find(["td"], string="Portas")
        portas = portas_td.find_next_sibling('td').get_text(strip=True)
        print("Portas: " + portas)

        ##
        ## Lugares = Lugares
        ##

        lugares_td = doc.find(["td"], string="Lugares")
        lugares = lugares_td.find_next_sibling('td').get_text(strip=True)
        print("Lugares: " + lugares)

        ##
        ## Altura = Altura
        ##

        altura_td = doc.find(["td"], string="Altura")
        altura = altura_td.find_next_sibling('td').get_text(strip=True)
        print("Altura: " + altura)

        ##
        ## Largura = Largura
        ##

        largura_td = doc.find(["td"], string="Largura")
        largura = largura_td.find_next_sibling('td').get_text(strip=True)
        print("Largura: " + largura)

        ##
        ## Comprimento = Comprimento
        ##
        ##Conversa com lucas
        comprimento_td = doc.find(["td"], string="Comprimento")
        comprimento = comprimento_td.find_next_sibling('td').get_text(strip=True)
        print("Comprimento: " + comprimento)

        ##
        ## Peso = Peso
        ##

        peso_td = doc.find(["td"], string="Peso")
        peso = peso_td.find_next_sibling('td').get_text(strip=True)
        print("Peso: " + peso)

        ##
        ## Tanque = Tanque de combustível
        ##
        try:
            tanque_td = doc.find(["td"], string="Tanque de combustível")
            tanque = tanque_td.find_next_sibling('td').get_text(strip=True)
            print("Tanque: " + tanque)
        except:
            tanque_td = doc.find(["td"], string="Capacidade da bateria")
            tanque = tanque_td.find_next_sibling('td').get_text(strip=True)
            print("Tanque: " + tanque)
            

        ##
        ## Entre Eixos = Distância entre-eixos
        ##

        entEix_td = doc.find(["td"], string="Distância entre-eixos")
        entEix = entEix_td.find_next_sibling('td').get_text(strip=True)
        print("Entre Eixos: " + entEix)


        ## 
        ## Litragem real do porta malas = Porta-malas
        ##
        try:
            litRea_td = doc.find(["td"], string="Porta-malas ")
            litRea = litRea_td.find_next_sibling('td').get_text(strip=True)
            print("Litragem real do porta malas: " + litRea)
        except:
            litRea_td = doc.find(["td"], string="Caçamba")
            litRea = litRea_td.find_next_sibling('td').get_text(strip=True)
            print("Litragem real do porta malas: " + litRea)

        ##
        ## Pneus Dianteiros = Pneus/Dianteiros
        ##
        pneDia_td = doc.find(["td"], string="PNEUS")
        pneDia_td2 = pneDia_td.find_parent('tr')
        pneDia_td3 = pneDia_td2.find_next_sibling('tr')
        pneDia_td4 = pneDia_td3.find_next_sibling('tr')
        pneDia_td5 = pneDia_td4.find_all('td')
        pneDia = pneDia_td5[1].get_text()


        print("Pneus Dianteiros: " + pneDia)


        ##
        ## Pneus Traseiros = Pneus/Traseiros
        ##
        pneTra_td = pneDia_td4.find_next_sibling('tr')
        pneTra_td2 = pneTra_td.find_all('td')
        pneTra = pneTra_td2[1].get_text()
        print("Pneus Traseiros: " + pneTra)

        ##
        ## Estepe =  pode ter ou não ter Estepe
        ##
        if doc.find(["td"], string="Estepe"):
            estepe_td = doc.find(["td"], string="Estepe")
            estepe = estepe_td.find_next_sibling('td').get_text(strip=True)
        else:
            estepe = "Não informado"

        df = pd.read_excel('dados_carros.xlsx')
        nova_linha = {
            'Ano': year,
            'Marca': marca,
            'Modelo': modelo,
            'Versão': versão,
            'Preço (Seminovos tabela KBB)': '',
            'Preço parametro': '',
            'Preço do IPVA': '',
            'Valor médio de revisões': revisao,
            'Tempo de garantia': garantia,
            'Câmbio': câmbio,
            'Categoria': categoria,
            'Porte': porte,
            'Seguimento': "seguimento",
            'Propulsão': propulsão,
            'Motorização': motor,
            'Cilindros': cilindros,
            'Potência': potência,
            'Torque': torque,
            'Velocidade Máxima': velocidade,
            '0-100': zero_cem,
            'Consumo Parametrizado': '',
            'Consumo cidade (Km/L)': gasoCid,
            'Consumo Estrada (Km/L)': gasoEst,
            'Autonomia Urbana': gasoAutUrb,
            'Autonomia Estrada': gasoAutEst,
            'Tração': tração,
            'Direção': direção,
            'Suspensão dianteira': susDia,
            'Suspensão Traseira': susTra,
            'Freios Dianteiros': freDia,
            'Freios Traseiros': freTra,
            'Itens de segurança': dadosSeg,
            'Itens de Conforto': dadosConf,
            'Itens de Infotenimento': dadosInfo,
            'Portas': portas,
            'Lugares': lugares,
            'Altura': altura,
            'Largura': largura,
            'Comprimento': comprimento,
            'Peso': peso,
            'Tanque': tanque,
            'Entre Eixos': entEix,
            'Litragem real do porta malas': litRea,
            'Pneus Dianteiros': pneDia,
            'Pneus Traseiros': pneTra,
            'Estepe': estepe,
            'Principais destaques do veículo': '',
            'Justificativa padrão': '',
            'Pontos Positivos': '',
            'Pontos Negativos': '',
            'Problemas Crônicos': '',
            'Facilidade de Revenda': '',
            'Informações de mercado': '',
            'Reposição de peças': '',
            'Mêcanica': '',
            'Segurança': '',
            'Conforto': '',
            'Tecnologia': '',
            'Performance': '',
            'Consumo': '',
            'Acabamento': '',
            'Espaço Interno': '',
            'Custo-beneficio': '',
            'Avaliação Geral': ''
        }

        df = df._append(nova_linha, ignore_index=True)
        df.to_excel('dados_carros.xlsx', index=False)
    except Exception as erro:
        print(erro)
        erro2 = []
        erro2.append(name)
        erro2.append(str(erro))
        filename = "erro de carros.txt"

        with open(filename, "a") as f:
            for wrong in erro2:
                f.write(wrong + "\n")'''

        return 'error'
        
        




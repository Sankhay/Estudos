import pandas as pd

nome_arquivo = '/home/davi/Codigos/Estudos/Estudos/Python/Programa_Excel/dados_carros.xlsx'

numero_da_linha = 2

df = pd.read_excel(nome_arquivo)

linha_especifica = df.iloc[numero_da_linha]


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


print(linha_especifica)
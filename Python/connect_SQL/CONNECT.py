import pyodbc

def conecta_ao_banco(driver, server, database, username, password):
    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor

conexao, cursor = conecta_ao_banco('{ODBC Driver 17 for SQL Server}', "177.154.191.251", "indkarco_form", "indkarco_davi", "D@vi4093")

print(conexao)
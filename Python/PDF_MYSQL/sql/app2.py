import mysql.connector

connection = mysql.connector.connect(
    user="indkarco_davi", password="D@vi4093",
    host="177.154.191.251", database="indkarco_main"
)

select_query = "select pdf from indications where id = 6"
cursor = connection.cursor()
cursor.execute(select_query)
result = cursor.fetchone()

if result is not None:
    pdf_data = result[0]

    save_path = '3.pdf'
    with open(save_path, 'wb') as file:
        file.write(pdf_data)
        print('Arquivo salvo com sucesso.')
else:
    print('Arquivo não encontrado')

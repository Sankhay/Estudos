import mysql.connector

connection = mysql.connector.connect(
    user="indkarco_davi", password="D@vi4093",
    host="177.154.191.251", database="indkarco_main"
)

with open('2.pdf', 'rb') as file:
    pdf_data = file.read()

insert_query = "INSERT INTO indications (id_form, pdf) VALUES (%s, %s)"
values = (6, pdf_data)
cursor = connection.cursor()
cursor.execute(insert_query, values)
connection.commit()

cursor.close()
connection.close()
from flask import Flask, render_template, session, request, jsonify
import mysql.connector
import jwt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sendData', methods=['POST'])
def sendData():
    try:
        data = request.form.to_dict()
        print(data)
        print(data['email'])
        print(data['senha'])
        #name = data['email']
        #age = data['password']
        conexao = mysql.connector.connect(user='root', password='4093',
                                        host='localhost', database='client')

        cursor = conexao.cursor()
        query2 = f'''INSERT INTO clients (name, password, cep, cpf, email, phone, secondary_phone)
                        VALUES ('{data["nome"]}', '{data["senha"]}', '{data["cep"]}', '{data["cpf"]}', '{data["email"]}', '{data["phone"]}', '{data["secondary_phone"]}');'''

        query = query2
        print(query)
        cursor.execute(query)
        conexao.commit()
        response = {'oi': 'oi'}

        return jsonify(response)
    except:
        return jsonify('oi')
        print('Erro no valor inserido')

@app.route('/getData', methods=['POST'])
def getData():
  
        data = request.form.to_dict()
        print(data)
        conexao = mysql.connector.connect(user='root', password='4093', host='localhost', database='client')
        
        cursor = conexao.cursor()
        query2 = f'''select id from clients where email = "{data["email"]}" and password = "{data["password"]}"'''
        print(query2)
        query = query2
        cursor.execute(query)
        nome = cursor.fetchone()
        nome = nome[0]
        response = {'nome': nome}
        token = jwt.encode({'id': nome}, app.config['SECRET_KEY'])
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        print(payload)

        return jsonify({'token': token})





if __name__ == '__main__':
    app.run(debug=True)
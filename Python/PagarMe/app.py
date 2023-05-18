from flask import Flask, render_template, request, jsonify
import requests
import json
from pprint import pprint as pp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/makeClient', methods=['POST'])
def makeClient():
    data = request.get_json()
    phone_area = data['phone_area']
    phone = data['phone']
    birthdate = data['birthdate']
    id = data['id']
    nome = data['nome']
    email = data['email']
    cpf = data['cpf']
    print(phone)
    print('')
    print(phone_area)
    print('')
    print(birthdate)
    print('')
    print(id)
    print('')
    print(nome)
    print('')
    print(email)
    print('')
    print(cpf)

    api_key = 'Basic c2tfdGVzdF81MFk0WDRsTXQ0VHFYMVdvOg=='
    url = 'https://api.pagar.me/core/v5/customers'

    payload = {
        "phones": {"mobile_phone": {
            "country_code": "55",
            "area_code": phone_area,
            "number": phone 
        }},
        "birthdate": birthdate,
        "code": id,
        "name": nome,
        "email": email,
        "document": cpf,
        "document_type": "CPF",
        "type": "individual"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": api_key
    }


    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print('Cliente criado com sucesso')
        codigo = response.text
        codigo = json.loads(codigo)
        code_client = codigo['id']
        print(codigo['id'])
    else:
        print(response.text)
        print(f'Erro ao criar cliente: {response.json()}')
    
    url = "https://api.pagar.me/core/v5/orders"

    payload = {
        "items": [
            {
                "amount": 1,
                "description": "Formulario",
                "quantity": 1,
                "code": '1'
            }
        ],
        "payments": [
            {
                "checkout": {
                    "accepted_payment_methods": ["pix", "credit_card"],
                    "expires_in": 1,
                    "Pix": {"expires_in": 300}
                },
                "Pix": {"expires_in": 300},
                "payment_method": "checkout"
            }
        ],
        "customer_id": code_client
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": api_key
    }


    response = requests.post(url, json=payload, headers=headers)
    link = response.text
    link = json.loads(link)
    link = link['checkouts'][0]['payment_url']

    
    return jsonify(link)



if __name__ == "__main__":
    app.run(port=2000)
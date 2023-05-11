import jwt

payload = {'user_id': 123456}
secret = 'seu-segredo-aqui'

# Gerar o token JWT
token = jwt.encode(payload, secret, algorithm='HS256')

print(token)
import requests
from requests import Session
import segredos
from pprint import pprint as pp

'''url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': segredos.API_KEY,
}

r = requests.get(url, headers=headers)'''

key = '28762d98-e4b9-462f-8f4d-8a2645a11766'
class CMC:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key}
        self.session = Session()
        self.session.headers.update(self.headers)
        print(self.headers)

    def getAllCoints(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url, headers=self.headers)
        data = r.json()['data']
        return data
    
    def getPrice(self, symbol):
        url = self.apiurl + '/v2/cryptocurrency/quotes/latest'
        parameters = {'id': "1,2"}
        r = self.session.get(url, headers=self.headers, params=parameters)
        data = r.json()['data']
        return data


cmc = CMC(segredos.API_KEY)

pp(cmc.getPrice('BTC'))

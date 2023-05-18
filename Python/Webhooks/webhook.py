import requests
import json

webhook_url = 'https://cbde-2804-40a8-197-e500-c223-ae9d-15e4-9961.sa.ngrok.io/webhook'

data = {'name': 'brad',
        'Channel URL': 'test_url'}

r = requests.post(webhook_url, json=data, headers={'Content-Type': 'application/json'})
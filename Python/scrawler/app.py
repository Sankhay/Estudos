import requests
import itertools
import random
import time

proxies = [
    'http://187.63.157.60:999',
    'http://201.91.82.155:3128',
    'http://177.85.245.87:8088',
    'http://181.191.94.126:8999',
    'http://201.76.218.220:9898',
    'http://187.1.57.206:20183',
    'http://201.30.192.149:8080',
    'http://186.251.224.82:8080',
    'http://187.62.158.168:8080',
    'http://177.130.104.58:33333',
    'http://191.243.46.30:43241',
    'http://177.126.129.43:8080',
    'http://131.161.65.17:9999',
    'http://177.207.208.35:8080',
    'http://187.115.138.75:8080',
    'http://189.45.10.99:3128',
    'http://179.189.215.53:3128',
    'http://45.224.150.46:8080',
    'http://45.224.150.62:8080',
    'http://45.224.150.45:8080',
    'http://177.8.170.162:8080',
    'http://138.36.79.157:8080',
    'http://177.85.245.87:8088',
    'http://201.21.32.214:8080',
    'http://177.11.151.253:8080',
    'http://170.82.223.14:8080',
    'http://200.169.160.30:8080',
    'http://45.186.22.218:8080',
    'http://45.160.167.50:8080',
    'http://138.186.157.26:80',
    'http://177.22.187.153:80',
    'http://179.51.179.24:8080',
    'http://165.225.214.89:10311',
    'http://186.65.107.26:666',
    'http://189.90.241.202:8090',
    'http://89.117.32.209:80',
    'http://170.79.12.75:9090',
    'http://200.229.224.221:8080',
    'http://179.189.50.160:80',
    'http://177.136.40.44:8080'
    # Add more proxies from Brazil as needed
]

url = 'https://www.carrosnaweb.com.br/m/fichadetalhe.asp?codigo=14828'
success_count = 0

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    # Add more user-agents as needed
]

# Create an infinite iterator over the user-agents
user_agent_cycle = itertools.cycle(user_agents)

# Create an infinite iterator over the proxies
proxy_cycle = itertools.cycle(proxies)

for _ in range(len(proxies)):
    try:
        # Get the next user-agent and proxy from the cycles
        user_agent = next(user_agent_cycle)
        proxy = next(proxy_cycle)

        headers = {'User-Agent': user_agent}

        # Randomize the order of headers
        headers['Accept-Language'] = 'pt-BR,en;q=0.9'
        headers['Referer'] = 'https://www.google.com/'

        # Set a random delay before making the request
        delay = random.uniform(1.5, 3.5)
        time.sleep(delay)

        response = requests.get(url, proxies={'http': proxy}, headers=headers)
        
        print(f'Successful request using proxy: {response}')
        print(response.text)  # Print the HTML content of the page

    except requests.exceptions.RequestException as e:
        print(f'Request failed using proxy: {proxy}. Error: {e}')

print(f'Total successful requests: {success_count}')


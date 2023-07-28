import requests
def pegar_proxy():
    def get_proxy_ip():
        url = "https://acq.iemoapi.com/getProxyIp?regions=br&lb=1&return_type=txt&protocol=http&num=1"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip()
            else:
                print(f"Erro ao obter o IP do proxy. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na solicitação HTTP: {e}")
            return None

    proxy_ip = get_proxy_ip()
    def extract_ip_port(proxy_str):
        ip, port = proxy_str.split(":")
        return ip, port

    proxy_str = proxy_ip
    ip, port = extract_ip_port(proxy_str)
    return ip, port


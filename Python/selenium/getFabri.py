from bs4 import BeautifulSoup

def getFabri(html12):
    doc = BeautifulSoup(html12, "html.parser")

    links = doc.find_all(["font"], style="font-size: 15px; font-family:arial; color:black;")

    links_reais = []

    for link in links:
        a_tags = link.find_all('a')
        for a_tag in a_tags:
            text = a_tag.get_text()
            if text != "Todos":
                links_reais.append(a_tag.get('href'))

    return links_reais

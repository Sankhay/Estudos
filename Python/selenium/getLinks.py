from bs4 import BeautifulSoup

def getLinksYears(html12):
    doc = BeautifulSoup(html12, "html.parser")

    links = doc.find_all(["font"], style="font-size: 15px; font-family:arial; color:black;")
    links_completo = []

    for link in links:
        a_tags = link.find_all('a')
        for a_tag in a_tags:
            text = a_tag.get_text()
            if text != "Todos":
                year = int(text)
                if year > 2009:
                    links_completo.append(a_tag.get('href'))

    return links_completo










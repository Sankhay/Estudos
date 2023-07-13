from bs4 import BeautifulSoup

with open("teste.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

element = doc.find("b", string="Próxima")
if element is not None:
    parent_element = element.parent
    link_real = parent_element.get('href')
    print(link_real)


from bs4 import BeautifulSoup

with open("erro.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

links = doc.find_all(["td"], bgcolor="#ffffff", align="left")
if links:
    print("tem")
else:
    print("não tem")
    

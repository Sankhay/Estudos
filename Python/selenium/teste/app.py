from bs4 import BeautifulSoup
import re
#import requests

#url = "https://www.newegg.com/gigabyte-geforce-rtx-4070-ti-gv-n407tgaming-oc-12gd/p/N82E16814932580"

#result = requests.get(url)
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
#if you going to search by class use class_
#going to search for something ahead of something string=re.compile("\$.*")
result = doc.find_all(["font"], size="4", color="darkred", limit=1)
print(result)
#prices = doc.find_all(string="$")
#parent = prices[0].parent
#strong = parent.find("strong")
#print(strong.string)
#with open("index.html", "r") as f:
 #   doc = BeautifulSoup(f, "html.parser")

#print(doc.prettify())
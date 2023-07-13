from ast import Lambda
from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint

search_term = input("What product do you want to search for?")

url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"

page = requests.get(url).text

doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text")
pages = int(str(page_text).split("/")[1][8])

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    items = div.find_all(string=re.compile(search_term))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong
        if price != None:
            price = price.string
            items_found[item] = {"price": int(price.replace(",", "")), "link": link}
        else:
            items_found[item] = {"price": "None", "link": link}
 
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'] if x[1]['price'] is not None else int('inf'))

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
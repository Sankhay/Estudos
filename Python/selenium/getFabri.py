from bs4 import BeautifulSoup

excluidos = ['Adamo',
'Todos',
'Agrale',
'Ariel',
'Asia',
'Avallone',
'Bianco',
'BRM',
'Caterham',
'CBT',
'Chamonix',
'Chana',
'Changan',
'Cross Lander',
'Daewoo',
'Daihatsu',
'DeLorean',
'Effa',
'Engesa',
'Enseada',
'Envemo',
'Farus',
'Geely',
'Gurgel',
'Hafei',
'Hennessey',
'Hofstetter',
'Iveco',
'Jinbei',
'JPX',
'Koenigsegg',
'KTM',
'Lada',
'Lafer',
'Lincoln',
'Lobini',
'Mahindra',
'Mercury',
'MG',
'Miura',
'Plymouth',
'Pontiac',
'Ragge',
'Rely',
'Saab',
'Saleen',
'Santa Matilde',
'Saturn',
'Seat',
'Shineray',
'SSC',
'TAC',
'W Motors']

def getFabri(html12):
    doc = BeautifulSoup(html12, "html.parser")

    links = doc.find_all(["font"], style="font-size: 15px; font-family:arial; color:black;")


    links_reais = []

    for link in links:
        a_tags = link.find_all('a')
        for a_tag in a_tags:
            text = a_tag.get_text()
            if text not in excluidos:
                links_reais.append(a_tag.get('href'))

    return links_reais


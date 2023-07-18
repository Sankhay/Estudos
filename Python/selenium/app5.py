with open('nomecertos.txt', 'r') as file:
    urls = file.read()

urls = str(urls)

separado = urls.split("catalogo")

for c in separado:
    print("catalogo" + c)

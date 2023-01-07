import bs4
import requests

# Obtener las diferentes paginas para hacer el scraping
# Crear url sin número de pagina
url = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista que guardara los titulos de los libros con 4 o más estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1,51):

    # Crear la sopa de cada pagina
    url_pagina = url.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros de cada pagina
    libros = sopa.select('.product_pod')

    # Iterar en los libros
    for libro in libros:

        # Chequear si tienen 4 o mas estrellas de rating
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en una variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# Ver los libros de 4 y 5 entrellas en consola
for t in titulos_rating_alto:
    print(t)

"""resultados = requests.get(url.format('1'))
    sopa = bs4.BeautifulSoup(resultados.text, 'lxml')
    
    #print(sopa.select('.product_pod'))
    libros = sopa.select('.product_pod')
    estrellas = libros[0].select('.star-rating.Three')
    titulo = libros[0].select('a')[1]['title']
"""

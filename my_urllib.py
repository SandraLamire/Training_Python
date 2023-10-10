import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter URL :')
# exemple : url = 'http://www.dr-chuck.com/page1.htm'

# possible de tout lire sans boucle si fichier pas trop volumineux
html = urllib.request.urlopen(url).read()
# création d'un Soup object sur lequel on peut faire des requêtes
soup = BeautifulSoup(html, 'html.parser')

# récupérer toutes les balises d'ancrage HTML
tags = soup('a')
for tag in tags:
    # retirer le href de chaque balise avant de d'imprimer le href
    print(tag.get('href', None))
    
# renvoie le seul lien existant dans la page renvoyé par l'url =
# http://www.dr-chuck.com/page2.htm
    
    

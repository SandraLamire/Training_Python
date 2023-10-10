# To run this, install Beautiful Soup
# https://pypi.python.org/pypi/beautifulsoup4
# or download the file http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# or lauch (.venv) PS C:\Users\Sandra\Documents\Python>pip install urllib3
# and pip install beautifulsoup4 (/!\ Lancer dans l'environnement virtuel (.venv))

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors => pour sites https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# ex : http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags (balises <a>)
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


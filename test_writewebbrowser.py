import socket

# création d'un socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecter le socket
mysock.connect(('data.pr4e.org', 80))
# encode : Unicode to UTF-8
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# envoi de la requête
mysock.send(cmd)

while True:
    # réception de 512 caractères (en bytes = UTF-8)
    data = mysock.recv(512)
    # si moins de 1 caractère reçu
    if len(data) < 1:
        break
    # sinon decode : UTF-8 to Unicode 
    print(data.decode(),end='')
    # déconnecter le socket
mysock.close()


# CE CODE CREE UN WEB BROWSER SIMPLE en utilsant Telnet (= non protégé): 

# HTTP/1.1 200 OK
# Date: Mon, 09 Oct 2023 15:12:17 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain
#
# But soft what light through yonder window breaks     
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief


# SI ON IMPORTE LA LIBRAIRIE urlilb : + simple mais ne renvoie que le corps, pas l'en-tête
import urllib.request, urllib.parse, urllib.error

fhand1 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand1:
    print(line.decode().strip())
    
# But soft what light through yonder window 
# breaks
# It is the east and Juliet is the sun      
# Arise fair sun and kill the envious moon  
# Who is already sick and pale with grief 


# OU si on veut compter les mots
import urllib.request, urllib.parse, urllib.error

fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

print("Comptage des mots :")
counts = dict()
for line in fhand2:
    # print(line.decode().strip()) ou
    words = line.decode().split()
    for word in words:
        # comptage des mots
        counts[word] = counts.get(word, 0) + 1
print(counts)

# renvoie
# {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 
# 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 
# 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 
# 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

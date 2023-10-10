import urllib.request, urllib.parse, urllib.error
import json

# API utilisée trouvée sur https://opencagedata.com/
serviceurl = "https://api.opencagedata.com/geocode/v1/json?"

# clé API OpenCage perso créée sur le site
cle_api_opencage = 'c4f2bee275ea4e7b8af0a7a087217820'

while True:
    address = input("Enter location:")
    if len(address) < 1:
        break

    # Ajouter le paramètre 'key' avec la clé API OpenCage
    url = f"{serviceurl}{urllib.parse.urlencode({'q': address, 'key': cle_api_opencage})}"

    print("Retrieving", url)
    response = urllib.request.urlopen(url)
    
    # Imprimer les en-têtes (headers)
    headers = response.info()
    print("Headers:")
    print(headers)
    
    # Headers:
    # date: Tue, 10 Oct 2023 14:08:47 GMT
    # server: Apache
    # access-control-allow-origin: *
    # x-ratelimit-limit: 2500
    # x-ratelimit-remaining: 2493
    # x-ratelimit-reset: 1696982400
    # vary: Accept-Encoding
    # x-frame-options: DENY
    # x-xss-protection: 1; mode=block
    # transfer-encoding: chunked
    # content-type: application/json; charset=utf-8
    # strict-transport-security: max-age=31536000; includeSubDomains; preload
    # connection: close
    
    data = response.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"]["message"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue
    
    # afficher un exemple de JSON reçu (utile pour débugg - indent inutile dans ce cas car pas de dictionnaires dans la liste reçue)
    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["lat"]
    lng = js["results"][0]["geometry"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted"]
    print(location)

    # Enter location:Rennes, Bretagne
    # Retrieving https://api.opencagedata.com/geocode/v1/json?q=Rennes%2C+Bretagne&key=c4f2bee275ea4e7b8af0a7a087217820
    # Retrieved 11458 characters
    # lat 48.1113387 lng -1.6800198
    # Rennes, Ille-et-Vilaine, France
    
    
#------------------------------------------------------------#
# Format du JSON envoyé par https://opencagedata.com/demo :

# Full response in the JSON Response section
# 🇫🇷 Rennes, Ille-et-Vilaine, France
# 48.1113387, -1.6800198
# _category: place
# _type: city
# 🇫🇷 Rennes, Ille-et-Vilaine, France
# 48.156836, -1.8144255
# _category: place
# _type: municipality
# 🇫🇷 Rennes, Place de la Gare, 35000 Rennes, France
# 48.1031932, -1.6723809
# _category: transportation
# _type: railway
# 🇫🇷 Rennes, Place de la Mairie, 35000 Rennes, France
# 48.1113618, -1.6800957
# _category: government
# _type: townhall
# 🇫🇷 Rennes, Esplanade Fulgence Bienvenüe, 35000 Rennes, France
# 48.102893, -1.6716875
# _category: transportation
# _type: railway
# 🇫🇷 Rennes, Esplanade Fulgence Bienvenüe, 35032 Rennes, France
# 48.1027514, -1.6716953
# _category: transportation
# _type: railway
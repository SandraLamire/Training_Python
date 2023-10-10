import json

# type = intl => internationalisation
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }    
}'''

# retourne un dictionnaire nommé info qui transforme le json en python
info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])

# Name: Chuck
# Hide: yes

input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Brent"
    }    
]'''

# retourne une liste composée de 2 dictionnaires
info_lst = json.loads(input)
print("User count:", len(info_lst))
for item in info_lst:
    print("Name", item["name"])
    print("Id", item["id"])
    print("Attribute", item["x"])
    
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7

# import json

# data = 65

# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)
    

import json

data = 6

    # 1️⃣ Essayer de lire le fichier s'il existe
try:
    with open("data.json", "r") as f:
        contenu = json.load(f)

    if not isinstance(contenu, list):
            contenu = [contenu] 
except FileNotFoundError:
    contenu = []     # si le fichier n'existe pas encore → liste vide

    # 2️⃣ Ajouter la nouvelle valeur
contenu.append(data)

    # 3️⃣ Réécrire toute la liste dans le fichier JSON
with open("data.json", "w") as f:
    json.dump(contenu, f, indent=4)

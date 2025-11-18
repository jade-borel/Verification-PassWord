# def generer_mdp():
#     while True:
#         mot_de_passe = input("Veuillez entrer votre mot de passe : ")
#         if not len(mot_de_passe)>=8 :
#             print("Le mot de passe doit contenir au moins 8 caractères.")
#         elif not any(i.isupper() for i in mot_de_passe) :
#             print("Le mot de passe doit contenir au moins une lettre majuscule.")
#         elif not any(i.islower() for i in mot_de_passe) :
#             print("Le mot de passe doit contenir au moins une lettre minuscule.")
#         elif not any(i.isdigit() for i in mot_de_passe) :
#             print("Le mot de passe doit contenir au moins un chiffre.")
#         elif not any(c in "!@#$%^&*" for c in mot_de_passe):
#             print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
#         else:
#             print("Le mot de passe est correct et sécurisé !")
#             break  # tout est correct

# generer_mdp()







import hashlib
import json

def generer_mdp():
    while True:
        mot_de_passe = input("Veuillez entrer votre mot de passe : ")
        if not len(mot_de_passe)>=8 :
            print("Le mot de passe doit contenir au moins 8 caractères.")
        elif not any(i.isupper() for i in mot_de_passe) :
            print("Le mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(i.islower() for i in mot_de_passe) :
            print("Le mot de passe doit contenir au moins une lettre minuscule.")
        elif not any(i.isdigit() for i in mot_de_passe) :
            print("Le mot de passe doit contenir au moins un chiffre.")
        elif not any(i in "!@#$%^&*" for i in mot_de_passe):
            print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        else:
            mdp_hache = hashlib.sha256(mot_de_passe.encode()).hexdigest()
            print("Le mot de passe est correct et sécurisé !")
            print("Mot de passe haché (SHA-256) :")
            print(mdp_hache)
            break  # tout est correct

    try:
        with open("mdp_hache.json", "r") as f:
            contenu = json.load(f)
    except FileNotFoundError:
        contenu = []

    if mdp_hache in contenu:
        print("Mot de passe déjà existant dans la liste")
    else :
        contenu.append(mdp_hache)
        print("Mot de passe ajouté à la liste avec succés ! ")

    with open("mdp_hache.json", "w") as f:
        json.dump(contenu, f, indent=4)

    while True : 
        reponse = input("Voulez-vous afficher tous les mots de passer enregistrés ? (Y/n) : ")
        if reponse == "Y" :    
            print(json.dumps(contenu, indent=4))
            break
        elif reponse == "n" :
            print("Réponse prise en compte, à bientot ! ")
            break
        else :
            print("Réponse invalide, veuillez repondre par 'Y' ou 'n' ")


generer_mdp()
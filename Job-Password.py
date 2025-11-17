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
        elif not any(c in "!@#$%^&*" for c in mot_de_passe):
            print("Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        else:
            print("Le mot de passe est correct et sécurisé !")
            break  # tout est correct

generer_mdp()
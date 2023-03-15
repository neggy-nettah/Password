import hashlib 
import json
from getpass import getpass 
'''J'utilise getpass() pour que le mot de passe ne soit pas visible dans le terminal. Normalement,
les caractères saisis devraient s'afficher sous forme d'étoiles (*), mais il semble que cela ne
fonctionne pas avec certains IDE."'''


# Définition des exigences pour le mot de passe
caracteres_autorises = ['!', '*', '?', '%', '#', '@', '&', '+', '=']
exigences = [
    'au moins 8 caractères',
    'au moins une majuscule',
    'au moins une minuscule',
    'au moins un chiffre',
    f'au moins un des caractères suivants: {", ".join(caracteres_autorises)}'
]

utilisateur = input("Entrez votre nom d'utilisateur: ")  
mot_de_passe_valide = False

# Boucle pour demander à l'utilisateur de saisir un mot de passe valide
while not mot_de_passe_valide:
    mot_de_passe = getpass("Entrez un mot de passe qui contient au moins une majuscule, une minuscule, 8 caractères, un chiffre, un caractère spécial (!, *, ?, %, #, @, &, +, =): ")
    majuscule, minuscule, chiffre, caractere_special = False, False, False, False # Initialiser les variables pour vérifier les exigences du mot de passe
    for c in mot_de_passe: # Parcourir tous les caractères du mot de passe pour vérifier s'ils respectent les exigences
        if c.isupper():
            majuscule = True
        elif c.islower():
            minuscule = True
        elif c.isdigit():
            chiffre = True
        elif c in caracteres_autorises:
            caractere_special = True
            
    # J'utilise plusieurs if car je veux que chaque condition soit vérifiée afin d'informer l'utilisateur de toutes les exigences.
    if not majuscule:
        print("Le mot de passe doit contenir au moins une majuscule.")
    if not minuscule:
        print("Le mot de passe doit contenir au moins une minuscule.")
    if not chiffre:
        print("Le mot de passe doit contenir au moins un chiffre.")
    if not caractere_special:
        print(f"Le mot de passe doit contenir au moins un caractère spécial parmi {', '.join(caracteres_autorises)}.")
    if len(mot_de_passe) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
    
    if all([majuscule, minuscule, chiffre, caractere_special, len(mot_de_passe) >= 8]):
        mot_de_passe_valide = True
    else:
        print("Le mot de passe est invalide. Veuillez réessayer.")

# Sauvegarder le mot de passe haché dans un dictionnaire
x = mot_de_passe
y = hashlib.sha256(x.encode('utf-8')).hexdigest()
print("Le mot de passe est valide.")
info_utilisateur = {"utilisateur": utilisateur, "mot_de_passe": y}

# Écrire le dictionnaire dans un fichier JSON
with open('data.json', 'a+') as data_mdp:
    data_mdp.write(json.dumps(info_utilisateur, ensure_ascii=False) + '\n')

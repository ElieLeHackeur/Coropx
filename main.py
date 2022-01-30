from sys import argv
from os.path import isfile
from os import rename

caractere = "a"
ecriture = ""

if len(argv) < 3:
    print("\nErreur : Pas assez d'arguments \nExemple : nomdufichier pdf 500 \nCette commande va creer un fichier .pdf corrompu de 500 octets\n")
    exit()

if len(argv) > 3:
    print("\nErreur : Trop d'arguments \nExemple : nomdufichier pdf 500 \nCette commande va creer un fichier .pdf corrompu de 500 octets\n")
    exit()

type_de_fichier = argv[1]
taille_du_fichier = argv[2]

for i in range(int(taille_du_fichier)):
    ecriture += caractere
    
with open('fichier.txt', "w") as f :
    f.write(ecriture)
    f.close()

rename('fichier.txt', f'fichier.{type_de_fichier}')

print("le fichier a été créé")

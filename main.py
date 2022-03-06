from sys import argv
from os.path import isfile
from os import rename

caractere = "a"
ecriture = ""

if len(argv) < 4:
    print("\nErreur : Pas assez d'arguments. \nUtilisation : Python3 create.py [nom] [extention] [octets]\n")
    exit()

if len(argv) > 4:
    print("\nErreur : trop assez d'arguments. \nUtilisation : Python3 create.py [nom] [extention] [octets]\n")
    exit()

nom = argv[1]
ext = argv[2]
octet = argv[3]

for i in range(int(octet)):
    ecriture += caractere
    
with open('fichier.txt', "w") as f :
    f.write(ecriture)
    f.close()

rename('fichier.txt', f'{nom}.{ext}')

print("le fichier a été créé")

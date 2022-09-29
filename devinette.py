#James Lanthier 402
#TP2 jeu de la devinette
import random

chiffre = random.randint(1, 100)
nbessaie = 0
print('J ai choisi un nombre entre 0 et 100. À vous de le deviner....')
Essai = input('Entrer votre essaie:')
nbessaie + 1
if Essai<chiffre:
    print('Mauvaise réponse, le nombre est plus grand que')
if Essai>chiffre:
    print('Mauvaise réponse, le nombre est plus grand que')
if Essai==chiffre:
    print('Bravo! Bonne réponse/Vous avez réussi en : ')
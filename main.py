#James Lanthier 402
#TP2 jeu de la devinette
import random

chiffre = random.randint(1, 100)
nbessaie = 0



def start():
    print('J ai choisi un nombre entre 0 et 100. À vous de le deviner....')
    main()

def main():
    essai = int(input('Entrer votre essaie:'))
    nbessaie + 1
    if essai < chiffre:
        print('Mauvaise réponse, le nombre est plus grand que', essai)
        main()
    if essai > chiffre:
        print('Mauvaise réponse, le nombre est plus grand que')
        main()
    if essai == chiffre:
        print('Bravo! Bonne réponse/Vous avez réussi en : ')

start()
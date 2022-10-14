#James Lanthier 402
#TP2 jeu de la devinette
import random

jouer = True
chiffre = random.randint(0, 100)
nbessaie = 0

while jouer:
    essai = int(input('Entrer votre essaie:'))

    if essai < chiffre:
        print('Mauvaise réponse, le nombre est plus grand que', essai)
        nbessaie += 1


    elif essai > chiffre:
        print('Mauvaise réponse, le nombre est plus petit que', essai)
        nbessaie += 1


    elif essai == chiffre:
        print('Bravo! Bonne réponse/Vous avez réussi en : ', nbessaie, 'essaie')
        restart = input('Voulez-vous faire une autre partie (o,n)?')

        if restart == 'n':
            print('Merci et au revoir... ')
            jouer = False

        elif restart == 'o':
            chiffre = random.randint(0, 10)
            nbessaie = 0


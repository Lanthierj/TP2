"""James Lanthier 402
TP2 jeu de la devinette
Le code permet de jouer a un jeu qui est une devinnete. Tu dois deviner le nombre qui a été choisi par l'ordinateur en le moins d'essaie possible.
"""
import random
jouer = True
chiffre = random.randint(0, 100)
nbessaie = 0
def main():
    """
Fait un jeu de devinnette a l'utilisateur en choississant un nombre aléatoire
    :return:
    """
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

main()
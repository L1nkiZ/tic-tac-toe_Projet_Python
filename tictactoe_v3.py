from ast import Return
from graphicalgrid import GraphicalGrid


def crée_grille (nombre_cote):
    grille = []
    for i in range (nombre_cote):
        l1 = []
        l2 = []
        for j in range (nombre_cote):
            l1 = [' ']
            l2 = l2 + l1
        grille.append(l2)
    return grille


def taille_cote(grille):
    n = len(grille)
    return n


def verif (grille, i, j):
    #test = plateau[i][j] 
    if grille[i][j] == (' '):
        return True
    else:
        return False
        

def ecrire(grille, i, j, symbole):
    if symbole != 'O' and symbole != 'X':
        print("Le symbole n'est pas bon")
    elif grille[i][j] == (' '):
        grille[i][j] = symbole
    else:
        print ("La case est occupé !")
    return grille
    

def effacer (grille, i, j):
    if i >= len(grille):
        print("La valeur de i est trop grande !")
    elif j >= len(grille):
        print("La valeur de j est trop grande !")
    else:
        grille [i][j] = (' ')
    return grille


def est (grille, i, j, symbole):
    if i >= len(grille):
        print("La valeur de i est trop grande !")
    elif j >= len(grille):
        print("La valeur de j est trop grande !")
    else:
        if grille[i][j] == symbole:
            return True
        else:
            return False


def affiche (grille):
    for i in range(len(grille)):
        print("|", end='')
        for j in range(len(grille)):
            if grille[i][j] == " ":
                print(" ", end ='|')
            elif grille[i][j] == "O":
                print("O", end = '|')
            else:
                print("X", end ='|')
        print()


def erreur (continu):
    continu = input("Veuillez rentrez uniquement O pour oui et N pour non:") 
    return continu


def erreur_taille_grille(taille):
     taille =int(demander_un_entier("Veuillez rentrez une valeur suppérieur ou égale à 3:")) 
     return taille
     


def erreur_taille(taille):
    taille = int(demander_un_entier("Veuillez rentrez une valeur suppérieur à 0 mais qui se trouve dans la grille:")) 
    return taille


def tour (joueur):
    if joueur == "X":
        joueur = "O"
        return joueur
    else:
        joueur = "X"
        return joueur


def joueur_actuel(joueur):
    print("C'est au joueur",joueur,"de jouer !")


def vainqueur (joueur_en_cours, grille,taille_grille,ligne,colonne):
    if verif_ligne(grille, ligne,joueur_en_cours, taille_grille):
        return True
    elif verif_colonne (grille, colonne,joueur_en_cours, taille_grille):
        return True
    elif verif_diago_un (grille,joueur_en_cours, taille_grille):
        return True
    elif verif_diago_deux (grille,joueur_en_cours, taille_grille):
        return True
    else:
        return False


def verif_ligne(grille, ligne,joueur_en_cours, taille_grille):
    for i in range (taille_grille):
        if grille[ligne][i] != joueur_en_cours:
            return False
    return True


def verif_colonne (grille, colonne,joueur_en_cours, taille_grille):
    for i in range (taille_grille):
        if grille[i][colonne] != joueur_en_cours:
            return False
    return True


def verif_diago_un (grille,joueur_en_cours, taille_grille):
    for i in range (taille_grille):
        if grille[i][i] != joueur_en_cours:
            return False
    return True


def verif_diago_deux (grille,joueur_en_cours, taille_grille):
    for i in range (taille_grille):
        if grille[i][taille_grille-1-i] != joueur_en_cours:
            return False
    return True


def verif_des_entiers(chaine_de_caractere):
    compteur = 0
    espace_debut = True
    signe_debut = True
    chiffre_trouve = False
    espace_fin = False
    while (compteur < len(chaine_de_caractere)):
        if chaine_de_caractere[compteur] == ' ' and espace_debut:
            compteur = compteur + 1
        elif chaine_de_caractere[compteur] =='+' or chaine_de_caractere[compteur] =='-' and signe_debut:
            espace_debut = False   
            compteur = compteur + 1
            signe_debut = False
        elif chaine_de_caractere[compteur] >= '0' and chaine_de_caractere[compteur] <= '9' and not espace_fin:
            espace_debut = False
            signe_debut = False  
            chiffre_trouve = True
            compteur = compteur + 1
        elif chiffre_trouve and chaine_de_caractere[compteur] == ' ':
            espace_fin = True
            compteur = compteur + 1
        else: 
            return False
    return True


def demander_un_entier(test):
    rep = "chaine de caractere qui n'est pas un entier"    
    while not verif_des_entiers (rep):
        print ("Entrez uniquement un entier")
        rep = input(test)
    return rep

    
'''
#grille = int(input("Quel est la valeur de la grille ?"))
taille = 3
grille = crée_grille(taille)
print("La taille de la grille est de :",taille_cote(grille))
print ("grille : ", grille)
print ("case :",verif(grille,2,1))
print("la nouvelle grille est :",écrire(grille,1,1,"O"))
print("la grille une fois effacer :",effacer(grille,1,1))
test = [[' ','X',' '], [' ','O','X'], ['O',' ','X']]
print("fonction est :", est(test, 1,1,"O"))
print(affiche(test))
'''
'''
grille_graphique = GraphicalGrid.write(0,1,'X')
grille_graphique = GraphicalGrid.write(3,4,'O')
grille_graphique = GraphicalGrid.write(0,0,'O')
grille_graphique = GraphicalGrid.erase(3,4)
grille_graphique.wait_quit()
'''

joueur = "X"
taille_grille = int(demander_un_entier("Quel est la valeur de la grille ?"))
while (taille_grille < 3):
    taille_grille = erreur_taille_grille(taille_grille)

grille = crée_grille(taille_grille)

grille_graphique = GraphicalGrid(taille_grille)

continuer_la_partie = True
compteur_de_tour = 0
historique = []

while(continuer_la_partie):
    continu = input("La partie dois continuer ?")
    while (continu != "O" and continu != "N" ): 
        continu = erreur(continu)
    if continu == 'N':
        continuer_la_partie = False
    else:

        joueur_actuel(joueur)


        ligne_str = demander_un_entier("Entrez la valeur de la ligne ?")
        if ligne_str != "":
            ligne = int(ligne_str)
            while (ligne < 0 or ligne > taille_grille-1):
                ligne = erreur_taille(ligne)

            colonne_str = demander_un_entier("Entrez la valeur de la colonne ?")
            if colonne_str != "":
                colonne = int(colonne_str)
                while (colonne < 0 or colonne > taille_grille-1):
                    colonne = erreur_taille(colonne)

                while (grille[ligne][colonne] == 'O' or grille[ligne][colonne] == 'X'):
                    print("La case n'est pas vide ! Saisir à nouveau les valeur")

                    ligne = int(demander_un_entier("Entrez la valeur de la ligne ?"))
                    while (ligne < 0 or ligne > taille_grille-1):
                        ligne = erreur_taille(ligne)

                    colonne = int(demander_un_entier("Entrez la valeur de la colonne ?"))
                    while (colonne < 0 or colonne > taille_grille-1):
                        colonne = erreur_taille(colonne)

                grille = ecrire(grille, ligne, colonne, joueur)
                grille_graphique.write(ligne,colonne,joueur)

                compteur_de_tour = compteur_de_tour + 1
                
                historique.append((joueur,ligne,colonne))

                affiche(grille)

                if vainqueur(joueur,grille,taille_grille,ligne,colonne):
                    print ("Le joueur,",joueur," à gagnné !!")
                    continuer_la_partie = False
                elif compteur_de_tour == taille_grille*taille_grille:
                    print("égalité, fin de la partie !")
                    continuer_la_partie = False

                joueur=tour(joueur)


print ("Historique de la partie",historique)


grille_graphique.wait_quit()
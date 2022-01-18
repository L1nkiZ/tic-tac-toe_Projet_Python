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
        grille[i][j] = [symbole]
    else:
        print ("La case est occupé !")
    return grille
    

def effacer (grille, i, j):
    if i > len(grille):
        print("La valeur de i est trop grande !")
    elif j > len(grille):
        print("La valeur de j est trop grande !")
    else:
        grille [i][j] = (' ')
    return grille


def est (grille, i, j, symbole):
    if i > len(grille):
        print("La valeur de i est trop grande !")
    elif j > len(grille):
        print("La valeur de j est trop grande !")
    else:
        if grille[i][j] == symbole:
            return True
        else:
            return False


def affiche (grille):
    for i in range(len(grille)):
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
     taille =int(input("Veuillez rentrez une valeur suppérieur ou égale à 3:")) 
     return taille
     


def erreur_taille(taille):
    taille = int(input("Veuillez rentrez une valeur suppérieur à 0 mais qui se trouve dans la grille:")) 
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

#def gagner test la ligne ou test colonne ou test diago si lettre pareil pour gagant 
    
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
taille_grille = int(input("Quel est la valeur de la grille ?"))
while (taille_grille < 3):
    taille_grille = erreur_taille_grille(taille_grille)

grille = crée_grille(taille_grille)

grille_graphique = GraphicalGrid(taille_grille)

continuer_la_partie = True

while(continuer_la_partie):
    continu = input("La partie dois continuer ?")
    while (continu != "O" and continu != "N" ): #if non break while après
        continu = erreur(continu)
    if continu == 'N':
        continuer_la_partie = False
    else:
        grille = [[' ','X',' '], [' ','O','X'], ['O',' ','X']]

        joueur_actuel(joueur)


        ligne = int(input("Entrez la valeur de la ligne ?"))
        while (ligne < 0 or ligne > taille_grille-1):
            ligne = erreur_taille(ligne)

        colonne = int(input("Entrez la valeur de la colonne ?"))
        while (colonne < 0 or colonne > taille_grille-1):
            colonne = erreur_taille(colonne)

        affiche(grille)
        while (grille[ligne][colonne] == 'O' or grille[ligne][colonne] == 'X'):
            print("La case n'est pas vide ! Saisir à nouveau les valeur")

            ligne = int(input("Entrez la valeur de la ligne ?"))
            while (ligne < 0 or ligne > taille_grille-1):
                ligne = erreur_taille(ligne)

            colonne = int(input("Entrez la valeur de la colonne ?"))
            while (colonne < 0 or colonne > taille_grille-1):
                colonne = erreur_taille(colonne)

        grille = ecrire(grille, ligne, colonne, joueur)
        grille_graphique.write(ligne,colonne,joueur)

        affiche(grille)


        grille_graphique.wait_quit()
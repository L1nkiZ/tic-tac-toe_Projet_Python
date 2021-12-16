

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

########################################################################################################################

def taille_cote(grille):
    n = len(grille)
    return n

########################################################################################################################

def verif (grille, i, j):
    #test = plateau[i][j] 
    if grille[i][j] == (' '):
        return True
    else:
        return False

########################################################################################################################        

def écrire(grille, i, j, symbole):
    if symbole != 'O' and symbole != 'X':
        print("Le symbole n'est pas bon")
    elif grille[i][j] == (' '):
        grille[i][j] = [symbole]
    else:
        print ("La case est occupé !")
    return  grille

########################################################################################################################    

def effacer (grille, i, j):
    if i > len(grille):
        print("La valeur de i est trop grande !")
    elif j > len(grille):
        print("La valeur de j est trop grande !")
    else:
        grille [i][j] = (' ')
    return grille

########################################################################################################################

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

########################################################################################################################

def affiche (grille):
    for i in range(len(grille)):
        for j in range(len(grille)):
            print (" ", end ='|')
        print()

########################################################################################################################

#grille = int(input("Quel est la valeur de la grille ?"))
taille = 3
grille = crée_grille(taille)
print("La taille de la grille est de :",taille_cote(grille))
print ("grille : ", grille)
print ("case :",verif(grille,2,1))
print("la nouvelle grille est :",écrire(grille,1,1,"O"))
print("la grille une fois effacer :",effacer(grille,1,1))
test = [[' ',' ',' '], [' ','O',' ']]
print("fonction est :", est(test, 1,1,"O"))
print(affiche(grille))


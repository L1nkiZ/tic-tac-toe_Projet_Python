def cree_grille (n):
    ligne = []
    for i in range (n):
        ligne.append("")
    return ligne

########################################################################################################################

def taille_cote(grille):
    cote = len(cree_grille(taille_cote))
    return cote

########################################################################################################################

def est_vide(plateau, i, j):
    return plateau[i][j]

########################################################################################################################

def affichage(plateau):
    for i in range(len(plateau)):
        for j in range(len(plateau[i])):
            if est_vide(plateau, i, j):
                print(" ", end='')
            elif ([i], [j]) == "X": 
                print ("X", end='')
            elif ([i], [j]) ==  "O": 
                print ("O", end='')
            else:
                print("", end='')
        print()

########################################################################################################################

print(affichage(5))

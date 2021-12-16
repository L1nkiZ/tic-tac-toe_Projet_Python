def cree_grille (plateau, nombre_colonne):
    plateau = []
    plateau.append(taille_du_jeu(nombre_colonne))
    for i in range (nombre_colonne):
        plateau.append(taille_du_jeu(nombre_colonne))
    return plateau

########################################################################################################################


########################################################################################################################
def taille_du_jeu(grille):
    cote = len(cree_grille(taille_du_jeu))
    return cote

########################################################################################################################

def est_vide(plateau, i, j):
    return plateau[i][j]

########################################################################################################################

print(cree_grille([1],3))
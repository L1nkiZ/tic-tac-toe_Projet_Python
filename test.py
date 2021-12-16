def ligne_pleine(nbre_colonnes):
    # ligne = [False] * nbre_colonnes
    ligne = []
    for i in range(nbre_colonnes):                  
        ligne.append(False)
    return ligne

def ligne_vide(nbre_colonnes):
    ligne = [False]
    for i in range(nbre_colonnes-2):
        ligne.append(True)
    ligne.append(False)
    return ligne


def init(nbre_lignes, nbre_colonnes):
    labyrinthe = []

    labyrinthe.append(ligne_pleine(nbre_colonnes))
    for i in range(nbre_lignes-2):
        labyrinthe.append(ligne_vide(nbre_colonnes))
    labyrinthe.append(ligne_pleine(nbre_colonnes))

    return labyrinthe

def générer_labyrinthe(nbre_lignes, nbre_colonnes, nbre_ilots):
    labyrinthe = init(nbre_lignes, nbre_colonnes)
    place_ilots(labyrinthe, nbre_ilots)

    cases_possibles = cases_constructibles(labyrinthe)
    while len(cases_possibles) != 0:
        indice = randint(0, len(cases_possibles)-1)
        #ligne, colonne = cases_possibles[indice][0], cases_possibles[indice][1]
        ligne, colonne = cases_possibles[indice]
        labyrinthe[ligne][colonne] = False
        cases_possibles = cases_constructibles(labyrinthe) 


print(affichage(5))    
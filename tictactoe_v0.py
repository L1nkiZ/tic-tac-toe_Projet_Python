#import randint

def cree_grille (n):
    ligne = []
    for i in range (n):
        ligne.append("")
    return ligne
############################################################

def ligne_de_jeu(dimension):
    ligne = [] 
    for i in range (dimension):
        ligne.append (" ")
        ligne.append("+")
    return ligne

############################################################

def ligne_de_contour(dimension):
    ligne = []
    for i in range (dimension * 2):
        ligne.append("+")
    return ligne

############################################################

def plateau_de_jeu (dimension):
    plateau = []

    plateau.append(ligne_de_contour(dimension))
    for i in range (dimension - 2):    
        plateau.append(ligne_de_jeu(dimension))
        plateau.append(ligne_de_contour(dimension))
    plateau.append(ligne_de_contour(dimension))
    return plateau

############################################################

#def affichage(plateau):
 #   for i in range(len(plateau)):
  #      for j in range (plateau[i]):
            

   #     print()

############################################################

print (plateau_de_jeu(4))



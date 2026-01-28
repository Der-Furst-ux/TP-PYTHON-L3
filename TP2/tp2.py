# fonction qui calcule la moyenne d'une liste de notes
def calcul_moy(liste_notes):
    return sum(liste_notes)/len(liste_notes)

# fonction qui retourne la mention en fonction de la moyenne
def mention(moy):
    if moy<10:
        return "ajourné"
    elif moy<12 :
         return "passable"
    elif moy<16 :
        return "bien"
    else:
        return "tres bien"
# les listes de notes
notes1 = [18, 0, 3, 4,  17, 20, 20, 15]
notes2 = [11, 15, 16, 14, 17, 20, 20, 17]
notes3 = [1, 6, 18, 6, 1, 2, 0, 12]

# affichage des moyennes et des mentionsgit
print(calcul_moy(notes1), mention(calcul_moy(notes1)))
print(calcul_moy(notes2), mention(calcul_moy(notes2)))
print(calcul_moy(notes3), mention(calcul_moy(notes3)))

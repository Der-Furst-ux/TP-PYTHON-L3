try:
#demander les nombres à l'utilisateur
    num = float(input("Entrez le numérateur : "))
    den = float(input("Entrez le dénominateur : "))

#calcul de la division
    resultat = num / den
    print(f"Résultat : {resultat}")

#gestion de la division par zéro
except ZeroDivisionError:
    print("Erreur : on ne peut pas diviser par zéro !")

#gestion de saisie qui n'est pas un nombre
except ValueError:
    print("Erreur : vous devez entrer un nombre valide !")

finally:
    print("Fin du programme.")
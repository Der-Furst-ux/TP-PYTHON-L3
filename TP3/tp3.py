#liste d'étudiants stocker
etudiants = [
    {"nom": "Serge", "age": 21, "moyenne": 17.49},
    {"nom": "Teddy", "age": 20, "moyenne": 9.99},
    {"nom": "Lamoula", "age": 21, "moyenne": 16.43},
    {"nom": "innocent", "age": 21, "moyenne": 12.33},
    {"nom": "kpi", "age": 21, "moyenne": 11.03},
    {"nom": "Hermann", "age": 24, "moyenne": 6.92},
    {"nom": "anake", "age": 25, "moyenne": 7.27}

]

#afficher les étudiants admis
print("Étudiants admis :")
for etudiant in etudiants:
    if etudiant["moyenne"] >= 10:
        print(etudiant["nom"], " ", etudiant["moyenne"])

print("Étudiants ajourné :")
for etudiant in etudiants:
    if etudiant["moyenne"] < 10:
        print(etudiant["nom"], " ", etudiant["moyenne"])        

#Calculer la moyenne générale de la classe
total = 0
for etudiant in etudiants:
    total += etudiant["moyenne"]
moyenne_generale = total / len(etudiants)
print("Moyenne générale de la classe :", moyenne_generale)
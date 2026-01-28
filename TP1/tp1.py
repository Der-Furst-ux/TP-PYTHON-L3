# emande a utilisateur de saisir nom et age
nom = input("entrez votre nom:")
age = int(input("entrez votre age:"))


#afficher s'il est mineur ou majeur
if age >= 18:
    print("vous etes majeur")
else:
    print("vous etes mineur")


#afficher tous les nombres pairs de 1 a 100
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
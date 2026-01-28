#demander une phrase à l'utilisateur
phrase = input("Écrivez une phrase : ")

#comptage du nombre de mots
mots = phrase.split()
print("Nombre de mots :", len(mots))

#trouver le mot le plus long
mot_plus_long = ""
for mot in mots:
    if len(mot) > len(mot_plus_long):
        mot_plus_long = mot
print("Mot le plus long :", mot_plus_long)

#vérifier si la phrase est un palindrome(se lit de la même manière dans les deux sens)
phrase_sans_espace = phrase.replace(" ", "").lower()
if phrase_sans_espace == phrase_sans_espace[::-1]:    
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
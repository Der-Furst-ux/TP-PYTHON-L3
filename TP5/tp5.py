
try:

#création du fichier notes.txt avec des notes
    with open("notes.txt", "w") as f:
        f.write("12\n15\n8\n10\n14\n")  # chaque note sur une ligne

#licture du fichier et calculer de la moyenne
    total = 0
    count = 0

    with open("notes.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line:  # ignorer les lignes vides
                note = int(line)
                total += note
                count += 1

    if count == 0:
        print("Le fichier est vide, impossible de calculer la moyenne.")
    else:
        moyenne = total / count
        print(f"La moyenne est : {moyenne}")

#résultat dans un fichier resultat.txt
        with open("resultat.txt", "w") as f:
            f.write(f"Moyenne de la classe : {moyenne}\n")

except FileNotFoundError:
    print("Erreur : le fichier notes.txt n'existe pas !")
except ValueError:
    print("Erreur : le fichier contient des valeurs non numériques !")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
finally:
    print("Programme terminé.")
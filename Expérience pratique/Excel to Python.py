import matplotlib.pyplot as plt

file = open("donne.txt", "r")
data = file.readlines()

T = []
X_sans_TMD = []
X_avec_TMD = []

for e in data:
    L = e.split(";")

    T.append(int(L[0]))
    X_sans_TMD.append(int(L[1]))
    X_avec_TMD.append(int(L[2].strip()))

#Vérification que toutes les données sont correctes
print("Valeurs de temps")
print(T)
print("Valeurs sans TMD")
print(X_sans_TMD)
print("Valeurs avec TMD")
print(X_avec_TMD)

#Affichage
plt.plot(T, X_sans_TMD)
plt.plot(T, X_avec_TMD)

plt.legend(["Sans TMD", "Avec TMD"])
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)") #Vérifier l'unité et être sûr que c'est bien des courbes de position

plt.show()

#Format du .txt:
#0;1;2   #Premiere nomnbre = instant t, deuxieme = position sans TMD à l'instant t, troisième = position avec TMD à l'instant t
#2;3;4   
#3;4;5   
#...

#Fais attention à part faire un saut de ligne après la troisième ligne, sinon ça va buguer
#Le fichier .txt doit être dans le même dossier que le .py et être renommé "donne.txt"

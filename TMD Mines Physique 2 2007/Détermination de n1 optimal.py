import math as m
import matplotlib.pyplot as plt
import numpy as np

a = 0.1
n = 0.3
b = 1/m.sqrt(1+a)

def G2(z, n):
    global a, b
    c = z**2 + (z**2)*a - 1
    module_numerateur = m.sqrt((-z**4+(b*z)**2)**2 + (2*n*b*z**2)**2)
    module_denominateur = m.sqrt((-(z**2)*c+(b**2)*c+a*z**4)**2 + (2*n*b*c)**2)
    return module_numerateur/module_denominateur

def difference_max(L): #En réalisant l'approximation que la valeur de n1 opt est celle pour laquelle la difference entre les deux maximums est le plus faible
    L1 = []
    L2 = []
    for i in range(500):
        L1.append(L[i])
    for i in range(501, 999):
        L2.append(L[i])
    L1.sort()
    L2.sort()
    return abs(L1[len(L1)-1] - L2[len(L2) - 1])


z = np.linspace(0.80, 1.2, 1000)

valeurs_n1 = np.linspace(0.18, 0.21, 500) #Compléter ici les valeurs à tester
liste_difference_max = []

for n1 in valeurs_n1:
    G_2 = []
    for elt in z:
        G_2.append(G2(elt, n1))
    liste_difference_max.append(difference_max(G_2))

print(min(liste_difference_max), liste_difference_max.index(min(liste_difference_max)), valeurs_n1[liste_difference_max.index(min(liste_difference_max))])

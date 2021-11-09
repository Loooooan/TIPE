import numpy as np  # Bibliothèque utilisée pour le calcul
import pylab as pl  # Bibliothèque utilisée pour les affichages

# Bibliothèque pour résoudre les
# équations différentielles ordinaires (EDO)
from scipy.integrate import odeint

# <----- Mise en données ----->

m1 = 264000000.  # Masse équivalente du batiment
k1 = 225000000.  # Raideur du batiment
x0 = 0.25  # Sollicitation initiale
temps1 = 240  # Temps maximum d'étude
nbpt = 200000  # Nombre de points pour discrétiser le temps
m2 = 660000
k2 = 510000
f = 52000

# <----- Ecriture de la dérivée ----->

def dx(x, t):
    # Fonction qui calcule la dérivée et la dérivée seconde
    # dans la ligne i de la matrice x on stocke le déplacement
    # de la tour, celui de l'amortisseur et leurs 2 dérivées.
    x1 = x[0]  # déplacement de la tour
    x2 = x[1]  # déplacement de l'amortisseur
    dx1 = x[2]  # vitesse de la tour
    dx2 = x[3]  # vitesse de l'amortisseur

    # On les stocke dans un plus petit vecteur pour plus de clarté (optionnel)
    X1 = np.array([x1, x2, dx1, dx2])
    # Ecriture de la matrice
    K = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [-(k1 + k2) / m1, k2 / m1, 0, 0], [k2 / m2, -k2 / m2, f / m2, -f / m2]])
    # Calcul du terme suivant (produit matriciel np.dot)
    dX1 = np.dot(K, X1)
    # Récupération des dérivées et des dérivées secondes
    dx1 = dX1[0]
    dx2 = dX1[1]
    ddx1 = dX1[2]
    ddx2 = dX1[3]
    return [dx1, dx2, ddx1, ddx2]


    # <----- Résolution ----->

# Découpage de l'intervalle avec un pas de temps régulier
t = np.linspace(0, temps1, nbpt)

# Résolution avec euler explicite

temps = 240

# découpage de l'intervalle avec un pas de temps régulier
t_pas1 = np.linspace(0, temps, nbpt)

# Avec euler explicite
x_pas1 = np.zeros((nbpt, 4))
x_pas1[0, 0] = x0

for i in range(len(t_pas1) - 1):
    x_pas1[i + 1, :] = x_pas1[i, :] + pl.dot(dx(x_pas1[i, :], t_pas1[i]), t_pas1[i + 1] - t_pas1[i])

pl.plot(t_pas1, x_pas1[:, 1], label="Déplacement du bâtiment")
pl.plot(t_pas1, x_pas1[:, 2], label="Déplacement de l'amortisseur")
pl.legend()

pl.show()




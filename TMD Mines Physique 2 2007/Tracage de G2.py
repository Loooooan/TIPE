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

z = np.linspace(0, 1.4, 1000)

valeurs_n1 = [0.1, 0.3, 0.6] #Compléter ici les valeurs à tester

for n1 in valeurs_n1:
    G_2 = []
    for elt in z:
        G_2.append(G2(elt, n1))
    plt.plot(z, G_2)

plt.legend((valeurs_n1))

plt.show()

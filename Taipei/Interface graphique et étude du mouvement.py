# -*- coding: utf-8 -*-

# <----- Importation des bibliothèques ----->

import numpy as np #Bibliothèque utilisée pour le calcul
import pylab as pl #Bibliothèque utilisée pour les affichages
from tkinter import *

# Bibliothèque pour résoudre les
# équations différentielles ordinaires (EDO) 
from scipy.integrate import odeint 

## Creer l'interface graphique en copiant/collant ici le fichier  InterfaceTaipei 



# <----- Créations des différents objets ----->
class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=360, height=500, **kwargs)

        # Données initiales
        g = 9.82
        self.m2 = 660000
        self.visco = 52000
        self.m1 = 264000000
        self.k1 = 225000000
        self.x0 = 0.5
        self.k2 = 510000
        self.nbpt1 = 50000
        self.nbpt2 = 10000
        self.nbpt3 = 5000

        self.pack()
        # taille de la fenetre
        fenetre.geometry('360x500')
        self.update()

        # Création du champs m1
        # Afichage d'un texte

        # On crée un Label, c'est-à-dire un objet graphique affichant du texte
        self.message = Label(self, text="Masse de la tour (m1) :")
        # On place le texte
        self.message.place(bordermode=OUTSIDE, height=20, width=200, x=10, y=30)
        # Création du champs
        self.m1_entry = Entry(self, textvariable=self.m1, width=30)
        # On place le champs
        self.m1_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=30)
        # On lui donne sa valeur initiale
        self.m1_entry.insert(0, self.m1)

        # Création du champs k1
        self.message = Label(self, text="Amortisseur de la tour (k1) :")
        self.message.place(bordermode=OUTSIDE, height=20, width=200, x=10, y=70)
        self.k1_entry = Entry(self, textvariable=self.k1, width=30)
        self.k1_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=70)
        self.k1_entry.insert(0, self.k1)

        # Création du champs x0
        self.message = Label(self, text="Solicitation de départ (x0) :")
        self.message.place(bordermode=OUTSIDE, height=20, width=200, x=10, y=110)
        self.x0_entry = Entry(self, textvariable=self.x0, width=30)
        self.x0_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=110)
        self.x0_entry.insert(0, self.x0)

        # Création du champs m2
        self.message = Label(self, text="Masse de l'amortisseur (m2) :")
        self.message.place(bordermode=OUTSIDE, height=20, width=200, x=10, y=150)
        self.m2_entry = Entry(self, textvariable=self.m2, width=30)
        self.m2_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=150)
        self.m2_entry.insert(0, self.m2)

        # Création du champs k2
        self.message = Label(self, text="Raideur de l'amortisseur (k2) :")
        self.message.place(bordermode=OUTSIDE, height=20, width=200, x=10, y=190)
        self.k2_entry = Entry(self, textvariable=self.k2, width=30)
        self.k2_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=190)
        self.k2_entry.insert(0, self.k2)

        # Création du champs f
        self.message = Label(self, text="Viscosité de l'amortisseur (v):")
        self.message.place(bordermode=OUTSIDE, height=20, width=200, x=10, y=230)
        self.visco_entry = Entry(self, textvariable=self.visco, width=30)
        self.visco_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=230)
        self.visco_entry.insert(0, self.visco)

        # Création du champs nbpt1
        self.message = Label(self, text="Nombre de points utilisés pour \n  la simulation 1 (avec animation) :")
        self.message.place(bordermode=OUTSIDE, height=25, width=200, x=10, y=270)
        self.nbpt1_entry = Entry(self, textvariable=self.nbpt1, width=30)
        self.nbpt1_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=270)
        self.nbpt1_entry.insert(0, self.nbpt1)

        # Création du champs nbpt2
        self.message = Label(self, text="Nombre de points utilisés pour \n la simulation 2 (en bleu):")
        self.message.place(bordermode=OUTSIDE, height=25, width=200, x=10, y=310)
        self.nbpt2_entry = Entry(self, textvariable=self.nbpt2, width=30)
        self.nbpt2_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=310)
        self.nbpt2_entry.insert(0, self.nbpt2)

        # Création du champs nbpt3
        self.message = Label(self, text="Nombre de points utilisés pour \n la simulation 3 (en vert) :")
        self.message.place(bordermode=OUTSIDE, height=25, width=200, x=10, y=350)
        self.nbpt3_entry = Entry(self, textvariable=self.nbpt3, width=30)
        self.nbpt3_entry.place(bordermode=OUTSIDE, height=20, width=100, x=220, y=350)
        self.nbpt3_entry.insert(0, self.nbpt3)

        # Création de l'affichage des valeurs
        self.message2 = Label(self, text="Valeurs:")
        self.message2.place(bordermode=OUTSIDE, height=30, x=10, y=390)

        # Création du bouton d'enregistrement des valeurs
        # définition du bouton et de l'action associée
        self.bouton_enregistrer = Button(self, text="Modifier", fg="black", command=self.modifier)
        # position du bouton
        self.bouton_enregistrer.place(bordermode=OUTSIDE, height=20, width=100, x=120, y=430)

        # Création du bouton de lancement de la simulation
        self.bouton_quitter = Button(self, text="Valider", command=self.quit)
        self.bouton_quitter.place(bordermode=OUTSIDE, height=20, width=100, x=240, y=430)

    def modifier(self):
        # si on clique sur modifier on recupere les valeurs de chaque champs
        self.m1 = self.m1_entry.get()
        self.k1 = self.k1_entry.get()
        self.x0 = self.x0_entry.get()
        self.m2 = self.m2_entry.get()
        self.k2 = self.k2_entry.get()
        self.visco = self.visco_entry.get()
        self.nbpt1 = self.nbpt1_entry.get()
        self.nbpt2 = self.nbpt2_entry.get()
        self.nbpt3 = self.nbpt3_entry.get()
        # On met alors a jour le texte donnant les valeurs enregistrées
        self.message2[
            'text'] = "Valeurs: m1 = {0},k1={1},x0={2},m2={3},k2={4},visco={5},\n nbpt1={6},nbpt2={7},nbpt3={8} ".format(
            self.m1, self.k1, self.x0, self.m2, self.k2, self.visco, self.nbpt1, self.nbpt2, self.nbpt3)


## <----- Mise en données ----->

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
m1=float(interface.m1_entry.get())
k1=float(interface.k1_entry.get())
x0=float(interface.x0_entry.get())
m2=float(interface.m2_entry.get())
k2=float(interface.k2_entry.get())
f=float(interface.visco_entry.get())
nbpt1=int(interface.nbpt1_entry.get())
nbpt2=int(interface.nbpt2_entry.get())
nbpt3=int(interface.nbpt3_entry.get())
fenetre.destroy()

temps=240 #temps maximum	(champs non créer dans l'interface)

# <----- Ecriture de la dérivée ----->

def dx(x,t):
    #fonction qui calcule la dérivée et la dérivée seconde
    # dans la ligne i de la matrice x on stocke le déplacement
    # de la tour, celui de l'amortisseur et leurs 2 dérivées.
   
    #x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    x1= x[0]        # déplacement de la tour
    x2= x[1]        # déplacement de l'amortisseur
    dx1= x[2]       # vitesse de la tour
    dx2= x[3]       # vitesse de l'amortisseur
    
    #on les stocke dans un plus petit vecteur pour plus de clarté (optionnel)
    X1=np.array([x1,x2,dx1,dx2])
  
    # écriture de la matrice
    A=np.array([[0,0,1,0],[0,0,0,1],[-(k1+k2)/m1,k2/m1,0,0],[k2/m2,-k2/m2,f/m2,-f/m2]])    
    
    #calcul du terme suivant
    #produit matriciel np.dot
    dX1=np.dot(A,X1)
    #on récupère les dérivées et les dérivées secondes
    dx1 = dX1[0]
    dx2 = dX1[1]
    ddx1 = dX1[2]
    ddx2 = dX1[3]
    return [dx1, dx2, ddx1, ddx2]
    

# <----- Résolution avec le pas 1 ----->

#nombre de points
nbpt=nbpt1  

#découpage de l'intervalle avec un pas de temps régulier
t_pas1 = np.linspace(0, temps, nbpt)

# Avec euler explicite
x_pas1=np.zeros((nbpt,4))
x_pas1[0,0]=x0

for i in range(len(t_pas1)-1):
    x_pas1[i+1,:]=x_pas1[i,:]+pl.dot(dx(x_pas1[i,:],t_pas1[i]),t_pas1[i+1]-t_pas1[i])
    
# <----- Résolution avec le pas 2 ----->

nbpt=nbpt2  
t_pas2 = np.linspace(0, temps, nbpt)
x_pas2=np.zeros((nbpt,4))
x_pas2[0,0]=x0

for i in range(len(t_pas2)-1):
    x_pas2[i+1,:]=x_pas2[i,:]+pl.dot(dx(x_pas2[i,:],t_pas2[i]),t_pas2[i+1]-t_pas2[i])


# <----- Résolution avec le pas 3 ----->
nbpt=nbpt3
t_pas3 = np.linspace(0, temps, nbpt)
x_pas3=np.zeros((nbpt,4))
x_pas3[0,0]=x0

for i in range(len(t_pas3)-1):
    x_pas3[i+1,:]=x_pas3[i,:]+pl.dot(dx(x_pas3[i,:],t_pas3[i]),t_pas3[i+1]-t_pas3[i])

# <-----  Affichage des résultats ----->

# affichage des positions en fonction du temps
fig, axes = pl.subplots(1,3, figsize=(12,4))

axes[0].plot(t_pas1, x_pas1[:, 0], 'b', label="Pas 1")
axes[0].plot(t_pas2, x_pas2[:, 0], 'g', label="Pas 2")
axes[0].plot(t_pas3, x_pas3[:, 0], 'y', label="Pas 3")

pl.xlabel('x')

axes[1].plot(t_pas1, x_pas1[:, 1], 'b', label="Pas 1")
axes[1].plot(t_pas2, x_pas2[:, 1], 'g', label="Pas 2")
axes[1].plot(t_pas3, x_pas3[:, 1], 'y', label="Pas 3")
pl.suptitle(u'Position de la masse et de l\'amortisseur en fonction du temps')  


## <----- Animation ----->
                 
 
pl.interactive(True)                      

#On définit le dessin de départ 
#4 points reliées par 3 traits
x = np.array([0,0,40,40])  
y = np.array([0,508,508,0])
x1 = np.array([17,17,23,23])  
y1 = np.array([508,480,480,508])

#Création du cercle
b = np.linspace(0, 2*np.pi, 40)
Rayon=3
xb = 20+Rayon*np.cos(b)
yb = 480+Rayon*np.sin(b)
cecrle,= pl.plot(xb, yb,'-b')

#Pour que les proportions soient respectées
pl.axis('equal')
#taille de la fenêtre
pl.axis([-10,50,0,550])  
line, = pl.plot(x,y,'-g')
line2, =pl.plot(x1,y1,'-b') 

pl.xlabel('x')           
                                      
# on fait varier les positions en fonction du temps
for j in range(len(t_pas1)//200-1):
    i=j*100 #pour diminuer le nombre d'affichage (pas un affichage tous les pas de calcul)                            
    #On définit les nouvelles positions à partir des calculs précédents    
    x = np.array([0,x_pas1[i,0],40+x_pas1[i,0],40])
    x1 = np.array([20-Rayon+x_pas1[i,0],20-Rayon+x_pas1[i,1],20+Rayon+x_pas1[i,1],20+Rayon+x_pas1[i,0]])      
    xb = 20+Rayon*np.cos(b)+x_pas1[i,1]    
    #On met à jour les positions                                                
    line.set_xdata(x)
    line2.set_xdata(x1) 
    cecrle.set_xdata(xb)            
    pl.draw()                      

    xx = pl.waitforbuttonpress(timeout=0.01) #petite astuce pour que ça fonctionne sous windows
             
 
xx = pl.waitforbuttonpress(timeout=10.)

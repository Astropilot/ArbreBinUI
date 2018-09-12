# -*- coding: utf-8 -*-

import os, sys

import Tkinter as tk
import tkFont

from saisie import *

"""
********************************************************
*													   *
*			Créé par Yohann MARTIN, 2017/2018		   *
*				DUT Informatique de Vélizy			   *
*													   *
********************************************************
"""

# La taille d'un noeud (cercle) en pixels
TAILLE_NOEUD = 30

# Le nombre de pixels de décalage entre un noeud et ses fils
DIMI_OFFSET = 50

FONT = None

# Permet de calculer la hauteur d'un arbre binaire
def calcul_hauteur_arbre(a):
	if(a == None):
		return -1
	else:
		h_g = calcul_hauteur_arbre(a.G)
		h_d = calcul_hauteur_arbre(a.D)
		return 1 + max(h_g, h_d)

# Retourne le nombre de noeuds pour un niveau donné dans un arbre binaire complet
def calcul_nb_noeud_niveau(k):
	return (2**(k-1))

# Permet d'obtenir le pixel sur l'axe X qui est au centre d'un noeud
def get_center_noeud(noeud_debut, noeud_largeur, text_size):
	return noeud_debut + ((noeud_largeur - noeud_debut - text_size) / 2)

# Permet de calculer l'indice de l'axe X pour un noeud d'un niveau
def calcul_indiceX(i, niveau):
	return float((2. * i + 1.) / (2.**niveau))

# Permet de calculer les indices des coins haut/gauche et bas/droit pour un noeud
def calcul_indice(indice, indiceX, niveau):
	return [indice[0] * indiceX - (TAILLE_NOEUD / 2), (indice[1] * niveau) + DIMI_OFFSET * niveau, indice[0] * indiceX + (TAILLE_NOEUD / 2), (indice[1] * niveau) + TAILLE_NOEUD + (DIMI_OFFSET * niveau)]

# Permet de dessiner l'arbre à partir d'un parcours en profondeur (récursivité)
def dessiner(canvas, a, indice, niveau, i):
	if(a != None):
		global FONT
		# La longueur & largeur du texte va nous permettre de centrer la valeur du noeud
		(textWidth, textHeight) = (FONT.measure(a.val),FONT.metrics("linespace"))

		# On calcul l'indice pixel sur l'axe X du noeud courant
		IndiceX = calcul_indiceX(i, niveau)

		# On calcul le reste des indices du noeud
		calculIndice = calcul_indice(indice, IndiceX, niveau)

		# On dessine le cercle aux indices donnés
		canvas.create_oval(calculIndice[0], calculIndice[1], calculIndice[2], calculIndice[3], outline ='black')
		# Puis on dessine le texte au milieu
		canvas.create_text(get_center_noeud(calculIndice[0], calculIndice[2], textWidth), get_center_noeud(calculIndice[1], calculIndice[3], textHeight), text = a.val, font = FONT, fill = 'black', anchor= 'nw')

		# On dessine ensuite les enfants gauche et droite
		dessiner(canvas, a.G, indice, niveau+1, i*2)
		dessiner(canvas, a.D, indice, niveau+1, (i*2)+1)

		# Si on à un fils gauche, on calcul ses indices pour dessiner une ligne entre le noeud courant et son fils
		if(a.G != None):
			filsGIndice = calcul_indice(indice, calcul_indiceX(i*2, niveau+1), niveau+1)
			canvas.create_line(get_center_noeud(filsGIndice[0], filsGIndice[2], 0), filsGIndice[1], get_center_noeud(calculIndice[0], calculIndice[2], 0), calculIndice[3], fill = 'black')
		# De même pour le fils droit
		if(a.D != None):
			filsDIndice = calcul_indice(indice, calcul_indiceX((i*2)+1, niveau+1), niveau+1)
			canvas.create_line(get_center_noeud(filsDIndice[0], filsDIndice[2], 0), filsDIndice[1], get_center_noeud(calculIndice[0], calculIndice[2], 0), calculIndice[3], fill = 'black')

# Créer une fenêtre et dessine l'arbre dedans
def dessiner_arbre(a):
	# On créé une nouvelle fenêtre graphique
	global FONT

	root = tk.Tk()

	image_Largeur = (calcul_nb_noeud_niveau(calcul_hauteur_arbre(a) + 1) * TAILLE_NOEUD) * 2
	image_Hauteur = ((calcul_hauteur_arbre(a) + 1 + 1) * (TAILLE_NOEUD + DIMI_OFFSET))

	if(image_Largeur < 500):
		image_Largeur = 500
	if(image_Hauteur > 1000):
		image_Hauteur = 1000

	FONT = tkFont.Font(family='Arial', size=-(TAILLE_NOEUD - 10))

	canvas = tk.Canvas(root, width=image_Largeur, height=image_Hauteur)
	canvas.pack()

	# On dessine notre arbre
	dessiner(canvas, a, [image_Largeur, 20], 1, 0)

	tk.mainloop()

# Cette partie n'est exécutée que si l'on lance le script directement, et non dans les import
if __name__ == "__main__":
	# On demande à rentrer un arbre (saisie classique en console, se référer au fichier saisie.py)
	arbre = entrerArbre(1)

	dessiner_arbre(arbre)

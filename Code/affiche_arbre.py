# -*- coding: utf-8 -*-

import os

# Si Pillow n'est pas installé, alors on tente de l'installer avant
try:
	from PIL import Image
	from PIL import ImageColor
	from PIL import ImageDraw
	from PIL import ImageFont
except ImportError:
	os.system('python -m pip install pillow')

from time import gmtime, strftime
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

if(os.name == 'nt'):
	# Sous windows le path des polices est géré
	FONT = ImageFont.truetype('arial.ttf', TAILLE_NOEUD - 5)
if(os.name == 'posix'):
	# Mais sous linux il faut spécifier le chemin absolu (sur d'anciennes versions de Pillow)
	FONT = ImageFont.truetype('/usr/share/fonts/truetype/ttf-liberation/LiberationSans-Regular.ttf', TAILLE_NOEUD - 5)

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
def dessiner(draw, a, indice, niveau, i):
	if(a != None):

		# La longueur & largeur du texte va nous permettre de centrer la valeur du noeud
		textWidth, textHeight = draw.textsize(a.val, font = FONT)

		# On calcul l'indice pixel sur l'axe X du noeud courant
		IndiceX = calcul_indiceX(i, niveau)

		# On calcul le reste des indices du noeud
		calculIndice = calcul_indice(indice, IndiceX, niveau)

		# On dessine le cercle aux indices donnés
		draw.ellipse((calculIndice[0], calculIndice[1], calculIndice[2], calculIndice[3]), outline ='black')
		# Puis on dessine le texte au milieu
		draw.text((get_center_noeud(calculIndice[0], calculIndice[2], textWidth), get_center_noeud(calculIndice[1], calculIndice[3], textHeight)), a.val, font = FONT, fill = 'black')

		# On dessine ensuite les enfants gauche et droite
		dessiner(draw, a.G, indice, niveau+1, i*2)
		dessiner(draw, a.D, indice, niveau+1, (i*2)+1)

		# Si on à un fils gauche, on calcul ses indices pour dessiner une ligne entre le noeud courant et son fils
		if(a.G != None):
			filsGIndice = calcul_indice(indice, calcul_indiceX(i*2, niveau+1), niveau+1)
			draw.line((get_center_noeud(filsGIndice[0], filsGIndice[2], 0), filsGIndice[1], get_center_noeud(calculIndice[0], calculIndice[2], 0), calculIndice[3]), fill = 'black')
		# De même pour le fils droit
		if(a.D != None):
			filsDIndice = calcul_indice(indice, calcul_indiceX((i*2)+1, niveau+1), niveau+1)
			draw.line((get_center_noeud(filsDIndice[0], filsDIndice[2], 0), filsDIndice[1], get_center_noeud(calculIndice[0], calculIndice[2], 0), calculIndice[3]), fill = 'black')

# Créer une image, dessine l'arbre dedans et l'affiche
def dessiner_arbre(a, saveImage=False):
	# On créé une nouvelle image

	image_Largeur = (calcul_nb_noeud_niveau(calcul_hauteur_arbre(a) + 1) * TAILLE_NOEUD) * 2
	image_Hauteur = ((calcul_hauteur_arbre(a) + 1) * (TAILLE_NOEUD + DIMI_OFFSET)) * 2

	im = Image.new("RGB", (image_Largeur, image_Hauteur), (255,255,255))
	# On récupère la fonction de dessin
	dr = ImageDraw.Draw(im)

	# On dessine notre arbre
	dessiner(dr, a, [image_Largeur, 20], 1, 0)

	# On affiche l'image dans l'explorateur d'image par défaut
	im.show()
	if(saveImage):
		im.save("arbre_" + strftime("%Y-%m-%d_%Hh%Mm%Ss", gmtime()) + ".png","PNG")
	del im

# Cette partie n'est exécutée que si l'on lance le script directement, et non dans les import
if __name__ == "__main__":
	# On demande a rentrer un arbre (saisie classique en console, se référer au fichier saisie.py)
	arbre = entrerArbre(1)
	# On dessine et affiche notre arbre
	dessiner_arbre(arbre, True)

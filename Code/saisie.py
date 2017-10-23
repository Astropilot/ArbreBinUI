# -*- coding: utf-8 -*-

### Interface de saisie et affichage : Pierre Lartigau, automne 2016  ###

class Arbre:
	""" Implémentation des Arbres binaires ( D = droite; G = gauche)"""
	
	val = None	#valeur du noeud
	G = None		#sous arbre Gauche
	D = None		#sous arbre Droit
	
	def __init__(self, valeur, aG, aD):
		self.val = valeur
		self.G = aG
		self.D = aD
	
	def ajouterFils(self, a, cote):
		if cote == "G":
			self.G = a
		elif cote == "D":
			self.D = a

"""
Affichage d'un arbre dans la forme ci dessous:

X
├─── Fils droit de X
├─── Fils gauche de X

p est la variable qui gère l'indentation de l'affichage
"""
def afficher(a, p):
	if p == 1:
		print str(a.val)
	else:
		print "│   "*(p-2)+"├─── "+str(a.val)
	
	if a.D != None:
		afficher(a.D,p+1)
	else:
		print "│   "*(p-1)+"├─── "+"Ø"
	if a.G != None:
		afficher(a.G,p+1)
	else:
		print "│   "*(p-1)+"├─── "+"Ø"

##### Q1 #####
"""
Saisie d'un arbre par l'utilisateur:

Valeur : X
	Valeur à gauche de X :
	Valeur à droite de X : 

p est la variable qui gère l'indentation de l'affichage
"""
def entrerArbre(p):
	print "    "*(p-1),
	valeur = raw_input("Valeur : ")
	if valeur == "":
		return None
	else:
		return Arbre(valeur, entrerArbre(p+1), entrerArbre(p+1))

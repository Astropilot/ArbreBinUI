# ![PythonLogo](https://www.python.org/static/favicon.ico) ArbreBinUI

ArbreBinUI est un script python permettant l'affichage de manière graphique (librairie Tkinter) d'un arbre binaire.

Ce script fait appel à un autre script permettant la saisie en console d'un arbre binaire ainsi que sa représentation
par une classe *Arbre*. Le script [saisie.py](https://github.com/Astropilot/ArbreBinUI/blob/master/Code/saisie.py) à été développé par Pierre Lartigau en 2016.

![ScreenShot](https://github.com/Astropilot/ArbreBinUI/blob/master/Images/arbresbin.png)

# Installation et prérequis

Pour utiliser correctement ce script vous avez besoin de
*   Python 2.*
*   Tkinter (Librairie de base, elle est normalement installée avec Python)

# Utilisation

Pour tester ArbreBinUI, vous pouvez lancer directement le fichier `affiche_arbre.py` qui vous demandera 3 arbres:
```sh
$ python affiche_arbre.py
```

Pour l'utiliser dans des projets:
```python
# -*- coding: utf-8 -*-
from affiche_arbre import TreeDrawer
from saisie import *

treeDrawer = TreeDrawer() # Il est important de créer cet objet avant toute tentative de dessin

arbre = entrerArbre(1)

# Mes opérations sur l'arbre ici..

treeDrawer.dessiner_arbre(arbre) # On dessine ici notre arbre, on peut l'appeler autant que l'on veut.
# Attention cette méthode est asynchrone, si vous voulez attendre je conseil de mettre une pause comme une attente clavier !

# Éventuellement d'autres opérations..

# On attend la fermeture des fenêtres avant de quitter le programme.
# Cette méthode est obligatoire avant la fin du programme.
treeDrawer.wait()
```

# Changelog

## 2.1 ##
*   Gestion multi-fenêtre pour chaque dessin
*   Passage de la fonction de dessin de synchrone à asynchrone

## 2.0 ##
*   Changement de librairie, passage de Pillow à Tkinter
*   Amélioration de la taille de la fenêtre en fonction de la hauteur de l'arbre
*   Meilleur fonctionnement multi OS

## 1.1 ##
*   La taille de l'image est générée en fonction de la hauteur de l'arbre
*   L'image peut être sauvegardée si demandée

## 1.0 ##
*   Affichage d'arbres binaires
*   **TODO**: Générer la taille de l'image en fonction de la hauteur de l'arbre

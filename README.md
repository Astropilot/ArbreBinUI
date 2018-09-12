# ![PythonLogo](https://www.python.org/static/favicon.ico) ArbreBinUI

ArbreBinUI est un script python permettant l'affichage de manière graphique (librairie Tkinter) d'un arbre binaire

Ce script fait appel à un autre script permettant la saisie en console d'un arbre binaire ainsi que sa représentation
par une classe *Arbre*. Le script [saisie.py](https://github.com/Astropilot/ArbreBinUI/blob/master/Code/saisie.py) à été développé par Pierre Lartigau en 2016.

![ScreenShot](https://github.com/Astropilot/ArbreBinUI/blob/master/Images/arbresbin.png)

# Installation et prérequis

Pour utiliser correctement ce script vous avez besoin de
*   Python 2.*
*   Tkinter (Librairie de base, elle est normalement installée avec Python)

# Utilisation

Pour utiliser ArbreBinUI, vous pouvez soit le lancer directement:
```sh
$ python affiche_arbre.py
```

Soit l'importer dans vos projets python pour l'utiliser, example:
```python
# -*- coding: utf-8 -*-
from affiche_arbre import *

arbre = entrerArbre(1)
dessiner_arbre(arbre)
```

# Changelog

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

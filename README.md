# ![PythonLogo](https://www.python.org/static/favicon.ico) ArbreBinUI

ArbreBinUI est un script python permettant l'affichage de manière graphique (image) d'un arbre binaire

Ce script fait appel à un autre script permettant la saisie en console d'un arbre binaire ainsi que sa représentation
par une classe *Arbre*. Le script [saisie.py](https://github.com/Astropilot/ArbreBinUI/blob/master/Code/saisie.py) à été développé par Pierre Lartigau en 2016.

![ScreenShot](https://github.com/Astropilot/ArbreBinUI/blob/master/Images/arbresbin.png)

# Installation et prérequis

Pour utiliser correctement ce script vous avez besoin de
*   Python 2.7
*   Pip (recommandé si Pillow n'est pas déjà installée)
*   La bibliothèque python Pillow

Le script python tente de télécharger automatiquement la bibliothèque Pillow si elle n'est pas présente,
si toutefois cela échoue, je vous invite à installer *Pip* avec la commande suivante:
```sh
$ sudo apt-get install pip
```

Et puis ensuite d'installer manuellement la bibliothèque *Pilow*:
```sh
$ pip install pillow
```

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

## 1.0 ##
*   Affichage d'arbres binaires
*   **TODO**: Générer la taille de l'image en fonction de la hauteur de l'arbre
## 1.1 ##
*   La taille de l'image est générée en fonction de la hauteur de l'arbre

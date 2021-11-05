## DM 1 d'informatique

## 1. Écrire une fonction somme telle que somme(n) renvoie la somme des entiers de 1 à n.
## Par exemple, somme(4) renvoie 10 (= 1 + 2 + 3 + 4).

## 2. Écrire une fonction puissance2 telle que puissance2(n) renvoie la liste
## contenant les puissances de 2 jusqu'à 2**n.
## Par exemple, puissance2(4) renvoie [1, 2, 4, 8] (car 2**0 = 1, 2**1 = 2, 2**2 = 4, 2**3 = 8).

## 3. Écrire une fonction produit telle que, si L est une liste de nombre,
## produit(L) renvoie la multiplication de tous les éléments de L
## Par exemple, produit([2, 1, 5, 4]) doit renvoyer 40 (= 2*1*5*4)

## 4. Écrire une fonction egal telle que egal(L) renvoie True si tous les éléments de L sont égaux, False sinon.
## Par exemple, egal([1, 1, 1, 1]) doit renvoyer True, egal([1, 2]) doit renvoyer False.

## 5. Écrire une fonction carre_parfait telle que carre_parfait(n) renvoie True si n peut être écrit comme le carré d'un entier, False sinon.
## Par exemple, carre_parfait(9) doit renvoyer True (car 9 = 3²), carre_parfait(5) doit renvoyer False.

def somme(n):
    return n*(n+1)/2
somme(10)

55.0

def puissance2(n):
    L = []
    for i in range(n):
        L.append(2**i)
    return L
puissance2(7)

[1, 2, 4, 8, 16, 32, 64]

def produit(L):
    p = 1
    for i in range(len(L)):
        p *= L[i]
    return p
produit([7, 80, 2, 2])

2240

def egal(L):
    if L.count(L[0]) == len(L): # si le premier élément de L apparaît autant de fois qu'il y a d'éléments dans L
        return True
    else:
        return False
egal([5, 5, 1, 7, 5])

False

import math
import numpy as np
def carre_parfait(n):
    if np.sqrt(n) == math.floor(np.sqrt(n)): # si la racine carrée de n est égale à sa propre partie entière
        return True
    else:
        return False
carre_parfait(36)

True

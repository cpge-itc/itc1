## DM 1 d'informatique

## 1. Écrire une fonction somme telle que somme(n) renvoie la somme des entiers de 1 à n.
## Par exemple, somme(4) renvoie 10 (= 1 + 2 + 3 + 4).

def somme(n):
    x=0
    for i in range (n+1):
        x=x+i
    return x

## 2. Écrire une fonction puissance2 telle que puissance2(n) renvoie la liste
## contenant les puissances de 2 jusqu'à 2**n.
## Par exemple, puissance2(4) renvoie [1, 2, 4, 8] (car 2**0 = 1, 2**1 = 2, 2**2 = 4, 2**3 = 8).

def puissance2(n):
    L=[]
    for i in range (n):
        L.append(2**i)
    return L

## 3. Écrire une fonction produit telle que, si L est une liste de nombre,
## produit(L) renvoie la multiplication de tous les éléments de L
## Par exemple, produit([2, 1, 5, 4]) doit renvoyer 40 (= 2*1*5*4)

def produit(L):
    x=1
    for i in range (len(L)):
        x=x*L[i]
    return x

## 4. Écrire une fonction egal telle que egal(L) renvoie True si tous les éléments de L sont égaux, False sinon.
## Par exemple, egal([1, 1, 1, 1]) doit renvoyer True, egal([1, 2]) doit renvoyer False.

def egal(L):
    for i in range (len(L)):
        if L[0] !=L[i]:
            return False
    return True

## 5. Écrire une fonction carre_parfait telle que carre_parfait(n) renvoie True si n peut être écrit comme le carré d'un entier, False sinon.
## Par exemple, carre_parfait(9) doit renvoyer True (car 9 = 3²), carre_parfait(5) doit renvoyer False.

def carre_parfait(n):
    if (n**0.5-int(n**0.5))==0 :
        return True
    return False

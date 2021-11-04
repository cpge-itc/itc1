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


## DM 1 d'informatique réponses

## 1. Écrire une fonction somme telle que somme(n) renvoie la somme des entiers de 1 à n.
## Par exemple, somme(4) renvoie 10 (= 1 + 2 + 3 + 4).

def somme(n):
    somme=0
    for i in range(n+1):
        somme=somme+i
    return somme

# on peut aussi définir la fonction avec les formules mathématiques des sommes:

def somm(n):
    somme=((1+n)*n)/2
    return somme

print(somme(4), somme(5), somme(3), somme(12), somm(4), somm(5), somm(3), somm(12))


## 2. Écrire une fonction puissance2 telle que puissance2(n) renvoie la liste contenant les puissances de 2 jusqu'à 2**n.
## Par exemple, puissance2(4) renvoie [1, 2, 4, 8] (car 2**0 = 1, 2**1 = 2, 2**2 = 4, 2**3 = 8).

def puissance2(n):
    puissance2=[]
    for i in range(n):
        puissance2.append(2**i)
    return puissance2

# Cette liste exclut 2**n. Si on veut inclure 2**n, on remplace n par n+1 à la ligne 3.

print(puissance2(4), puissance2(10))


## 3. Écrire une fonction produit telle que, si L est une liste de nombre,
## produit(L) renvoie la multiplication de tous les éléments de L
## Par exemple, produit([2, 1, 5, 4]) doit renvoyer 40 (= 2*1*5*4)

def produit(L):
    produit=1
    for i in L:
        produit=produit*i
    return produit

print(produit([2, 1, 5, 4]))


## 4. Écrire une fonction egal telle que egal(L) renvoie True si tous les éléments de L sont égaux, False sinon.
## Par exemple, egal([1, 1, 1, 1]) doit renvoyer True, egal([1, 2]) doit renvoyer False.

def egal(L):
    for i in L:
        if i!=L[0]:
            return False
    return True

print(egal([1, 1, 1]), egal([2, 0]), egal([5, 5, 5, 5, 5, 5, 5]), egal([1, 3, 6]))


## 5. Écrire une fonction carre_parfait tel le que carre_parfait(n) renvoie True si n peut être écrit comme le carré d'un entier, False sinon.
## Par exemple, carre_parfait(9) doit renvoyer True (car 9 = 3²), carre_parfait(5) doit renvoyer False.

def carre_parfait(n):
    from math import sqrt
    if int(sqrt(n))==sqrt(n):
        return True
    return False

print(carre_parfait(9), carre_parfait(5), carre_parfait(25), carre_parfait(2))


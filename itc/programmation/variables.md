---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.0
kernelspec:
  display_name: Python 3.8.5 64-bit
  name: python3
  language: python
---

# Variables

## Affectation

Une variable en informatique possède 3 caractéristiques :
- un **nom**
- une **valeur**
- un **type**

Par exemple, l'instruction suivante permet de définir une variable nommée `a`, de valeur 42 et de type entier :

```{code-cell} ipython3
a = 42  # définition d'une variable a
```

Lorsque l'on définit une variable de cette façon, la valeur 42 est stockée dans la mémoire RAM et peut être récupérée en écrivant le nom de la variable :

```{code-cell} ipython3
a
```

Python remplace `a` par sa valeur et donne le résultat.  
On peut aussi modifier la valeur de `a` :

```{code-cell} ipython3
a = -4  # modification de a
a
```

De manière générale, une affectation s'écrit sous la forme suivante :
````{margin}
```{danger}
Le sens du symbole = en mathématiques est très différent. Ainsi, en mathématiques, $x = x + y\times4$ est une équation que l'on peut résoudre en $0 = y\times4$, c'est à dire $y = 0$... rien à voir avec ce que fait Python !
```
````
```python
a = expression
```
**Cette affectation a pour effet de calculer la valeur de l'expression et de mettre cette valeur dans `a`.**

Considérons par exemple les lignes suivantes : 
```{code-cell} ipython3
x = 2  # x est défini en prenant la valeur 2
y = 3  # y est défini en prenant la valeur 3
x = x + y*4  # x + y*4 est calculé et sa valeur (14) est mise dans x
print(x)
```

## Types de base

Voici les principaux types qui vont nous intéresser en Python :

| Type | Description | Exemple |
| --- | --- | --- |
| `int` | entier | `0`, `42`, `-7` |
| `float` | nombre à virgule | `3.14`, `-2.718` |
| `bool` | booléen (vrai ou faux) | `True`, `False` |
| `tuple` | $n$-uplet | `(1, 2, 3)`, `(3.14, "chaine", [1, 0])` |
| `list` | liste | `[1, 2, 3]`, `[3.14, "chaine", [1, 0]]` |
| `str` | chaîne de caractères | `"blabla"`, `""`, `"info"` |

### Types numériques : `int`, `float`

* `int` est utilisé pour les entiers (naturels : positif ou négatif).
* `float` est utilisé pour les nombres à virgule. Attention :  
```{danger}
Python utilise en fait des points pour les nombres à virgules. Les virgules sont utilisées pour séparer des éléments, par exemple dans des `tuple` ou `list` :
```
```{code-cell} ipython3
e = 2,718
print(e)  # on a défini un couple et non pas un float !
e = 2.718
print(e)  # cette fois, on a bien un float
```

Voici les opérations que l'on peut effectuer sur les `int` et `float` :

| Opérateur | Signification | Exemple |
| --- | --- | --- |
| `+` | addition | `2 + 3` vaut `5` |
| `-` | soustraction | `2 - 3` vaut `-1` |
| `*` | multiplication | `2*3` vaut `6` |
| `**` | puissance | `2**3` vaut `8` |
| `/` | division (dans $\mathbb{Q}$) | `5/2` vaut `2.5` |
| `//` | division **entière** (dans $\mathbb{N}$) | `5//2` vaut `2`  |

Une racine peut être calculée avec `**`. Par exemple, $\sqrt{2} = 2^{\frac{1}{2}}$ :
```{code-cell} ipython3
2**0.5
```

```{admonition} Exercice
:class: tip
Utiliser Python pour calculer la valeur (approximative) du nombre d'or $\phi = \frac{1 + \sqrt{5}}{2}$
```
```{code-cell} ipython3
# Votre solution
```
```{code-cell} ipython3
:tags: [hide-cell]
(1 + 5**0.5)/2
```

````{admonition} Exercice
:class: tip
Calculer à la main la valeur de l'expression suivante :
```python
(6 + 4**0.5)/2*2
```
````

```{code-cell} ipython3
:tags: [hide-cell]
(6 + 4**0.5)/2*2
```

On peut comparer des `int`/`float` de la façon suivante :
````{margin}
```{danger}
Ne pas confondre `a = b`, qui permet de mettre la valeur de `b` dans `a`, et `a == b` qui permet de tester si `a` et `b` ont la même valeur.  
```
````
| Symbole | Signification | Exemple |
| --- | --- | --- |
| `==` | égal | `0 == 0` vaut `True`, `3.14 == 3` vaut `False` |
| `<` | inférieur strictement | `1 < 2` vaut `True`, `3.14 < 3.14` vaut `False` |
| `>` | supérieur strictement | `1 > 2` vaut `False`, `3.14 > 3.14` vaut `False` |
| `<=` | inférieur ou égal | `1 <= 2` vaut `True`, `3.14 <= 3.14` vaut `True` |
| `>=` | supérieur ou égal | `1 >= 2` vaut `False`, `3.14 >= 3.14` vaut `True` |
| `!=` | différent | `1 != 2` vaut `True`, `3.14 != 3.14` vaut `False` |


Il est possible d'enchaîner des comparaisons. Par exemple, pour tester si $\phi$ est compris entre 1 et 2 :
```{code-cell} ipython3
1 < (1 + 5**0.5)/2 < 2
```

### Booléens

| Opérateur | Signification | Exemple |
| --- | --- | --- |
| `or` | ou | `0 == 0 or 3.14 == 3` vaut `True` |
| `and` | et | `0 == 0 and 3.14 == 3` vaut `False` |
| `not` | négation | `not 0 < 1` vaut `False` |

````{admonition} Exercice
:class: tip
Donner la valeur de l'expression suivante :
```python
not (1 <= 1 and (1 == 2 or 0 != 1))
```
````
```{code-cell} ipython3
:tags: [hide-cell]
not (1 <= 1 and (1 == 2 or 0 != 1))
```

### Listes

Une liste sert à stocker plusieurs éléments. Par exemple, pour définir une liste contenant l'entier 1, le booléen `True` et le flottant `3.14` :
```{code-cell} ipython
:tags: []

L = [1, True, 3.14]
L
```

```{list-table}
:header-rows: 1

* - Python
  - Signification
  - Exemple
* - `[..., ..., ...]`
  - Création d'une liste
  - `[1, True, 3.14]` <br> `[]` (liste vide)
* - `len(L)`
  - Taille d'une liste `L`
  - `len([1, True, 3.14])` vaut 3
* - `L[i]`
  - Élement d'indice `i` d'une liste `L`
  - Si `L` vaut `[1, True, 3.14]`, <br> `L[0]` vaut `1`, `L[1]` vaut `True`, `L[2]` vaut `3.14`
* - `L.append(e)`
  - Ajoute un élément `e` à une liste `L`
  - `L.append(42)`
``` 
```{danger}
`L.append(e)` modifie `L`, il ne faut donc surtout pas écrire `L = L.append(e)` (erreur fréquente).
```

```{danger}
Les indices commencent toujours à 0 en informatique. Le dernier indice d'une liste `L` est `len(L) - 1`.
```
`L[-1]` est un raccourci permettant d'accéder au dernier élément d'une liste. De même, `L[-2]` accède à l'avant dernier élément...

Essayer d'accéder à un élément qui n'existe pas produit une erreur :
``` python
L = [3, 1, 4]
print(L[2])  # donne 4
print(L[3])  # erreur
```
```
4
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-13-e387ee5c742b> in <module>
      1 L = [3, 1, 4]
      2 print(L[2])  # pas de problème
----> 3 print(L[3])  # erreur

IndexError: list index out of range
```

````{margin}
```{danger}
Les indices de fin sont presque toujours exclu en Python, par convention.
```

````
L'opération de *slicing* `L[i:j]` permet d'extraire une sous liste de `L` contenant les éléments de l'indice `i` inclu à `j` **exclu** :

```{code-cell} ipython3
L = [-3, 0, 42, 7, 5]
L[1:3]
```

Dans un slicing, il est possible d'ommettre l'indice de début (auquel cas la liste ext extraite à partir du début) ou l'indice de fin (auquel cas la liste ext extraite jusqu'à la fin).

```{code-cell} ipython3
print(L[:2])  # sous-liste du 1er au 2ème élément
print(L[-2:])  # sous-liste de l'avant-dernier au dernier élément
```

### Chaînes de caractères

Les chaînes de caractères (string en anglais) servent à stocker du texte, sous forme d'une suite de caractères (symboles). Contrairement aux listes, il n'est pas possible de modifier une chaîne de caractères (on dit que c'est un type immutable)). Par exemple, il n'y a pas de `append` sur les chaîne de caractères.


```{code-cell} ipython3
s = "l'informatique c'est fun"  # définition d'une chaîne de caractères
print(len(s))  # taille de s
print(s[2])  # caractère d'indice 2 (c'est à dire en 3ème position)
# s[0] = "L"  # ERREUR : on ne peut pas modifier un str
# s.append("!")  # ERREUR : on ne peut pas modifier un str
```


### Tuples

Les tuples (ou $n$-uplets) sont la généralisation des couples, triplets... Ils ressemblent beaucoup aux chaînes de caractères (en particulier, ils sont immutables) mais servent à stocker autre chose que du texte. 

```{code-cell} ipython3
t = (2, 3, 4, 5)
print(t[1])  # donne 3
print(len(t))  # donne 4
# t[1] = 6  ERREUR : on ne peut pas modifier un tuple
# t.append(6)  # ERREUR : on ne peut pas modifier un tuple
```

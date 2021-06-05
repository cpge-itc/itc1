---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.0
---

# Variables

## Affectation

Une variable en informatique possède 3 caractéristiques :
- un nom
- une valeur
- un type

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
```python
a = expression
```
**Cette affectation a pour effet de calculer la valeur de expression et de mettre cette valeur dans `a`.**

Considérons par exemple les lignes suivantes : 
```{code-cell} ipython3
x = 2
y = 3
x = x + y*4
print(x)
```
Voici le fonctionnement détaillé :
- `x` est défini en prenant la valeur 2
- `y` est défini en prenant la valeur 3
- `x + y*4` est calculé, ce qui donne 14
- `x` prend la valeur 14 


```{danger}
Le sens du symbole = en mathématiques est très différent. Ainsi, en mathématiques, $x = x + y\times4$ est une équation que l'on peut résoudre en $0 = y\times4$, c'est à dire $y = 0$... rien à voir avec ce que fait Python !
```

| Python | Description | Exemple |
| --- | --- | --- |
| `int` | entier | `0`, `42`, `-7` |
| `float` | nombre à virgule | `3.14`, `-2.718` |
| `bool` | booléen (vrai ou faux) | `True`, `False` |
| `str` | chaîne de caractères | `"blabla"`, `""`, `"info"` |
| `list` | liste | `[1, 2, 3]`, `[3.14, "chaine", [1, 0]]` |

## Types numériques : `int`, `float`

* `int` est utilisé pour les entiers (naturels : positif ou négatif).

Voici les opérations que l'on peut effectuer sur les `int` et `float` :

| Python | Signification | Exemple |
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
:tags: ["hide-cell"]
(1 + 5**0.5)/2
```

````{admonition} Exercice
:class: tip
Donner la valeur de l'expression suivante :
```python
(6 + 4**0.5)/2*2
```
````

```{code-cell} ipython3
:tags: ["hide-cell"]
(6 + 4**0.5)/2*2
```

On peut comparer des `int`/`float` de la façon suivante :
| Python | Signification | Exemple |
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

```{danger}
Ne pas confondre `a = b`, qui permet de mettre la valeur de `b` dans `a`, et `a == b` qui permet de tester si `a` et `b` ont la même valeur.  
```

---

## Booléens


| Python | Signification | Exemple |
| --- | --- | --- |
| `or` | ou | `0 == 0 or 3.14 == 3` vaut `True` |
| `and` | et | `0 == 0 and 3.14 == 3` vaut `False` |
| `not` | négation | `not 0 < 1` vaut `False` |
| `<=` | inférieur ou égal | `1 <= 2` est `True`, `3.14 <= 3.14` vaut `True` |
| `>=` | supérieur ou égal | `1 >= 2` est `False`, `3.14 >= 3.14` vaut `True` |
| `!=` | différent | `1 != 2` est `True`, `3.14 != 3.14` vaut `False` |

````{admonition} Exercice
:class: tip
Donner la valeur de l'expression suivante :
```python
not (1 <= 1 and (1 == 2 or 0 != 1))
```
````
```{code-cell} ipython3
:tags: ["hide-cell"]
not (1 <= 1 and (1 == 2 or 0 != 1))
```

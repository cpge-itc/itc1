---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.0
kernelspec:
  display_name: Python 3.8.5 64-bit
  name: python385jvsc74a57bd0916dbcbb3f70747c44a77c7bcd40155683ae19c65e1c03b4aa3499c5328201f1
---

# Variables

## Définition
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

```{danger}
Même si la définition d'une variable et la modification d'une variable s'écrivent de la même façon en Python (`a = ...`), il s'agit de deux instructions fondamentalement différentes.   
```

+++

```{dropdown} Types classiques
:open:
| Python | Description | Exemples |
| --- | --- | --- |
| `int` | entier | `0`, `42`, `-7` |
| `bool` | booléen (vrai ou faux) | `True`, `False` |
| `float` | nombre à virgule | `3.14`, `-2.718` |
| `str` | chaîne de caractères | `"blabla"`, `""`, `"info"` |
| `list` | liste | `[1, 2, 3]`, `[3.14, "chaine", [1, 0]]` |
```

### Types numériques : `int`, `float`

* `int` est utilisé pour les entiers (naturels : positif ou négatif).

```{dropdown} Opérations numériques
:open:
| Python | Signification | Exemples |
| --- | --- | --- |
| `+` | addition | `` vaut `False` |
| `<` | inférieur strictement | `1 < 2` vaut `True`, `3.14 < 3.14` vaut `False` |
| `>` | supérieur strictement | `1 > 2` vaut `False`, `3.14 > 3.14` vaut `False` |
| `<=` | inférieur ou égal | `1 <= 2` vaut `True`, `3.14 <= 3.14` vaut `True` |
| `>=` | supérieur ou égal | `1 >= 2` vaut `False`, `3.14 >= 3.14` vaut `True` |
| `!=` | différent | `1 != 2` vaut `True`, `3.14 != 3.14` vaut `False` |
```

```{dropdown} Comparaisons numériques
:open:
| Python | Signification | Exemples |
| --- | --- | --- |
| `==` | égal | `0 == 0` vaut `True`, `3.14 == 3` vaut `False` |
| `<` | inférieur strictement | `1 < 2` vaut `True`, `3.14 < 3.14` vaut `False` |
| `>` | supérieur strictement | `1 > 2` vaut `False`, `3.14 > 3.14` vaut `False` |
| `<=` | inférieur ou égal | `1 <= 2` vaut `True`, `3.14 <= 3.14` vaut `True` |
| `>=` | supérieur ou égal | `1 >= 2` vaut `False`, `3.14 >= 3.14` vaut `True` |
| `!=` | différent | `1 != 2` vaut `True`, `3.14 != 3.14` vaut `False` |
```

```{note}
Ne pas confondre `a = b`, qui permet de mettre la valeur de `b` dans `a`, et `a == b` qui permet de tester si `a` et `b` ont la même valeur.  
```

```{dropdown} **Opérateurs booléens**
:open:
| Python | Signification | Exemples |
| --- | --- | --- |
| `or` | ou | `0 == 0 or 3.14 == 3` vaut `True` |
| `and` | et | `0 == 0 and 3.14 == 3` vaut `False` |
| `not` | négation | `not 0 < 1` vaut `False` |
| `<=` | inférieur ou égal | `1 <= 2` est `True`, `3.14 <= 3.14` vaut `True` |
| `>=` | supérieur ou égal | `1 >= 2` est `False`, `3.14 >= 3.14` vaut `True` |
| `!=` | différent | `1 != 2` est `True`, `3.14 != 3.14` vaut `False` |

```{admonition} Exercice
:class: tip
- Que vaut `not ()
```

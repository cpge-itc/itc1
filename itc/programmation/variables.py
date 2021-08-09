{
  "nbformat": 4,
  "nbformat_minor": 5,
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3.8.5 64-bit",
      "language": "python",
      "name": "python3"
    },
    "colab": {
      "name": "variables.ipynb",
      "provenance": []
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5bd539ce"
      },
      "source": [
        "# Variables\n",
        "\n",
        "## Affectation\n",
        "\n",
        "Une variable en informatique possède 3 caractéristiques :\n",
        "- un **nom**\n",
        "- une **valeur**\n",
        "- un **type**\n",
        "\n",
        "Par exemple, l'instruction suivante permet de définir une variable nommée `a`, de valeur 42 et de type entier :"
      ],
      "id": "5bd539ce"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "46f4dfa5"
      },
      "source": [
        "a = 42  # définition d'une variable a"
      ],
      "id": "46f4dfa5",
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4a6ccfb5"
      },
      "source": [
        "Lorsque l'on définit une variable de cette façon, la valeur 42 est stockée dans la mémoire RAM et peut être récupérée en écrivant le nom de la variable :"
      ],
      "id": "4a6ccfb5"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e61f2cb6"
      },
      "source": [
        "a"
      ],
      "id": "e61f2cb6",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "111ceb40"
      },
      "source": [
        "Python remplace `a` par sa valeur et donne le résultat.  \n",
        "On peut aussi modifier la valeur de `a` :"
      ],
      "id": "111ceb40"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9cfc31ae"
      },
      "source": [
        "a = -4  # modification de a\n",
        "a"
      ],
      "id": "9cfc31ae",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "757d3a7b"
      },
      "source": [
        "De manière générale, une affectation s'écrit sous la forme suivante :\n",
        "````{margin}\n",
        "```{danger}\n",
        "Le sens du symbole = en mathématiques est très différent. Ainsi, en mathématiques, $x = x + y\\times4$ est une équation que l'on peut résoudre en $0 = y\\times4$, c'est à dire $y = 0$... rien à voir avec ce que fait Python !\n",
        "```\n",
        "````\n",
        "```python\n",
        "a = expression\n",
        "```\n",
        "**Cette affectation a pour effet de calculer la valeur de l'expression et de mettre cette valeur dans `a`.**\n",
        "\n",
        "Considérons par exemple les lignes suivantes :"
      ],
      "id": "757d3a7b"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "08972b4c"
      },
      "source": [
        "x = 2  # x est défini en prenant la valeur 2\n",
        "y = 3  # y est défini en prenant la valeur 3\n",
        "x = x + y*4  # x + y*4 est calculé et sa valeur (14) est mise dans x\n",
        "print(x)"
      ],
      "id": "08972b4c",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "29656743"
      },
      "source": [
        "## Types de base\n",
        "\n",
        "Voici les principaux types qui vont nous intéresser en Python :\n",
        "\n",
        "| Type | Description | Exemple |\n",
        "| --- | --- | --- |\n",
        "| `int` | entier | `0`, `42`, `-7` |\n",
        "| `float` | nombre à virgule | `3.14`, `-2.718` |\n",
        "| `bool` | booléen (vrai ou faux) | `True`, `False` |\n",
        "| `tuple` | $n$-uplet | `(1, 2, 3)`, `(3.14, \"chaine\", [1, 0])` |\n",
        "| `list` | liste | `[1, 2, 3]`, `[3.14, \"chaine\", [1, 0]]` |\n",
        "| `str` | chaîne de caractères | `\"blabla\"`, `\"\"`, `\"info\"` |\n",
        "\n",
        "### Types numériques : `int`, `float`\n",
        "\n",
        "* `int` est utilisé pour les entiers (naturels : positif ou négatif).\n",
        "* `float` est utilisé pour les nombres à virgule. Attention :  \n",
        "```{danger}\n",
        "Python utilise en fait des points pour les nombres à virgules. Les virgules sont utilisées pour séparer des éléments, par exemple dans des `tuple` ou `list` :\n",
        "```"
      ],
      "id": "29656743"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "83f7142e"
      },
      "source": [
        "e = 2,718\n",
        "print(e)  # on a défini un couple et non pas un float !\n",
        "e = 2.718\n",
        "print(e)  # cette fois, on a bien un float"
      ],
      "id": "83f7142e",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "df3fd2c7"
      },
      "source": [
        "Voici les opérations que l'on peut effectuer sur les `int` et `float` :\n",
        "\n",
        "| Opérateur | Signification | Exemple |\n",
        "| --- | --- | --- |\n",
        "| `+` | addition | `2 + 3` vaut `5` |\n",
        "| `-` | soustraction | `2 - 3` vaut `-1` |\n",
        "| `*` | multiplication | `2*3` vaut `6` |\n",
        "| `**` | puissance | `2**3` vaut `8` |\n",
        "| `/` | division (dans $\\mathbb{Q}$) | `5/2` vaut `2.5` |\n",
        "| `//` | division **entière** (dans $\\mathbb{N}$) | `5//2` vaut `2`  |\n",
        "\n",
        "Une racine peut être calculée avec `**`. Par exemple, $\\sqrt{2} = 2^{\\frac{1}{2}}$ :"
      ],
      "id": "df3fd2c7"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ea5988f9"
      },
      "source": [
        "2**0.5"
      ],
      "id": "ea5988f9",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b95fa959"
      },
      "source": [
        "```{admonition} Exercice\n",
        ":class: tip\n",
        "Utiliser Python pour calculer la valeur (approximative) du nombre d'or $\\phi = \\frac{1 + \\sqrt{5}}{2}$\n",
        "```"
      ],
      "id": "b95fa959"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e645338c"
      },
      "source": [
        "# Votre solution"
      ],
      "id": "e645338c",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "hide-cell"
        ],
        "id": "0e07acca"
      },
      "source": [
        "(1 + 5**0.5)/2"
      ],
      "id": "0e07acca",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c576895b"
      },
      "source": [
        "````{admonition} Exercice\n",
        ":class: tip\n",
        "Calculer à la main la valeur de l'expression suivante :\n",
        "```python\n",
        "(6 + 4**0.5)/2*2\n",
        "```\n",
        "````"
      ],
      "id": "c576895b"
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "hide-cell"
        ],
        "id": "25cb6360"
      },
      "source": [
        "(6 + 4**0.5)/2*2"
      ],
      "id": "25cb6360",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e02ddf3b"
      },
      "source": [
        "On peut comparer des `int`/`float` de la façon suivante :\n",
        "````{margin}\n",
        "```{danger}\n",
        "Ne pas confondre `a = b`, qui permet de mettre la valeur de `b` dans `a`, et `a == b` qui permet de tester si `a` et `b` ont la même valeur.  \n",
        "```\n",
        "````\n",
        "| Symbole | Signification | Exemple |\n",
        "| --- | --- | --- |\n",
        "| `==` | égal | `0 == 0` vaut `True`, `3.14 == 3` vaut `False` |\n",
        "| `<` | inférieur strictement | `1 < 2` vaut `True`, `3.14 < 3.14` vaut `False` |\n",
        "| `>` | supérieur strictement | `1 > 2` vaut `False`, `3.14 > 3.14` vaut `False` |\n",
        "| `<=` | inférieur ou égal | `1 <= 2` vaut `True`, `3.14 <= 3.14` vaut `True` |\n",
        "| `>=` | supérieur ou égal | `1 >= 2` vaut `False`, `3.14 >= 3.14` vaut `True` |\n",
        "| `!=` | différent | `1 != 2` vaut `True`, `3.14 != 3.14` vaut `False` |\n",
        "\n",
        "\n",
        "Il est possible d'enchaîner des comparaisons. Par exemple, pour tester si $\\phi$ est compris entre 1 et 2 :"
      ],
      "id": "e02ddf3b"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "46a326bc"
      },
      "source": [
        "1 < (1 + 5**0.5)/2 < 2"
      ],
      "id": "46a326bc",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e114c39d"
      },
      "source": [
        "### Booléens\n",
        "\n",
        "| Opérateur | Signification | Exemple |\n",
        "| --- | --- | --- |\n",
        "| `or` | ou | `0 == 0 or 3.14 == 3` vaut `True` |\n",
        "| `and` | et | `0 == 0 and 3.14 == 3` vaut `False` |\n",
        "| `not` | négation | `not 0 < 1` vaut `False` |\n",
        "\n",
        "````{admonition} Exercice\n",
        ":class: tip\n",
        "Donner la valeur de l'expression suivante :\n",
        "```python\n",
        "not (1 <= 1 and (1 == 2 or 0 != 1))\n",
        "```\n",
        "````"
      ],
      "id": "e114c39d"
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "hide-cell"
        ],
        "id": "404b1440"
      },
      "source": [
        "not (1 <= 1 and (1 == 2 or 0 != 1))"
      ],
      "id": "404b1440",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "39797cf1"
      },
      "source": [
        "### Listes\n",
        "\n",
        "Une liste sert à stocker plusieurs éléments. Par exemple, pour définir une liste contenant l'entier 1, le booléen `True` et le flottant `3.14` :"
      ],
      "id": "39797cf1"
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [],
        "id": "59a96c3b"
      },
      "source": [
        "L = [1, True, 3.14]\n",
        "L"
      ],
      "id": "59a96c3b",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5ab7034b"
      },
      "source": [
        "```{list-table}\n",
        ":header-rows: 1\n",
        "\n",
        "* - Python\n",
        "  - Signification\n",
        "  - Exemple\n",
        "* - `[..., ..., ...]`\n",
        "  - Création d'une liste\n",
        "  - `[1, True, 3.14]` <br> `[]` (liste vide)\n",
        "* - `len(L)`\n",
        "  - Taille d'une liste `L`\n",
        "  - `len([1, True, 3.14])` vaut 3\n",
        "* - `L[i]`\n",
        "  - Élement d'indice `i` d'une liste `L`\n",
        "  - Si `L` vaut `[1, True, 3.14]`, <br> `L[0]` vaut `1`, `L[1]` vaut `True`, `L[2]` vaut `3.14`\n",
        "* - `L.append(e)`\n",
        "  - Ajoute un élément `e` à une liste `L`\n",
        "  - `L.append(42)`\n",
        "``` \n",
        "```{danger}\n",
        "`L.append(e)` modifie `L`, il ne faut donc surtout pas écrire `L = L.append(e)` (erreur fréquente).\n",
        "```\n",
        "\n",
        "```{danger}\n",
        "Les indices commencent toujours à 0 en informatique. Le dernier indice d'une liste `L` est `len(L) - 1`.\n",
        "```\n",
        "`L[-1]` est un raccourci permettant d'accéder au dernier élément d'une liste. De même, `L[-2]` accède à l'avant dernier élément...\n",
        "\n",
        "Essayer d'accéder à un élément qui n'existe pas produit une erreur :"
      ],
      "id": "5ab7034b"
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "hide-output"
        ],
        "id": "d1f0463f"
      },
      "source": [
        "L = [3, 1, 4]\n",
        "print(L[2])  # donne 4\n",
        "print(L[3])  # ERREUR"
      ],
      "id": "d1f0463f",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "510f2d71"
      },
      "source": [
        "````{margin}\n",
        "```{danger}\n",
        "Les indices de fin sont presque toujours exclu en Python, par convention.\n",
        "```\n",
        "\n",
        "````\n",
        "L'opération de *slicing* `L[i:j]` permet d'extraire une sous liste de `L` contenant les éléments de l'indice `i` inclu à `j` **exclu** :"
      ],
      "id": "510f2d71"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cfd2bd1b"
      },
      "source": [
        "L = [-3, 0, 42, 7, 5]\n",
        "L[1:3]"
      ],
      "id": "cfd2bd1b",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3e4915c0"
      },
      "source": [
        "Dans un slicing, il est possible d'ommettre l'indice de début (auquel cas la liste ext extraite à partir du début) ou l'indice de fin (auquel cas la liste ext extraite jusqu'à la fin)."
      ],
      "id": "3e4915c0"
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1fdcbfc5"
      },
      "source": [
        "print(L[:2])  # sous-liste du 1er au 2ème élément\n",
        "print(L[-2:])  # sous-liste de l'avant-dernier au dernier élément"
      ],
      "id": "1fdcbfc5",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5720998a"
      },
      "source": [
        "### Chaînes de caractères\n",
        "\n",
        "Les chaînes de caractères (string en anglais) servent à stocker du texte, sous forme d'une suite de caractères (symboles). Contrairement aux listes, il n'est pas possible de modifier une chaîne de caractères (on dit que c'est un type immutable)). Par exemple, il n'y a pas de `append` sur les chaîne de caractères."
      ],
      "id": "5720998a"
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "hide-output"
        ],
        "id": "795daef3"
      },
      "source": [
        "s = \"l'informatique c'est fun\"  # définition d'une chaîne de caractères\n",
        "print(len(s))  # taille de s\n",
        "print(s[2])  # caractère d'indice 2 (c'est à dire en 3ème position)\n",
        "s[0] = \"L\"  # ERREUR : on ne peut pas modifier un str\n",
        "s.append(\"!\")  # ERREUR : on ne peut pas modifier un str"
      ],
      "id": "795daef3",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e9a46a7b"
      },
      "source": [
        "### Tuples\n",
        "\n",
        "Les tuples (ou $n$-uplets) sont la généralisation des couples, triplets... Ils ressemblent beaucoup aux chaînes de caractères (en particulier, ils sont immutables) mais servent à stocker autre chose que du texte."
      ],
      "id": "e9a46a7b"
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "hide-output"
        ],
        "id": "54bf420a"
      },
      "source": [
        "t = (2, 3, 4, 5)\n",
        "print(t[1])  # donne 3\n",
        "print(len(t))  # donne 4\n",
        "t[1] = 6  # ERREUR : on ne peut pas modifier un tuple\n",
        "t.append(6)  # ERREUR : on ne peut pas modifier un tuple"
      ],
      "id": "54bf420a",
      "execution_count": null,
      "outputs": []
    }
  ]
}
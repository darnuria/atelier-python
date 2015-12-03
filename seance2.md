# Séance 1: Fonctions

## 1.0: Introduction

Une fonction est comme un sous-programme déjà écrit par quelqu'un ou vous même.
Afin de le réutiliser facilement. `print` en Python est une fonction de même que `input`.

En Python le mot clef pour définir une fonction est `def`.
Il s'utilise de la façon suivante:

On suppose que notre fichier s'appellera `mon_fichier.py`.

```python
# -- mon_ficher.py --

# On définit la fonction ma_fonction.
def ma_fonction():
    # On rédige les instructions de la fonction.
    print('Hello World')

# On appel la fonction `ma_fonction`.
ma_fonction()
```

Examinons le résultat de l'exécution de notre programme.
```shell
> python3 mon_fichier.py
Hello World
```

Nous avons donc écris une fonction qui ne prends pas de *paramètres*.
Et qui agit par *effet de bords*, c'est à dire elle ne nous rends pas une valeur.
Cela s'illustre par le fait qu'elle affiche via `print` son résultat.
Nous reviendrons sur ce détail sous peu.

## 1.1: Fonctions avec paramètres.

Maintenant nous aimerons pouvoir écrire une fonction qui à le comportement du programme `is_even`.

Pour rappel voici le code de `is_even`:
```python
nb = int(input("entrez un nombre entier: "))
if ((nb % 2) == 0):
    print(True)
else:
    print(False)
```

Transformé en fonction cela donnerais:
```python
# On définit is_even avec un paramètre nb.
def is_even(nb):
    if ((nb % 2) == 0):
        print(True)
    else:
        print(False)

# On pratique quelques test en appellant is_even
# avec differents paramètres
is_even(2)
is_even(2 * 3)
a = 5
is_even(a)
is_even(a * 2)
```

On notera que le *paramètre* `nb` est propre au *contexte* de la fonction
is_even. Si nous avions un autre `nb` dans le *context global* du programme
il serait *masqué* le temps de la fonction.

Exemple:
```python
nb = 3 # nb global au programme.

def print_nombre(nb): # nb de la fonction
    print(nb)

print_nombre(nb)
print_nombre(5)
```

### 1.2.3: Contextes

On observe que le `nb` du contexte global est occulté, par
le `nb` de la fonction `print_nombre`.
Mais une fois sorti de l'appel de `print_nombre` nb est à nouveau nb du contexte global.
C'est important de noté ce détail car cela pourrait être une source de comportements inattendus dans vos programmes.

## 1.2: Fonctions retournant une valeur.

Les fonctions que nous avons écris actuellement ont un défaut majeur.
Nous ne pouvons pas récupérer le résultat de leur calcul.

En effet si nous voulions *affecter* à la variable `a` le résultat de `is_even(3)`.
Cela ne produirait pas ce que l'ont veux.
```python
def is_even(nb):
    if ((nb % 2) == 0):
        print(True)
    else:
        print(False)

a = is_even(3)
print(a)
```
```shell
> python3 is_even.py
False
None
```
Hmm pas tout à fait le résultat que nous attendions. `a` ne vaut pas la valeur du résultat de is_even.

Pour arriver à ce résultat il faut introduire le mot clef `return` à notre
vocabulaire.
Ce mot clef permet de renvoyer au *contexte appellant* de la
fonction le résultat du calcul de cette dernière.

Ce mot clef s'utilise de la façon suivante:

```python
def is_even(nb):
    if ((nb % 2) == 0):
        return True
    else:
        return False

a = is_even(7)
print(a) # False
print(is_even(3)) # False
print(is_even(4 + 4)) # True
```

Il nous permet donc de récupérer le résultat de la fonction.
Et de le réutiliser.
Notez bien que la fonction n'est en rien altérée par son appel.

## 1.3: Applications:

Écrire dans des fichier Python séparées dans un dossier `seance2_fonctions`.

### 1.3.1: Simplifier is_even. (is_even.py_

On a vu comment écrire `is_even` avec une fonction.
Maintenant simplifiez `is_even` pour qu'elle ne tienne que sur une ligne avec un `return`.

### 1.3.2: Récrire is_between(inf, sup, n) (is_between.py)

Réécrivez la fonction `is_between`. Qui renvoie `True` si et seulement si n est strictement compris entre inf et sup sinon faux.

### 1.3.4: Écrire la fonction Maximum. (maximum.py)

Écrire la fonction qui renvoie le nombre le plus grand nombre entre a et b.

Par exemple `maximum(5, 2)` renvoie `2`.

### 1.3.4: Écrire la fonction xor. (xor.py)

Écrire une fonction `xor(a, b)` qui calcul le “Ou exclusif” de a et de b.

Pour information voici la table de vérité du
[xor](https://fr.wikipedia.org/wiki/Fonction_OU_exclusif):

| a xor b |   a   |  b    |
| --------|:-----:|------:|
| False   | False | False |
| True    | False | True  |
| True    | True  | False |
| False   | True  | True  |

Vous n'aurez besoin que d'une ligne avec un `return` pour l'écrire.

### 1.3.4: Écrire la fonction identité (id.py)

La fonction
[identité](https://fr.wikipedia.org/wiki/Application_identit%C3%A9) est la fonction qui pour toute valeur x renvoie x.

### 1.3.5: Écrire la fonction min: (min.py)

Cette fonction renvoie le nombre minimum entre a et b.
Ainsi `minimum(5, 3)` renvoie `3`.

## 1.4: Fonctions récursives

A présent que nous maitrisons bien les fonctions nous allons voir une façon,
de faire répéter à un programme Python une série d'action.

Vous le ne saviez peut-être pas. Mais il est possible d'appeler une fonction dans une fonction. Et même de faire s'appeler une fonction dans sa définition!

Attention la fonction suivante ne s'arrête pas et causera surement une erreur.

```python
def loop():
    print("Hellooooo!")
    loop()

loop()
```

Mais si l'on définit un *cas d'arrêt* et un *cas récursif* alors nos fonctions peuvent s'arrêter au bout d'un moment.

### 1.4.0: is_even récursif (is_even_rec.py)
Par exemple on aurais pu écrire `is_even` de la façon suivante même si c'est
dramatique en terme de *complexité*:

En se basant sur le constat que:
On sait que 1 est impair par définition.

Et donc que dire que `n` est pair. C'est comme dire que `n - 1` est impair.
Alors `n - 1` impair soit `n - 2` pair...

On arrive ainsi à 1 et si on *dépile* les sous résultats.
On peut déterminer si `n` est pair ou impair.

```python
def is_even(n):
    # Si n = 1 Alors n n'est pas pair.
    if n == 1:
        return False
    else:
        return not is_even(n - 1)
```

C'est perturbant au début mais force est de constaté que cela marche.

Essayez de dérouler(c'est à dire faire comme si vous etiez Python) sur papier les appels récursif pour bien comprendre pour `is_even(3)`.

### 1.4.1: Écrire la fonction récursive sum_n(n)

Écrire la fonction récursive `sum_n(n)` qui calcul la somme de tout les entiers de 0 à n. n est donner en paramètre.

Indices:

Le *cas de base* sera si `n == 0`. On renvoie 0.

Le *cas récursif* sera sinon on revoie n + sum_n(n - 1).

# 1.5: Bonus!










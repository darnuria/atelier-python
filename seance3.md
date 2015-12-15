# Séance 2: Itération et Collections

## 2.0: Introduction

Comme nous l'avons vu lors de la séance précédente.
Une fonction est une façon d'abstraire un calcul ou un sous-programme.
Afin d'éviter de se répéter.

## 2.0.1: Paramètres
Rappel: Une fonction peut prendre des paramètres. Ce sont des variables locales à la fonction sauf dans certains cas.

```python
# On dit que author et words sont des paramètres de la fonction.
def say(author, words):
    print(author + ': ' + words)

say("Me", "Hello world")
```

Attention si dans un contexte un paramètre et une variable ont le même nom Python choisira la définition la plus proche.

```python
a = "Je suis 'a' du contexte global."

def f(a):
    # affiche le a de la définiton.
    # pas le a définit au début.
    print(a)

f("Je ne suis pas le a précédent!")
```

## 2.0.2: Return

Rappel: `Return` renvoie le résultat de l'expression. Et sors de la fonction.

Exemple:
```python
def add(a, b):
    return a + b

def add3(a, b ,c):
    return add(a, add(b, c))
```

Dans le cas des appels récursifs ont à donc une accumulation de `return` qui doit se résoudre. Comme nous avions vu avec la fonction somme.

## 2.0.3: Fonctions récursives et boucles

A titre d'exemple voici plusieurs façon d'écrire la fonction qui calcul la (factorielle)[https://fr.wikipedia.org/wiki/Factorielle] d'un nombre n.

```python
# De façon récursive.
def factorielle(n):
    if (n > 1):
        return n * factorielle(n - 1)
    else:
        return 1

# Avec une boucle while.
def factorielle(n):
  fact = 1
  while (n > 1):
      fact = fact * n
      n = n - 1
  return fact

# Avec une boucle for.
def factorielle(n):
    fact = 1
    for n in range(1, n + 1):
        fact = fact * n
    return fact

# Ou simplement car python propose des fonctions déjà existantes.
from math import factorial
n = 5
print(factorial(n))
```

Ces trois définitions sont équivalentes elles calculent toutes la
factorielle d'un nombre n.

Nous avions vu jusque la que les fonctions récursives.
Nous reviendrons sur les boucles `for` et `while` dans ce cours.

## 2.1: Itération

Un des principes récurrent en programme est l'itération. Il peut s'exprimer
au travers de fonctions récursives ou bien de boucles. L'idée de de
continuer un calcul tant qu'une condition n'est pas satisfaite.

Les fonctions récursives sont une façon de faire adopté par le paradigme de
(programmation
 fonctionnelle)[https://fr.wikipedia.org/wiki/Programmation_fonctionnelle].
Cependant Python est un langage versé principalement dans les paradigmes de programmation
(Imperative)[https://fr.wikipedia.org/wiki/Programmation_imp%C3%A9rative] et
(Objet)[https://fr.wikipedia.org/wiki/Programmation_orient%C3%A9e_objet].

La façon la plus “commune” en python pour exprimer l'itération est en général la boucle `for`.

Cependant il était intéressant de voir les fonctions récursives pour s'habituer aux fonctions.

### 2.1.1: mot-clef `while`

Nous avons vu en cours rapidement le mot-clé `while` qui permet de répéter un calcul tant qu'une condition n'est pas satisfaite.

Il s'utilise de la façon suivante
```python
# while (condition boolenne):
#     Instructions...

# Par exemple:
# Calcul de la somme de 0 à n inclu.
def somme(n):
    sum = 0
    # On continue tant que n est supérieur ou égal à 0.
    while (n >= 0):
        sum = sum + n
        n = n - 1
    return sum

print(somme(3))
```

Une pratique courante est d'incrémenter(ajouter 1) ou décrémenter(enlever 1) à une variable pour savoir si on rempli la condition de fin.
Nous reviendrons dessus en cours.

### 2.1.2: mot-clef `for`

En python il existe aussi des boucles `for`. Ce mot clef est très puissant
et permet de faire beaucoup de choses. Pour l'instant nous l'utiliseront
ainsi:

```python
# for iterateur in collection:
#     instructions
```

Un _iterateur_ est l'élément courant d'une _collection_.
Par exemple:

```python
for elem in range(0, 4):
    print(elem)
```

Affichera `0, 1, 2, 3` avec 4 exclut.
On observe donc que `range(0, 4)` crée une _collection_ et que _elem_ est tour
à tour un des éléments de la collection crée par `range(0, 4)`.

Nous reviendrons dans les détails de la boucle for une fois que nous seront
aux listes mais c'est une notion très importante de Python.

## 2.2: Collections

Actuellement nous avons utiliser que des structures de données très simple tel que des entiers.

A présent nous allons voir qu'il est possible de créer des collections de
données. Vous avez déjà manipuler une structure tel que celle çi. Il s'agissait des chaines de caractères qui regroupe plusieurs caractères.

```python
collection = "Je suis une collection!"

for letter in collection:
    print(letter)
```

Ce que nous verrons ne pouvant être exaustif python étant un langage avec
une bibliothèque de fonctions et de modules très fournie je vous recommande
de vous familiariser avec la documentation du langage.
Disponible à cette adresse:
https://docs.python.org/3/index.html

Dans notre cas c'est cette partie qui s'avèrera salvatrice:
https://docs.python.org/3/library/index.html

Cela peut paraitre parfois fastidieux mais savoir utiliser de la
documentation vous rends vraiment indépendant. (imaginez un monde sans StackOverflow...)

## 2.2.1: Les chaines de caractères

Documentation associée:
https://docs.python.org/3.4/tutorial/introduction.html#strings

A venir

## 2.2.2: Les Listes

Documentation associée:
https://docs.python.org/3.4/tutorial/introduction.html#lists
et
https://docs.python.org/3.4/tutorial/datastructures.html#more-on-lists


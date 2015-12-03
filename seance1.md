# Séance 0: Fondamentaux en algorithmique.

## Exercice 0: L'interpréteur Python et expressions arithmétiques

### 0.0: Exécuter python

Lancer un terminal sur votre poste de travail.
Lancer l'interpréteur de commande Python3 dans votre terminal.
```shell
> python3
```

### 0.1: Arithmétique basique

Découvrir les expressions arithmétiques de bases sur des nombres réels.
- Addition: `+`
- Soustraction: `-`
- Multiplication: `*`
- Division: `/`
- Division entière: `//`
- Modulo(reste de la division entière): `%`

Faire quelques calculs basiques dans l'interpréteur tel que:
```python
>>> 2 * 2
4
>>> 1 / 2
0.5
>>> 1 + 1
2
>>> 9 - 10
-1
>>> 3 % 2
1
```

### 0.2: Variables

Une variable est une valeur à laquelle on a donner un nom. Afin de ne pas avoir
à la recalculer et aussi afin d'abstraire les détails décrier son calcul.

Attention ce n'est pas le “ = ” mathématique!

On *assigne* une valeur à une variable de la façon suivante:
```python
>>> a = 5

```

Expérimentez dans votre interpréteur en nommant différents calculs fait
précédemment.

Exemple:
```python
>>> a = 2 + 2
>>> a
4
```
### 0.2: Logique booléenne
#### 0.2.1: Introduction

Une valeur booléenne vaut soit Vrai soit Faux. En Python on utilisera `True` et
`False`.

```Python
>>> True
True
>>> False
False
```
Grâce à la logique booléenne on peut exprimer des expressions plus ou moins
complexes.

#### 0.2.2.: Comparaisons arithmétiques

Il existe des opérateurs pour comparer des entiers tels que:
```python
>>> 5 > 2
True
>>> 2 < 5
True
>>> 3 >= 3
True
>>> 3 <= 2
False
>>> 2 == 5 # On note que l'ont utilise un double = et non un simple.
False
>>> 2 != 5
True
>>> a = 10
>>> b = 20
>>> a == b
False
```

Expérimentez dans votre terminal quelques expressions pour comparer des entiers
à des entiers puis avec des variables.

#### 0.2.3: Opérateurs logiques

Vous allez me dire "C'est bien pour l'instant ça ne diffère pas d'une
calculette". Et bien c'est vrai avant tout un ordinateur sait faire ce qu'une
calculette fait.

Cependant avec de la logique booléenne et plus tard les fonctions et structures
de données on verra que l'ont peut faire bien plus.

Les opérateurs logiques sont:
- le “Et” dit “la conjonction” noté `and` en python.
- le “Ou inclusif” dit “l'union” noté `or` en python.
- le “non” dit “négation” noté `not` en python.
Il en existe d'autres mais ils sont implémente à partir de ces trois
fondamentaux.

L'opérateur `and` désigne le “et” logique parfois noté ”∧”.
```Python
>>> False and False
False
>>> False and True
False
>>> True and False
False
>>> True and True
True
```

L'opérateur `or` désigne le “ou” logique parfois noté “∨”.
```python
>>> False or False
False
>>> False or True
True
>>> True or False
True
>>> True or True
True
```
Et l'opérateur `not` désigne le “non” logique noté parfois “¬” dans la
littérature.

```python
>>> not True
False
>>> not False
True
```

#### 0.2.4: Application

Exercice écrire expression booléenne qui permet d'avoir le même résultat qu'en
utilisant l'opérateur `!=`.

Indices: il vous faudra deux variables a et b ensuite plusieurs solutions
s'offrent à vous.

```python
>>> a = 5 # La valeur que vous voulez par exemple 5.
>>> b = 10 # pareil mettez le nombre que vous souhaitez.
>>> # ici votre expression booleenne qui mime le comportement de !=.
```

### 0.3: Conditionnelles
#### 0.3.1: `if`

Pour l'instant les lignes de codes que vous avons écrites étaient très simples.
Et très linéaire. Hors une des caractéristiques des machines programmables c'est
qu'elles peuvent suivre un programme en fonction de conditions logiques.

Pour cela il existe des mots clefs dans le langage tels que le mot clef `if`.
et `else`.

Le `if` qui correspond au si en français. Est une condition qui si elle est vrai
conduit à l'exécution du code dans le bloc suivant.
Le `else` lui exécute son bloc si la condition du si n'est pas satisfaite. Tout
`if` n'est pas obligé de comporter un `else`.

```python
>>> a = 10
>>> if a > 10:
...    'A est superieur à 10.'
... else:
...    'A est inferieur ou égal à 10.'
est inferieur ou égal à 10.
```

En python nous sommes obliger d'intenter nos programmes par 4 espaces. Car
l'indentation symbolise les "blocs" de nos programmes.

A partir de maintenant nous Allons écrire nos programmes dans un fichier avec
l'extension `.py` et les exécuter de la manière suivante:

Pour tester recopiez ou copiez collez le code suivant dans un fichier Hello.py
et exécutez le de la manière suivante.

```python
import os
user = os.environ['USER']
print('Hello ' + user + '!') # Affiche dans votre terminal la chaine résultante.
```

Ces trois lignes peuvent vous sembler bien complexes mais ne vous inquiétez pas
nous y reviendrons. Elles font appels à des "fonctions" tel que `print` que nous
allons utilisez dans l'application. Nous verrons ce concept en détail juste après.

Toujours est-il que print vous permet d'écrire dans votre terminal. Ce qui
permet d'afficher le résultat de votre programme ou son avancement. Ou débugger
de façon très sommaire.

```shell
> python3 hello.py
Hello <votre login>
```

### 0.3.1: Application

Rédiger un programme qui affiche `"C'est un nombre pair"` quand un nombre est
multiple de 2 c'est à dire pair.
Et `"C'est un nombre impair"` sinon.

Indice il vous faudra faire appel à l'opérateur modulo `%`. Et utiliser un if.
Utiliser `print` de la manière suivante: `print("mon message").


# L'interpréteur Python

L'interpréteur (aussi appelé « REPL » (« Read-Eval-Print-Loop ») ou « toplevel »)
Python nous permet de saisir directement des expressions, donc Python nous donne
la valeur.

Lancons Python en tapant dans votre interpreteur de commande (shell):

```Shell
$ python
```

Une ligne commençant par un « $ » représente une commande à taper dans votre
terminal. Sans le « $ ». Python nous indique qu'il attend un programme avec
« >>> ». Si à n'importe quel moment on veut s'en aller, il suffit de taper
Ctrl-D quand Python nous présente cette invite.

Dans ce doucment, le code Python à donner à l'interpréteur est situé après les
« >>> » (pour imiter le « prompt » de l'interpréteur, à ne pas recopier,
évidemment... ). La ligne en-dessous représenter la valeur que l'interpréteur
devrait répondre :

```Python
>>> Ceci est le texte à donner à Python
```
Ceci est ce que répond Python. (en l'occurence, il ne répondrait pas ça, il vous
dirait qu'il ne comprend rien du tout)

```Python
>>> # Ceci est un commentaire !
>>> # Python ignore les lignes qui commencent par un '#'
>>> # Du coup, il ne dit rien du tout... :(
```

Une expression est un morceau de code qui représente une valeur. Par exemple
du texte :

```Python
>>> "Bonjour, Python :)"
Bonjour, Python :)
```

# Expressions arithmétiques

## Operations usuelles

Un nombre est une valeur.

```Python
>>> 5
5
```

Le morceau de code Python « 5 » a pour valeur 5.
« 5 » est donc une expression, dont la valeur est le nombre 5.

Une expression « arithmétique » est une expression dont la valeur est un nombre.
L'ordinateur est avant tout une très rapide machine à calculer.

On dispose de tous les autres opérateurs habituels :

### Addition

```Python
>>> 5 + 3
8
```

`5 + 3` est une expression dont la valeur est le résulat du calcul.

### Soustraction

```Python
>>> 5 - 3
2
```

### Multiplication

```Python
>>> 5 * 3
15
```

### Division sur les entiers.

Note: L'opérateur `//` réalise une division d'entiers. (Renvoie le
« quotient »). On peut forcer un résultat d'exact en indiquant à Python que les
opérandes sont des nombres réels :

```Python
>>> 5 // 3
1
```

### Division sur les Réels

L'opérateur `/` réalise une division de noms réels. Renvoie le nombre en
précision dite "flotante".

```Python
>>> 5 / 4
1.25
```

## Expressions composées

Les opérateurs ne marchent pas que sur les nombres. Ils marchent avec n'importe
quelle expression et produisent une nouvelle expression (dont la valeur est une
nouvelle valeur). On peut les emboîter à l'infini :

```Python
>>> 5 + 4 + 3 + 2 + 1
15
>>> 5 + 3 * 2
11
>>> (5 + 3) * 2
16
```

# Variables

Comme en mathématiques : on peut donner un nom à une valeur, pour éviter de devoir la re-calculer,
et de la ré-écrire, et aussi s'abstraire de ce qu'elle contient vraiment !

```Python
>>> a = 5
```

Attention, ce n'est pas le  `=` des mathématiques. On pose une nouvelle
définition : « Soit a un nombre dont la valeur est 5 »

Python ne répond rien, mais il a compris quand même, sinon il l'aurait dit !
Vérifions.

```Python
>>> # Python, combien vaut a ?
>>> a
5
```

Merci Python. `a` est une *variable*. Dans le cas général, on ne connait pas
sa valeur à l'avance. Parce qu'elle sera donnée par l'utilisateur du programme,
par exemple.

Au passage, le nom d'une variable (comme « a »), est une... expression. Dont
la valeur est la valeur que nous avons donnée à la variable.

Du coup, il faut pouvoir exprimer des valeurs qui *dépendent* de cette variable
sans se référer à sa valeur.

```Python
>>> a + 1
6
```

Encore une expression ! Rappel : une expression est une nouvelle valeur. On
vient d'exprimer comment construire le nombre égal à la valeur de `a` plus 1.
`a` n'a pas été modifiée :

```Python
>>> a
5
>>> b = 2
>>> a + b
7
```

Python permet tout de même de modifier la valeur d'une variable. Il suffit...
de lui donner une nouvelle valeur. On appelle ça « ré-affecter » ou
« ré-assigner », ou encore « muter » la variable.

On appelle ça de la *mutabilité*. On dit que Python est un langage *impératif* car il permet cela.  Derrière, l'ordinateur va écrire dans la mémoire.

```Python
>>> a = 5
>>> a
5
>>> b = 2
>>> a + b
7
>>> a = 6
>>> a
6
>>> a + b
8
```

# Logique booléenne.

Un booléen est une valeur binaire. « Vrai » ou « Faux ». En Python, on écrit
`True` et `False`.

```Python
>>> True
True
>>> False
False
```

On peut du coup exprimer des comparaisons entre nos expression :

```Python
>>> a = 5
>>> # Python, est-ce que a est égal à 5 ?
>>> a == 5
True
>>> a = 6
>>> Très bien, et maintenant ?
>>> a == 5
False
```

Logique. On note que pour tester l'égalité, on utilise un double égal, `==`,
pour le différencier du simple égal `=` qui sert à définir une variable. Les
autres opérateurs de comparaison ?

```Python
>>> a < 6
False
>>> a <= 6
True
>>> a > 3
True
>>> a >= 3
True
>>> 3 < a
True
>>> 3 != a
True
```

Le `!=` veut dire « différent de », ou « non-égal ». Il ressemble au « ≠ » des
mathématiques. Si si, un peu quand même...

## And

L'opérateur `and` correspond au ET logique. a ET b est vrai si et seulement si
a est vrai ET QUE b est vrai aussi.

```Python
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True and True
True
```

## Or

De la même façon, a OU b est vrai si a est vrai OU ALORS si b est vrai. Cela
s'appelle le OU logique. En Python, on écrit cela `or`.

```Python
>>> False or False
False
>>> True or False
True
>>> False or True
True
>>> True and True
True
```

## Not

Le NON, noté `not`, donne l'inverse (pour être précis, on appelle ça la
« négation ») d'un booléen :

```Python
>>> not True
False
>>> not False
True
>>> not not True
True
>>> not not False
False
```

Sans blagues.

# Conditionnelles

Pour l'instant, nous n'avons effectué que des calculs purement linéaires. Pour
apprendre à l'ordinateur à faire des choses complexes, il faut pouvoir être
capable de lui demander de faire des choses différentes en fonction du cas qu'il
a traîter.
C'est la caractéristique fondamentale d'une machine programmable : effectuer un
choix basé sur une condition.

```Python
>>> if a == 5:
...     "yep."
...
yep.
```

Après le mot `if` on doit mettre une expression qui va renvoyer un booléen.
Si le booléen est `True`, on fait quelque chose. Sinon, eh bien, on ne fait
rien... Sauf si...

```Python
>>> if a == 3:
...     "yep."
... else:
...     "nop."
...
nop.
```

Python veut impérativement que ce qui est à « l'intérieur » d'un `if` ou d'un
`else` soit *indenté*, c'est à dire en avance par rapport au reste du
programme. Il se fiche de combien, pourvu que ce soit indenté. Par conviention,
c'est souvent quatre espaces.

Tout ceci commence à devenir fort intéressant mais aussi fort pénible, taper
4 espaces dans son terminal, ce n'est pas pratique... Ouvrons l'éditeur de
fichiers.

# Fonctions

Voici un programme Python simple :

```Python
a = 5
if a == 5:
    "yep."
else:
    "nop."
```

Ici on commence à écrire des programmes en dehors de notre interpréteur, c'est à
dire dans des fichiers. On notera l'absence des `>>>` et des `...`. Cependant le
contenu reste le même.

Lançons le programme :

```Shell
$ python monfichier.py
```

Rien. Python est devenu moins bavard. En mode non-intéractif, il n'affiche pas
la valeur de toutes les expression. Alors comment faire ? On lui demande
explicitement d'afficher une valeur :

```Python
print("La valeur de a est :")
print(a)
```

`print` est une *fonction*. Une fonction est un programme que quelqu'un a
écrit, et qui porte un nom, pour qu'on puisse le ré-utiliser. `print` a été
écrit par les gens qui ont fait Python, et il fait appel à du code très
compliqué pas de votre niveau pour pouvoir écrire à l'écran.

```Shell
$ python monfichier.py
La valeur de a est :
5
```

Super. Nous aussi on veut écrire nous propres fonctions :

```
def une_fonction():
    print("Hello, world")

une_fonction()
```
```Shell
python ma_premiere_fonction.py
Hello World
```

Une fonction peut faire plusieurs choses. Quand elle a fini, le programme
reprend où il en était avant qu'on lance la fonction :

```Python
def une_autre_fonction():
    print("allo ?")
    print("allooooooo ?")
    print("au revoir.")

print("bonjour.")
une_autre_fonction()
print("zut, ça a coupé")
```

```Shell
bonjour.
allo ?
allooooooo ?
au revoir.
zut, ça a coupé
```

Une fonction est un programme. Un programme est une description d'un traîtement
automatique de données. En conséquence, il faut pouvoir donner à la fonction des
données avec lesquelles travailler.

```Python
def somme(a, b):
    print(a + b)

somme(1, 2) # Affiche 3
```

Cette fonction prend 2 valeurs avec lesquelles travailler. On appelle ça les
*paramètres* de la fonction. Le premier s'appelle `a`, et le deuxième
s'appelle `b`. Ce sont des variables qui n'existent qu'à « l'intérieur » de
la fonction.

Quand on appelle la fonction, on lui donne les données dans l'ordre. Mais on
peut aussi les désigner par leur nom, et les mettre dans le désordre :

```Python
somme(b = 0, a = 1)
1
```

Une fonction peut évidemment nous retourner quelque chose qu'elle a calculé,
plutôt que de simplement l'afficher.

```Python
def somme(a, b):
    return a + b
```

`return a` signifie basiquement « arrête-toi, et retourne où tu en étais avec
la valeur a.

```Python
a = somme(1, 2)
print(a) # Affiche 3
```

On voit donc qu'un appel de fonction est une... expression ! Un bout de code qui
a une valeur... on l'occurence, la valeur de « somme(1, 2) » est la valeur que
la fonction va donner à « return » quand elle aura terminé ses calculs. Du coup,
on peut refaire la même chose qu'avant pour afficher le résultat, en combinant
les appels de fonction :

```Python
>>> print(somme(0, 1)) # Affiche 1
```

Mais au moins, maintenant, on a le choix. Plutôt que de bêtement l'afficher, on
peut aussi stocker le résultat dans une variable, le passer à une autre fonction
(ou un opérateur), tester sa valeur, etc. C'est la force d'une *syntaxe
d'expression*. Et encore, celle de Python reste assez limitée.

Dernier détail pour cette partie, que se serait-il passé si on avait stocké le
résultat de nos fonctions sans `return` ?

```Python
def ma_fonction():
    print("eeyup.")

a = ma_fonction()
print(a) # Affiche None
```

La fonction renvoie quand même une valeur, la valeur `None`, pour « pas de
valeur ». Si on tape une expression renvoyant `None` dans l'interpréteur,
Python ne l'affiche pas, contrairement aux nombres ou au texte, par exemple,
sauf si on le lui demande explicitement avec `print`.
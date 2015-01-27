# 1. L'interpréteur Python

L'interpréteur (aussi appelé « REPL » (« Read-Eval-Print-Loop ») ou « toplevel »)
Python nous permet de saisir directement des expressions, donc Python nous donne
la valeur.

Lancons Python en tapant dans votre interpréteur de commandes (« shell ») :

```shell
$ python
```

Une ligne commençant par un « $ » représente une commande à taper dans votre
terminal. Sans le « $ ». Python nous indique qu'il attend un programme avec
« >>> ». Si à n'importe quel moment on veut s'en aller, il suffit de taper
Ctrl-D quand Python nous présente cette invite.

Dans ce doucment, le code Python à donner à l'interpréteur est situé après les
« >>> » (pour imiter le « prompt » de l'interpréteur, à ne pas recopier,
évidemment... ). La ligne en-dessous représenter la valeur que l'interpréteur
devrait répondre :

```python
>>> Ceci est le texte à donner à Python
Ceci est ce que répond Python.
```

En l'occurence, il ne répondrait pas ça, il vous dirait qu'il ne comprend rien du tout.

```python
>>> # Ceci est un commentaire !
>>> # Python ignore les lignes qui commencent par un '#'
>>> # Du coup, il ne dit rien du tout... :(
```

Une expression est un morceau de code qui représente une valeur. Par exemple
du texte :

```python
>>> "Bonjour, Python :)"
Bonjour, Python :)
```

# 2. Expressions arithmétiques

Un nombre est une valeur.

```python
>>> 5
5
```

Le morceau de code Python « 5 » a pour valeur 5.
« 5 » est donc une expression, dont la valeur est le nombre 5.

Une expression « arithmétique » est une expression dont la valeur est un nombre.
L'ordinateur est avant tout une très rapide machine à calculer.

```python
>>> 5 + 3
8
```

`5 + 3` est une expression dont la valeur est le résulat du calcul.
On dispose de tous les autres opérateurs habituels :

```python
>>> 5 - 3
2
>>> 5 * 3
15
>>> 5 / 4
1.25
```

Note : L'opérateur `/` réalise une division sur les nombres réels. On peut à la
place utiliser l'opérateur `//` pour indiquer à Python de faire une divison
d'enteirs (renvoie le « quotient »).

```python
>>> 5 // 3
1
```

Les opérateurs ne marchent pas que sur les nombres. Ils marchent avec n'importe
quelle expression et produisent une nouvelle expression (dont la valeur est une
nouvelle valeur). On peut les emboîter à l'infini :

```python
>>> 5 + 4 + 3 + 2 + 1
15
>>> 5 + 3 * 2
11
>>> (5 + 3) * 2
16
```

# 3. Variables

Comme en mathématiques : on peut donner un nom à une valeur, pour éviter de devoir la re-calculer,
et de la ré-écrire, et aussi s'abstraire de ce qu'elle contient vraiment !

```python
>>> a = 5
```

Attention, ce n'est pas le  `=` des mathématiques. On pose une nouvelle
définition : « Soit a un nombre dont la valeur est 5 »

Python ne répond rien, mais il a compris quand même, sinon il l'aurait dit !
Vérifions.

```python
>>> # Python, combien vaut a ?
>>> a
5
```

Merci Python. `a` est une *variable*. Dans le cas général, on ne connait pas
sa valeur à l'avance. Parce qu'elle sera donnée par l'utilisateur du programme,
par exemple.

Au passage, le nom d'une variable (comme « a »), est une... expression. Dont
la valeur est la valeur que nous avons donnée à la variable.

Du coup, il faut pouvoir exprimer des valeurs qui *dépendent* de cette variable
sans se référer à sa valeur.

```python
>>> a + 1
6
```

Encore une expression ! Rappel : une expression est une nouvelle valeur. On
vient d'exprimer comment construire le nombre égal à la valeur de `a` plus 1.
`a` n'a pas été modifiée :

```python
>>> a
5
>>> b = 2
>>> a + b
7
```

Python permet tout de même de modifier la valeur d'une variable. Il suffit...
de lui donner une nouvelle valeur. On appelle ça « ré-affecter » ou
« ré-assigner », ou encore « muter » la variable.

On appelle ça de la *mutabilité*. On dit que Python est un langage *impératif*
car il permet cela.  Derrière, l'ordinateur va écrire dans la mémoire.

```python
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

# 4. Logique booléenne.

Un booléen est une valeur binaire. « Vrai » ou « Faux ». En Python, on écrit
`True` et `False`.

```python
>>> True
True
>>> False
False
```

On peut du coup exprimer des comparaisons entre nos expression :

```python
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

```python
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

Le `!=` veut dire « différent de », ou « non-égal ». Il ressemble au « ≠ » des
mathématiques. Si si, un peu quand même...

L'opérateur `and` correspond au ET logique. a ET b est vrai si et seulement si
a est vrai ET QUE b est vrai aussi.

```python
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> True and True
True
```

De la même façon, a OU b est vrai si a est vrai OU ALORS si b est vrai. Cela
s'appelle le OU logique. En Python, on écrit cela `or`.

```python
>>> False or False
False
>>> True or False
True
>>> False or True
True
>>> True and True
True
```

Le NON, noté `not`, donne l'inverse (pour être précis, on appelle ça la
« négation ») d'un booléen :

```python
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

# 5. Conditionnelles

Pour l'instant, nous n'avons effectué que des calculs purement linéaires. Pour
apprendre à l'ordinateur à faire des choses complexes, il faut pouvoir être
capable de lui demander de faire des choses différentes en fonction du cas qu'il
a traîter.
C'est la caractéristique fondamentale d'une machine programmable : effectuer un
choix basé sur une condition.

```python
>>> if a == 5:
...     "yep."
...
yep.
```

Après le mot `if` on doit mettre une expression qui va renvoyer un booléen.
Si le booléen est `True`, on fait quelque chose. Sinon, eh bien, on ne fait
rien... Sauf si...

```python
>>> if a == 3:
...     "yep."
... else:
...     "nop."
...
nop.
```

Python veut impérativement que ce qui est à « l'intérieur » d'un `if` ou d'un
`else` soit *indenté*, c'est à dire en avance par rapport au reste du
programme. Il se fiche de combien, pourvu que ce soit indenté. Par conviention,
c'est souvent quatre espaces.

Tout ceci commence à devenir fort intéressant mais aussi fort pénible, taper
4 espaces dans son terminal, ce n'est pas pratique... Ouvrons l'éditeur de
fichiers.

# 6. Fonctions

Voici un programme Python simple :

```python
a = 5
if a == 5:
    "yep."
else:
    "nop."
```

À partir de maintenant, on écrira les programmes dans des fichiers, en dehors de
notre interpréteur. On notera l'absence des `>>>` et des `...`, mais le langage
reste le même : Tous ces exemples peuvent également être copiés directement dans
l'interpréteur.

Lançons le programme :

```shell
$ python monfichier.py
```

Rien. Python est devenu moins bavard. En mode non-intéractif, il n'affiche pas
la valeur de toutes les expression. Alors comment faire ? On lui demande
explicitement d'afficher une valeur :

```python
print("La valeur de a est :")
print(a)
```

`print` est une *fonction*. Une fonction est un programme que quelqu'un a
écrit, et qui porte un nom, pour qu'on puisse le ré-utiliser. `print` a été
écrit par les gens qui ont fait Python, et il fait appel à du code très
compliqué^W^W pas de votre niveau pour pouvoir écrire à l'écran.

```shell
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

```shell
$ python monfichier.py
Hello World
```

Une fonction peut faire plusieurs choses. Quand elle a fini, le programme
reprend où il en était avant qu'on lance la fonction :

```python
def une_autre_fonction():
    print("allo ?")
    print("allooooooo ?")
    print("au revoir.")

print("bonjour.")
une_autre_fonction()
print("zut, ça a coupé")
```

```shell
bonjour.
allo ?
allooooooo ?
au revoir.
zut, ça a coupé
```

Une fonction est un programme. Un programme est une description d'un traîtement
automatique de données. En conséquence, il faut pouvoir donner à la fonction des
données avec lesquelles travailler.

```python
def somme(a, b):
    print(a + b)

somme(1, 2) # affiche 3
```

Cette fonction prend 2 valeurs avec lesquelles travailler. On appelle ça les
*paramètres* de la fonction. Le premier s'appelle `a`, et le deuxième
s'appelle `b`. Ce sont des variables qui n'existent qu'à « l'intérieur » de
la fonction.

Quand on appelle la fonction, on lui donne les données dans l'ordre. Mais on
peut aussi les désigner par leur nom, et les mettre dans le désordre :

```python
somme(b = 0, a = 1) # affiche 1
```

Une fonction peut évidemment nous retourner quelque chose qu'elle a calculé,
plutôt que de simplement l'afficher.

```python
def somme(a, b):
    return a + b
```

`return a` signifie basiquement « arrête-toi, et retourne où tu en étais avec
la valeur a.

```python
a = somme(1, 2)
print(a) # affiche 3
```

On voit donc qu'un appel de fonction est une... expression ! Un bout de code qui
a une valeur... on l'occurence, la valeur de « somme(1, 2) » est la valeur que
la fonction va donner à « return » quand elle aura terminé ses calculs. Du coup,
on peut refaire la même chose qu'avant pour afficher le résultat, en combinant
les appels de fonction :

```python
print(somme(0, 1)) # affiche 1
```

Mais au moins, maintenant, on a le choix. Plutôt que de bêtement l'afficher, on
peut aussi stocker le résultat dans une variable, le passer à une autre fonction
(ou un opérateur), tester sa valeur, etc. C'est la force d'une *syntaxe
d'expression*. Et encore, celle de Python reste assez limitée.

Dernier détail pour cette partie, que se serait-il passé si on avait stocké le
résultat de nos fonctions sans `return` ?

```python
def ma_fonction():
    print("eeyup.")

a = ma_fonction()
print(a)
```

```shell
None
```

La fonction renvoie quand même une valeur, la valeur `None`, pour « pas de
valeur ». Si on tape une expression renvoyant `None` dans l'interpréteur,
Python ne l'affiche pas, contrairement aux nombres ou au texte, par exemple,
sauf si on le lui demande explicitement avec `print`.

# 7. La récursion

On va maintenant écrire de vraies fonctions. De vraies programmes. On rappelle
que le but d'un programme, c'est de résoudre un problème de façon mécanique en
le découpant en une suite de problèmes plus simples, que quelqu'un de
complètement idiot (au hasard, un ordinateur... ) pourrait effectuer 
automatiquement sans avoir aucune idée de ce qu'il est en train de faire, mais
en fournissant tout de même un résultat correct /in fine/.

Commençons sans trop d'ambition. Par exemple, on pourrait écrire un programme
(une fonction...) qui étant donné un nombre nous dit s'il est pair ou pas.

Il existe une façon évidente de faire cela. Un entier est pair si et seulement
si il est divisible par deux, c'est à dire si le reste dans la division de cet
entier par deux est zéro. En Python, l'opérateur « % » (ou « modulo ») sert à
ça.

```python
>>> # Dans l'interpréteur...
>>> 5 % 2
1
>>> 4 % 2
0
```

Ceci nous donne une version facile de la fonction :

```python
def est_pair(a):
    if a % 2 == 0:
        return True
    else 
        return False
```

Ce n'est pas très joli. On peut mieux faire :

```python
def est_pair(a):
    return a % 2 == 0
```

La valeur de cette expression est déjà celle que nous avons besoin de renvoyer.
`True` si le nombre est pair, `False` sinon.

Bien, cela nous a permis de pratiquer un peu les fonctions, d'en écrire une qui
correspond à un petit problème concret, et de voir qu'il existe parfois plusieurs
façons, plus ou moins jolies, d'écrire des programmes. La dernière version est
très bien. Jolie, efficace, tout ce qu'il faut.

Mais elle ne m'intéresse pas pour vous apprendre ce que je veux vous apprendre.
À savoir, la façon de penser du programmeur. Comment un programmeur, confronté
à la résolution d'un problème, s'y prend pour le découper en étapes simples. Une
des techniques les plus utilisées, les plus omniprésentes dans tous les domaines
de l'informatique est la *récursion*.

La récursion consiste à trouver un cas pour lequel notre problème est trivial.
Ensuite, comme on ne peut pas gérer tous les cas, pour tous les autres, on
essaie de se ramener d'une manière ou d'une autre à un cas trivial.

Wow. Tout ça est très vague. Un exemple avec la fonction `est_pair`.

* Ce qui est sûr, c'est que 1 est impair.
* Dire qu'un nombre N est pair, c'est comme dire que N - 1 est impair.
* Dire que N - 1 est impair, c'est comme dire que N - 2 est pair.
* Dire que N - 2 est pair, c'est comme ...
* ...

Et on descend comme ça. Fatalement, suivant le nombre originel, on finira par
devoir dire si 1 est pair ou impair. Et ça, c'est plutôt facile ! On n'a plus
qu'à remonter pour dire si notre nombre était pair ou impair.

On va donc résoudre le même problème, mais avec des données de plus en plus
simples, jusqu'à ce qu'elles soient si simples que le problème devient trivial.

Voici ce que ça donnerait en Python :

```python
def est_pair(a):
    if a == 1:
        # si a est 1, la question ne se pose pas...
        return False
    else:
        # est ce que a est pair ? bon, voyons si a est impair...
        # rappel, la négation de est_pair(a) est... !est_pair(a)
        return !est_pair(a - 1)
```

Et voici comment un programmeur résoud un problème de façon *récursive*. En
tàchant de ramener tous les cas compliqués à un cas plus simple du même probleme.
Bien entendu, la version d'au-dessus, en utilisant le modulo, était à la fois
plus simple, plus jolie, et plus performante. On ne fait qu'une opération, au
lieu de devoir se balader dans tous les nombres de « n » jusqu'à un...
Mais cette solution nous a permis de découvrir la pensée récursive qui nous sera
très utile pour des problèmes plus complexes.

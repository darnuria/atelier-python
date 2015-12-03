#!/usr/bin/python

inf = int(input("borne inférieure: "))
sup = int(input("borne supérieure: "))
n = int(input("nombre à tester: "))

if ((n > inf) and (n < sup)):
    print(True)
else:
    print(False)

# Version encore plus simple:
print((n > inf) and (n < sup))

# Version ENCORE plus simple valide en python:
print(inf < n < sup)

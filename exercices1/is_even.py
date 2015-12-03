#!/usr/bin/python3

a = int(input("Donnez un nombre: "))
if ((a % 2) == 0):
    print(True)
else:
    print(False)

# Version plus simple:
print((a % 2 == 0))

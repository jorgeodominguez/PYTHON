#Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
import os

os.system("cls")

lista=[100,123,456,222,999,895,325,234,322,988]

print(f"El primer elemento de la lista {lista[0]}")
print(f"\nEl ultimo elemento de la lista {lista[-1]}")
print(f"\nEl 5 elemento de la lista {lista[4]}")
print(f"\nLos elementos de la lista entre 2 y 5 {lista[2:4]}")
print(f"\nLos elementos del inicio al 4 {lista[:4]}")
print(f"\nLos elementos del 4 al final {lista[3:]}")
print(f"\nLos ultimos 3 elementos {lista[-3:]}")
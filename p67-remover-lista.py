#Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
import os

os.system("cls")

lista=[100, 123, 456, 222, 999, 895, 325, 234, 322, 988]

print(f"Lista original: {lista}")
del lista[0:3]
lista.remove(322)
lista.remove(988)
eli=lista.pop(0)
print(f"\nRemover y mostrar: {lista} - {eli}")
eli=lista.pop()
print(f"\nRemover y mostrar: {lista} - {eli}")

print(f"\nLista modificada: {lista}")
lista.clear()
print(f"\nLista: {lista}")
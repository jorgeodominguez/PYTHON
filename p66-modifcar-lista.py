#Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988.
import os

os.system("cls")

lista=[100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
print(f"Lista Original: {lista}")
lista[0]=200
lista[4]=1000
lista[-1]=999
lista[1:4]=[555,666,777]
print(f"Lista Modificada: {lista}")
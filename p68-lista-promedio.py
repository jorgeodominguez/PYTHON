#Crear un programa que permita procesar una lista de n números enteros, de acuerdo a lo siguiente:

import os

os.system("cls")

l=[]
c=int(input("Cuantos Numeros: "))

for i in range(c):
    n=int(input(f"dame el numero {i+1}: "))
    l.append(n)

print(f"\nMostrar toda la lista; {l}")

print("\nIterar lista ")
sum=0
pro=0
for i in range(len(l)):
    print(l[i])
    sum=l[i]+sum
    pro=sum/len(l)

print(f"\nLa suma de los {c} elementos es: {sum}")
print(f"\nEl promedio de los {c} elementos es: {pro}\n")
#Se tienen los datos de nombres y sueldos de los siguientes trabajadores, en dos listas:

import os
os.system('cls')

nombres=['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']

sueldos=[4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

trabajadores=dict(zip(nombres,sueldos))

print(f"\n Mostrar Diccionario: {trabajadores}")

print("\nLas llaves: ")
for k in trabajadores.keys():
    print(k,end=" ")

print("\nLos valores: ")
for v in trabajadores.values():
    print(v,end=" ")

sum=0
pro=0
print("\nDiccionario completo: ")
for k,v in trabajadores.items():
    print(f'{k:<10} : {v}')
    sum=sum+v
    pro=sum/len(trabajadores)

print(f"\nLa suma de los sueldos es {sum}")
print(f"\nEl promedio de los sueldos es {pro}")
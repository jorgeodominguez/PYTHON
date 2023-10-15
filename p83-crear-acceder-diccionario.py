#Crear un diccionario de llave numérica dias, con los siguientes elementos:

import os
os.system('cls')

dias={
    1:'Lunes',
    2:'Martes',
    3:'Miercoles',
    4:'Jueves',
    5:'Viernes',
    6:'Sabado',
    7:'Domingo'
}

print(f"\nDiccionario: {dias}")

print(f"\nEl primero elemento: {dias[1]}")
print(f"\nEl Ultimo elemento: {dias[7]}")
print(f"\nEl 5 elemento con get: {dias.get(5)}")
print(f"\nEl 7 elemento con get: {dias.get(7)}")

print("\nDiccionario completo: ")
for k,v in dias.items():
    print(f'{k:<1} : {v}')

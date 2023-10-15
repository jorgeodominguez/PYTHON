#Crear un diccionario de llave de cadena, ventas, con los siguientes elementos:

import os
os.system('cls')

ventas={
    'Juan':1550,
    'Jose':2600,
    'Maria':2220
}

print(f"\n Mostrar Diccionario: {ventas}")

ventas['Rocio']=2500
ventas['Mateo']=1567
ventas.update({'Andrea':9567})
ventas.update({'Miguel':1234})




print("\nDiccionario completo: ")
for k,v in ventas.items():
    print(f'{k:<10} : {v}')
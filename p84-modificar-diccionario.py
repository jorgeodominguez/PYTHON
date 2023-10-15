#Crear un diccionario de llaves de cadena países, con los siguientes elementos:

import os
os.system('cls')

paises={
    'Argentina':100,
    'Brasil':200,
    'Colombia':300,
    'Chile':400,
    'Ecuador':500,
    'Bolivia':600,
    'Jamaica':700
}

print(f"\nDiccionario: {paises}")

paises['Brasil']=250
paises['Chile']=450
paises.update({'Bolivia':650})
paises.update({'Jamaica':750})


print("\nDiccionario completo: ")
for k,v in paises.items():
    print(f'{k:<10} : {v}')

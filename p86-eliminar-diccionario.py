#Cree un diccionario de llave de cadena municipios con los siguientes elementos:

import os
os.system('cls')

municipios={
    'Apozol':1863,
    'Calera':1868,
    'Fresnillo':1554,
    'Guadalupe':1821,
    'Jalpa':1824,
    'Jerez':1824,
    'Loreto':1931,
    'Mazapil':1824,
    'Momax':1857
}

print(f"\n Mostrar Diccionario original: {municipios}")

del municipios['Apozol']
municipios.pop('Fresnillo')
municipios.popitem()

print("\nDiccionario completo: ")
for k,v in municipios.items():
    print(f'{k:<10} : {v}')

municipios.clear()

print(f"\n Mostrar Diccionario: {municipios}")

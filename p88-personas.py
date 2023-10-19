#personas

import os
os.system('cls')

A={'Juan', 'Maria', 'Pedro', 'Jose', 'Rocio'}
B={'Pedro', 'Juan', 'Pablo', 'Mateo', 'Esther'}
C={'Pablo', 'Mateo'}
D={'Reynaldo', 'Angelica'}

print("Conjunto A:")
print(A)
print("Conjunto B:")
print(B)

print('\nUnion')
print('A union B',A.union(B))

print('\nInterseccion')
print('A Interseccion B',A.intersection(B))

print('\nDiferencia')
print('A Diferencia B',A.difference(B))

print('\nDiferencia simetrica')
print('A Diferencia simetrica B',A.symmetric_difference(B))

print('\nComprobamos subconjunto')
print('Pablo, Mateo subconjunto B',C.issubset(B))

print('\nComprobamos subconjunto')
print('A subconjunto Reynaldo, Angelica',A.issubset(D))

print('\nVerificar')
print('Pedro esta en A','Pedro' in A)

print('\nVerificar')
print('Liliana no esta en B','Liliana' is not B)


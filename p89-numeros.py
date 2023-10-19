#numeros

import os
os.system('cls')

A={50,60,70,80,90,100,200}
B={60,90,100,300,400,500}
C={10,20,60,90,70,100,600,700}

print("Conjunto A:")
print(A)
print("Conjunto B:")
print(B)
print("Conjunto C:")
print(C)

print('\nUnion')
print('A union B',A.union(B))
print('B union C',B.union(C))

print('\nDiferencia')
print('A Diferencia C',A.difference(C))

print('\nDiferencia simetrica')
print('B Diferencia simetrica C',B.symmetric_difference(C))

print('\nInterseccion')
print('B Interseccion C',A.intersection(B))

print('\nComprobamos subconjunto')
print('A subconjunto B',A.issubset(B))

print('\nComprobamos subconjunto')
print('C subconjunto A',C.issubset(A))

print('\nVerificar')
print('100 esta en A',100 in A)

print('\nVerificar')
print('60 esta en A y en B y C',60 in A & B & C)

print('\nVerificar')
print('900 no esta en C',100 is not C)

#nos permite ejemplificar las operaciones logicas sobre conjuntos
import os
os.system('cls')

c1={1,2,3,4,5}
c2={5,6,7,8,9,10}
c3={9,10,11,12,13}
c4={3,4,5}

print(c1,c2,c3,c4)

print('\nUnion')
print('c1 union c2',c1.union(c2))
print('c2 union c3',c2 | c3)

print('\nInterseccion')
print('c1 Interseccion c2',c1.intersection(c2))
print('c2 Interseccion c3',c2 & c3)

print('\nDiferencia')
print('c1 Diferencia c4',c1.difference(c4))
print('c2 Diferencia c3',c2 - c3)

print('\nDiferencia simetrica')
print('c1 Diferencia simetrica c2',c1.symmetric_difference(c2))
print('c2 Diferencia simetrica c3',c2 ^ c3)

print('\Comprobamos subconjunto')
print('c4 subconjunto c1',c4.issubset(c1))
print('c3 subconjunto c2',c3 <= c2)

print('\nVerificar')
print('2 esta en c1',2 in c1)
print('6 no esta en c1',6 is not c1)

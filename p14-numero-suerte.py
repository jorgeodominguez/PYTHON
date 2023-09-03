#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte.

print("Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte.")

anio=int(input("\nDame tu año de nacimiento: "))

numero=str(anio)
uno=numero[-4]
dos=numero[-3]
tres=numero[-2]
cuatro=numero[-1]

suerte=int(uno)+int(dos)+int(tres)+int(cuatro)


print(f"\nTu año de compleaños es {anio}")
print(f"\nTu 1er numero es '{uno}'")
print(f"Tu 2do numero es '{dos}'")
print(f"Tu 3er numero es '{tres}'")
print(f"Tu 4to numero es '{cuatro}'")
print(f"\nTu numero de la suerte es {suerte}\n")

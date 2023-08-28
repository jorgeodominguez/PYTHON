#Calcular el promedio de 3 calificaciones

print("Calcular el promedio de 3 calificacione\n")
print("Dame tres caificaciones separadas por espacio entre ellas\n")
c1, c2, c3 = input().split()
c1, c2, c3 = [float(c1),float(c2),float(c3)]

suma=(c1+c2+c3)
prom=suma/3

print(f"Las calificaciones son {c1},{c2},{c3}, la suma es {suma:.2f} y el promedio es {prom:.2f}")
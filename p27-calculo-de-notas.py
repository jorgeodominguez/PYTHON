#Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir un mensaje de acuerdo al promedio obtenido:

print("Calcular el promedio de 5 calificacione\n")
print("Dame 5 caificaciones separadas por espacio entre ellas\n")
c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = [float(c1),float(c2),float(c3),float(c4),float(c5)]

suma=(c1+c2+c3+c4+c5)
prom=suma/5

if prom>0 and prom<=6:
    print(f"Las calificaciones son {c1},{c2},{c3},{c4},{c5} y el promedio es {prom:.2f} Quedas reprobado")

elif prom>6 and prom<=7:
    print(f"Las calificaciones son {c1},{c2},{c3},{c4},{c5} y el promedio es {prom:.2f} Pasas de panzazo")

elif prom>7 and prom<=8:
    print(f"Las calificaciones son {c1},{c2},{c3},{c4},{c5} y el promedio es {prom:.2f} Muy bien, pues mejorar")

elif prom>8 and prom<=9:
    print(f"Las calificaciones son {c1},{c2},{c3},{c4},{c5} y el promedio es {prom:.2f} Excelente sigue así")

elif prom>9 and prom<=10:
    print(f"Las calificaciones son {c1},{c2},{c3},{c4},{c5} y el promedio es {prom:.2f} Perfecto tu esfuerzo valió la pena")
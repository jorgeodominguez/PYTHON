#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5.

print("\nCaptura de datos para Universidad Kitty Kat SA")

nom=input("Dame el nombre: ")
sex=input("Dame el sexo (H/M): ").upper()
if sex=="M":
    eda=int(input("Dame la edad: "))
    if eda>=21:
        print("Dame tres caificaciones separadas por espacio entre ellas\n")
        c1,c2,c3=input().split()
        c1,c2,c3=[float(c1),float(c2),float(c3)]
        suma=(c1+c2+c3)
        prom=suma/3 
        if prom>=8 and prom<=9.5:
            print(f"\nBienvenida {nom} a la Univercidad cumples con los requisitos")
            print(f"Tu edad {eda}")
            print(f"Tu promedio {prom}")
        else:
            print(f"No cumples con el promedio {nom} se pide entre 8 y 9.5 y tienes {prom}")
    else:
        print(f"No comples con la edad {nom} se piden mayores de 21 y tienes {eda}")

else:
    print(f"{nom} la Univercidad es para MUJERES")

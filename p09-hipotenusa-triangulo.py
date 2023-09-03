#Se desea calcular la hipotenusa de un triángulo rectángulo dadas las longitudes de sus lados.
import math
print("Calcular la hipotenusa de un triangulo rectangulo")

longlado1=float(input("\nIngresa las longitudes del lado 1: "))
longlado2=float(input("Ingresa las longitudes del lado 2: "))

hipotenusa = math.sqrt( longlado1 * longlado1 + longlado2 * longlado2 )

print(f"\nLa Hipotenusa del triango es: {hipotenusa}"
        f"\ncon la longitud de lado 1: {longlado1}, lado 2: {longlado2}\n")
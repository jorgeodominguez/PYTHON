#Se desea calcular el volumen de un cilindro dado su radio y altura.
import math
print("Se desea calcular el volumen de un cilindro dado su radio y altura.")

radio=float(input("\nIngresa el radio: "))
altura=float(input("Ingresa la altura: "))

volumen = math.pi * (radio * radio) * altura

print(f"\nEl volumen del cilindro es: {volumen:.2f}"
        f"\ndado el radio: {radio}, altura: {altura}\n")
# calcula el area de un circulo dado el radio

#importar la libreria de funciones y constantes matematicas
import math 

print("Calculando el area de un circulo \n")

print("Dame el radio: ")
radio = float(input())

#area = 3.1416 * radio * radio
area = math.pi * math.pow(radio,2)

print(f"\nPara un circulo de radio: {radio} El area es: {area:.2f}")
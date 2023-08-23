# Calcula el area de un triangulo dada la base y la altura

import math

print("Calculando el area de un triangulo \n")

print("Dame la base y la altura separados por un Enter: ")
base, altura = int(input()), int(input())

area = (base * altura) / 2

print(f"\nEl triangulo de base {base} y altura {altura} tiene una area de {area:.2f}")
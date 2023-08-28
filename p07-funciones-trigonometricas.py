#Uso de las Funciones trigonometricas en python

import math

print("Calculo de las funciones trigonometricas basicas\n")

angulo=float(input("Dame un angulo en grados: "))
angrad=math.radians(angulo)

seno=math.sin(angrad)
coseno=math.cos(angrad)
tangente=math.tan(angrad)

#print(f"Seno: {seno}\nCoseno: {coseno}\nTangente: {tangente}")
salida=('Resumen de funciones\n'
        f'El seno es    : {seno}\n'
        f'El coseno es  : {coseno}\n'
        f'El tangente es: {tangente}\n'
        f'El angulo es  : {angulo} grados, equivale a {angrad} radianes\n'
        )
print(salida)
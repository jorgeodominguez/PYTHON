#Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos.

print("Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos.")

horas=float(input("\nHoras a calcular: "))
dia=horas/24
minutos=horas*60
segundos=minutos*60

print(f"\n{horas} horas equivalen a {dia:.4f} dia")
print(f"{horas} horas equivalen a {minutos} minutos")
print(f"{horas} horas equivalen a {segundos} segundos\n")
#Calcula la paga total de un trabajador

print("Calculando la paga toral de un trabajador \n")

nombre = input("Dame tu nombre: ")
horas = int(input("Horas Trabajadas: "))
paga = float(input("Paga por hora: "))

tasa = 0.03

pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

print("\nResumen de pagos")
print("****************************************************************************")
print(f"{nombre} trabajo: {horas} horas con una paga de: {paga} pesos a una tasa de: {tasa}")
print("****************************************************************************")

print("----------------------")
print(f"Pagabruta: {pagabruta}")
print(f"Impuestos: {impuesto}")
print(f"Paganeta : {paganeta}")
print("----------------------\n")


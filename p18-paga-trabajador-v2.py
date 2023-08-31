#Calcula la paga de un trabajador, las horas extra se pagan al doble

print("Calcula la paga de un trabajador, las horas extra sepagan al doble\n")

nombre=input("Nombre: ")
horas=int(input("Horas trabajadas: "))
paga=float(input("Paga x hora: "))
extra=0

if horas>40 :
    extra=horas-40
    total=(40*paga)+(2*paga*extra)
else:
    total=horas*paga
print("**********************")
print(f"{nombre} trabajo {horas} horas\ncon paga de {paga}\nhora extra {extra}\ndando un total de {total:.2f}")
print("**********************\n")
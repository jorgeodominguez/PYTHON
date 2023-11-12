class Empleado:
    #Constructor recibe los valores que el usuario pasa
    def __init__(self,nombre,edad,sexo,casado):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.casado=casado
    #Regresa la cadena con los datos
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo=="M" else "Hombre"}, Casado: {"Casado" if self.casado else "No Casado"}'

#principal
emp1=Empleado('Jose Díaz',35,'H',True)
#print('Nombre ',emp1.nombre)
#print('Edad ',emp1.edad)
#print('Sexo ',emp1.sexo)
#print('Casado ',emp1.casado)
print(emp1)

emp2=Empleado('Maria Lopez',22,'M',False)
#print('Nombre ',emp2.nombre)
#print('Edad ',emp2.edad)
#print('Sexo ',emp2.sexo)
#print('Casado ',emp2.casado)
print(emp2)

emp3=Empleado('Rosario Valenzuela',15,'M',True)
print(emp3)

emp4=Empleado('Juan Perez',20,'H',False)
print(emp4)

prom=(emp1.edad+emp2.edad+emp3.edad+emp4.edad)/4

print('Promedio de edades de los empleados ',prom)

print(f'Los nombres son : {emp1.nombre}, {emp2.nombre}, {emp3.nombre}, {emp4.nombre}')

if(not emp2.casado and not emp4.casado):
    print(f"\n{emp2.nombre} se puede casar con {emp4.nombre} ambos son solteros")

if(not emp1.casado and not emp3.casado):
    print(f"\n{emp1.nombre} se puede casar con {emp3.nombre} ambos son solteros")
else:
    print(f"\n{emp1.nombre} no se puede casar con {emp3.nombre} por que ambos estan casados")
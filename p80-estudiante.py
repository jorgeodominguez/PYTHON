#Estudiante diccionarios de datos

estudiante={
    'nombre':'Juan Perez',
    'edad':45,
    'correo':'jperez@msn.com',
    'carrera':'Sistemas'
}

print(f"\nDiccionario original: \n {estudiante}")
estudiante['calificacion']=9.5
estudiante['correo']='juanp@gmail.com'
print(f"\nDiccionario actualizado: \n {estudiante}")

print("\nLas llaves: ")
for k in estudiante.keys():
    print(k,end=" ")

print("\nLos valores: ")
for v in estudiante.values():
    print(v,end=" ")

print("\nLlaves y valores juntos: ")
for k,v in estudiante.items():
    print(f'{k:<10} : {v}')
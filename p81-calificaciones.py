#

materias=['Fisica','Quimica','Matematicas','Geografia','Estadistica']
califs=[10,9,8,7.5,6]
print('Lista de materias: ',materias)
print('Lista de calificaciones: ',califs)
notas=dict(zip(materias,califs))
print("\nLas notas: ",notas,len(notas))
notas.update({'Ingles':10})#actualiza y agrega si no esta
notas.update({'Programacion':7})
print("\nDiccionario actualizado: ",notas,len(notas))
notas.pop('Fisica')#elimina el que se marca
notas.popitem()#elimina el ultimo
print("\nDiccionario actualizado: ",notas,len(notas))
notas.update({'Quimica':10})
#se peude tambien utilizar de esta forma
#notas['Quimica']=10
notas.update({'Matermaticas':10})
#notas['Matermaticas']=10
print("\nDiccionario actualizado: ",notas,len(notas))

s=p=0
for m,c in notas.items():
    print(f"{m:<12} - {c:>5.2f}")
    s=s+c
p=s/len(notas)
print(f"\nLa suma es {s} y el promedio es {p}")
#Funcion que recibe un numero arbitraro de parametros

def saludatodos(*todos):
    print("Saludos a : ",todos)
    for nombre in todos:
        print("Hola",nombre)
    if(len(todos)!=0):
        print("El primero es el primero: ",todos[0])
        print("El Ultimo es el ultimo y es: ",todos[-1])

saludatodos("Jose","Juan","Pedro","Luis","Rocio","Fatima","Maria","Felipe")
saludatodos()
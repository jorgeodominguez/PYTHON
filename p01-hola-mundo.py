# Lee datos del usuario y envia un saludo la pantalla

print("Hola Mundo \n")

print("Leyendo datos y enviando un mensaje a pantalla \n")

nombre = input("Dame tu Nombre: ")
edad = int(input("Dame tu Edad: "))
peso = float(input("Dame el peso: "))

print(f"\n Tu nombre es: {nombre}, Tu edad es: {edad},Tu peso es: {peso}.")

print(type(nombre))
print(type(edad))
print(type(peso))
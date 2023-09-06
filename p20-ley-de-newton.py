#calcula la segunda ley de newton (f=m*a)
import os

os.system('cls')
print('[F]uerza f=m*a')
print('[M]aza m=f/a')
print('[A]celeracion a=f/m')
op=input('Elige ?').upper()

if op == 'F':
    print("\nCalculando la Fuerza")
    m=float(input('Dame la Masa: '))
    a=float(input('Dame la Aceleracion: '))
    f=m*a
    print(f"\nLa fuerza es {f:.2f}")

elif op == 'M':
    print("\nCalculando la Masa")
    f=float(input('Dame la Fuerza: '))
    a=float(input('Dame la Aceleracion: '))
    m=f/a
    print(f"\nLa Masa es {m:.2f}")
elif op == 'A':
    print("\nCalculanto Aceleracion")
    f=float(input('Dame la Fuerza: '))
    m=float(input('Dame la Masa: '))
    a=f/m
    print(f"\nLa Acerelacion es {a:.2f}")
else:
    print("\nOpcion Invalida")

print("\nProceso terminado")

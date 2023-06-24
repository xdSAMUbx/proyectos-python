numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número:  "))

print("¿Qué desea hacer?")
print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("4) Dividir")

decision = int(input("Ingrese la opción que desea realizar (números): "))

if decision == 1:
    resultado = numero1 + numero2
    print(f"El resultado de su suma es: {resultado}")
elif decision == 2:
    resultado = numero1 - numero2
    print(f"El resultado de su resta es: {resultado}")
elif decision == 3:
    resultado = numero1 * numero2
    print(f"El resultado de su multiplicación es: {resultado}")
elif decision == 4:
    resultado = round(numero1 / numero2, 3)
    print(f"El resultado de su división es: {resultado}")
else: 
    print("No ingreso ninguna opción valida, intente de neuvo")

    
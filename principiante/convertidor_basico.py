#convertidor de unidades

medida = float(input("Ingrese la medida que desea convertir: "))

def inicial ():
    print("De las siguientes opciones: ")
    print("1) Metros: ")
    print("2) Pulgadas: ")
    print("3) Pies: ")
    print("4) Millas: ")
    opciones1 = int(input("Digite la medida de la cual viene: "))
    return opciones1

def final ():
    print("De las siguientes opciones: ")
    print("1) Metros: ")
    print("2) Pulgadas: ")
    print("3) Pies: ")
    print("4) Millas: ")
    opciones2 = int(input("Digite la medida a la cual desea convertir: "))
    return opciones2

def convertidor (medida):
    while medida > 0:
        opcion_inicial = inicial()
        opcion_final = final()
        while opcion_inicial == 1:
            if opcion_final == 2:
                conversion = medida * 39.37
                print(f"1 Metro equivale a 39.37 Pulgadas, por lo tanto {medida} metros equivalen a {conversion} pulgadas")
                break
            elif opcion_final == 3:
                conversion = medida * 39.37
                print(f"1 Metro equivale a 39.37 Pulgadas, por lo tanto {medida} metros equivalen a {conversion} pulgadas")
                break
            elif opcion_final == 4:
                conversion = medida * 39.37
                print(f"1 Metro equivale a 39.37 Pulgadas, por lo tanto {medida} metros equivalen a {conversion} pulgadas")
                break
            else:
                print("No sabemos a que medida desea convertir")
                
        
    print("Sin medida no podemos continuar, intentelo de nuevo")

convertidor(medida)


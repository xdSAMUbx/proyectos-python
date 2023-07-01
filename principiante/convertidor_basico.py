#convertidor de unidades

medida = float(input("Ingrese la medida que desea convertir (en Metros): "))

def final ():
    print("De las siguientes opciones: ")
    print("1) Metros: ")
    print("2) Pulgadas: ")
    print("3) Pies: ")
    print("4) Millas: ")
    opciones2 = int(input("Digite la medida a la cual desea convertir: "))
    return opciones2

def convertidor (medida):
    opcion_final = final()
    while medida > 0:
        if opcion_final == 1:
            print("No se puede convertir de metros a metros")
            break
        elif opcion_final == 2:
                conversion = medida * 39.37
                print(f"1 Metro equivale a 39.37 Pulgadas, por lo tanto {medida} metros equivalen a {conversion} pulgadas")
                break
        elif opcion_final == 3:
                conversion = medida * 3.28
                print(f"1 Metro equivale a 3.28 pies , por lo tanto {medida} metros equivalen a {conversion} pies")
                break
        elif opcion_final == 4:
                conversion = medida * 0.000621
                print(f"1 Metro equivale a 0.000621 Millas, por lo tanto {medida} metros equivalen a {conversion} millas")
                break
        else:
                print("No sabemos a que medida desea convertir")
                break

convertidor(medida)


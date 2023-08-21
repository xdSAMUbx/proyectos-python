datos_escritos = []

def datos():
    dat = int(input("Digite cuantos datos desea ingresar: "))
    return dat 

def ingresar_datos(dat):
    
    for i in range(dat):
        dat_var = float(input(f"Ingrese el dato número {i+1}: "))
        datos_escritos.append(dat_var)
        
    datos_escritos.sort()
    print("Los datos son: ", datos_escritos)
    
    return datos_escritos

def medidas_tendencia(datos_escritos):
    moda = max(datos_escritos, key=datos_escritos.count)
    media = sum(datos_escritos) / len(datos_escritos)
    mediana = datos_escritos[len(datos_escritos) // 2]
    print("Moda:", moda)
    print("Media:", media)
    print("Mediana:", mediana)
    
dat = datos()
datos_escritos = ingresar_datos(dat)
medidas_tendencia(datos_escritos)

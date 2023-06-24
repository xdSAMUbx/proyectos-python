#generador de contraseñas
import random
#solicita la cantidad de caracteres que desea que tenga la contraseña
chars = int(input("Ingrese el numero de caracteres que desea que hallan en la contraseña: "))

#crea una contraseña aleatoria 
def generador (chars):
    posibilidades = "abcdefghijklmñnopqrstuvwxyz_-"
    if chars == 0:
        print("Las contraseñas deben tener una cantidad de caracteres")
    else:
        contraseña = ""
        for i in range(chars):
            i = random.choice(posibilidades)
            contraseña += i     #append solo sirve en listas
        
        print(f"Su contraseña es: {contraseña}")
        
generador(chars)
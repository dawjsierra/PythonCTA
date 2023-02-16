from random import randint

# ejercicio 
    # generar un numero aleatorio entre 1-9

numero_secreto = randint(1,9)
print(numero_secreto)

#ejercicio
    # soliciar al usuario un numero entre 1 y 9
    # verificar si es o no el numero secreto
    # si no es el numero secreto, pedir un nuevo numero hasta que acierte
    # contar el numero de intentos
    # si acierta en 3 o menos intentos es un adivino, si no, es un impostor


numero_usuario = input("DIME UN NUMERO: ")
numero_usuario = int(numero_usuario)
numero_secreto = randint(1,9)
intentos = 1

if(numero_usuario == numero_secreto):
    print("ERES UN ADIVINO!!")
else:
    while numero_usuario != numero_secreto:
        if(intentos<=2):
            numero_usuario = input("INCORRECTO, DIME OTRO NUMERO: ")
            numero_usuario = int(numero_usuario)
            intentos=intentos+1
            if(numero_usuario == numero_secreto and intentos<=3):
                    print("eres un adivino")
                    print("el numero secreto es",numero_secreto)
                    print("numero de intentos",intentos)
        else:
            print("eres un impostor")
            print("numero de intentos", intentos)
            break
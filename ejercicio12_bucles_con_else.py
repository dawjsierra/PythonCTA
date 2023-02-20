numero_secreto=8
numero_candidato= int(input("INTRODUCE UN NUMERO ENTRE 1 Y 9: "))
numero_intentos = 1

while(numero_candidato!=numero_secreto):
    print("no has acertado en este intento")
    if(numero_intentos==3):
        print("no has acertado el numeo secreto en el total de intentos")
        break
    numero_candidato = int(input("INTRODUCE UN NUMERO ENTRE 1 Y 9: "))
    numero_intentos+=1
else:
    #solo se ejecuta cuando la condicion del while ha dejado de cumplirse
    print("has acertado el numero secreto")
print("fin de la ejecución")
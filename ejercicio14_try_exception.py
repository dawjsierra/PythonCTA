lista = ["UNO", "DOS", "TRES"]
""" i = int(input("introduce un numero entre 0 y 2: "))

try:
    print(lista[i])
except:
    print("ha ocurrido un error")
 """

# tratamiento especifico
""" i = int(input("introduce un numero entre 0 y 2: "))

try:
    print(lista[i])
except IndexError:
    print("ha ocurrido un error")
 """

# tratamiento generico
try:
    i = int(input("introduce un numero entre 0 y 2: ")) #value error
    print(lista[i]) #indexError
except BaseException as b:
    print("Ha ocurrido un error: ", b)


# tratamiento especifico
try:
    i = int(input("introduce un numero entre 0 y 2: "))#valueerror
    print(lista[i]) #indexerror
except BaseException:
    print("Ha ocurrido un error desconocido. Contacte el administrador")
except ValueError:
    print("Ha ocurrido un error: debes introducir un digito numérico")
except IndexError:
    print("Ha ocurrido un error: debes introducir un numero entero entre 0 y 2")

# con base exception podremos modificar el mensaje de error, por ello si lo ponemos arriba, no llegará a las excepciones de abajo



# EJERCICIO
    # Existe un error que se produce cuando se divide un numero entre 0
    # Averiguar que tipo de error es (nombre) -> (ZeroDivisionError)
    # Pedir al usuario dos numeros y a dividirlos. Si el divisor es 0, capturar
    # la exception y volver a pedir otro par de numeros


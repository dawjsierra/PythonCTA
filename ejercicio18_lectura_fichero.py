fichero = open("palabras_castellano_100.txt", "r", encoding="utf-8")
# contenido = fichero.read() lee todo el fichero
# contenido = fichero.readline() lee una linea

contenido = fichero.readlines()
print(contenido)
fichero.close()


#EJERCICIO
    # limpiar fichero de saltos de linea
    # pedir al usuario que introduzca una contraseña
    # comprobamos que la contraseña no se encuentre en el fichero
    # si la contraseña coincide con una palabra, se debe repetir otra hasta que no coincida

fichero 
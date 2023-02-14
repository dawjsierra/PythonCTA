nombre = "valor"
print(type(nombre))

3
3.5
True
print(type(3)) #int
print(type(3.5)) #float
print(type(True)) #boolean


#LOS STRINGS SON INMUTABLES
texto ="en un lugar de la mancha, cuyo nombre..."

texto.capitalize()
texto.upper() #no modifica el valor de la variable texto
texto = texto.upper()


#Concatenacion de string
cadena1 = "hola"
espacio = " "
cadena2 = "a todos"
total = cadena1 + espacio + cadena2

print(total)

anyo = 2023
nombre = "Python"
version = 3
# ¿Como escribimos por pantalla '2023 Python 3' usando el operador +?

# ¿Como escribimos por pantalla '2023 Python 3' sin utilizar el operador +?

print( str(anyo) + nombre + str(version)  )


#operador * está sobrecargado para str copiando n veces la cadena
cadena = "Esta es una cadena"

print(cadena*3)



#SLICING
nombre_fichero = "saul.jpg"
print(nombre_fichero[-3:])

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print(type(dias)) #tipo dias (collecion, no array!)
print(dias[0]) #posicion 0
print(dias[-2:]) #dias fin de semana
print(dias[:-2]) #dias laborales

print(nombre_fichero[nombre_fichero.index("."):]) #.jpg
print(nombre_fichero[nombre_fichero.index(".")+1:]) #jpg



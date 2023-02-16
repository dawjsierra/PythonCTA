from comunes import dias_semanas
from comunes import clientes

#pass -> es el comodin (no hace nada) para cuando hay que poner codigo y no hay codigo que poner
edad = 18
if(edad>=18):
    pass






#IF
mayoria_edad=18
edad=17

if(edad>=mayoria_edad):
    print("es mayor de edad")
    print("otra cosa")
print("final del proceso")

if edad>=mayoria_edad:
    print("es mayor de edad")
    print("pasa")
else:
    print("es menor de edad")
    print("fuera")

if(edad>=mayoria_edad):
    print("es mayor de edad")
    print("pasa")
elif(edad>=16):
    print("anda ahi, ahi")
    print("me lo pienso")
else:
    print("es menor de edad")
    print("fuera")


# if ternario
anyos_experiencia = 5
salario = 0
if anyos_experiencia>4:
    salario = 2000
else:
    salario=180000
print(salario)

salario2 = 2000 if anyos_experiencia>4 else 18000
print(salario2)

#ejercicio
    # solicitar al usuario un nombre de fichero que incluye su extensión
    # crear una variable que tenga el valor "fichero png" si la extension es .png
    # o el valor "fichero jpg" si la extension es .jpg
    # usar input, notacion ternario, slicing

""" fichero = input("nombre de la extension del fichero")
apartirpunto = fichero[fichero.index("."):]
nombrefichero = ""

if(apartirpunto == ".jpg"):
    nombrefichero="fichero jpg"
elif(apartirpunto == ".png"):
    nombrefichero="fichero png"
else:
    nombrefichero="ninguna"
print(nombrefichero) """

#forma ternaria
""" nombre_fichero = input("introduce el nombre del fichero:")
x=nombre_fichero[-3:]
extension = "FICHERO PNG" if nombre_fichero[-3:]=="png" else ("FICHERO JPG" if nombre_fichero[-3:]=="jpg" else "EXTENSION DE")
print(extension) """






#WHILE
""" contador=0
lista = []
while contador<10:
    print(contador)
    contador=contador+1
print("final del bucle") """






#FOR
#gracias a la importacion de las primeras lineas, disponemos de las lista dias_semana
dias_semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
for dia in dias_semana:
    print(dia)


#EXAMEN CERTIFICACION: EL ULTIMO ELEMENTO NO ENTRA (en este caso imprime del 0 al 9)
rango = range(0,10)
for numero in rango:
    print(numero)

#range(10) --> seria entre 0 y 10 (range de parada)
#range(1,10) --> entre 1 y 10
# range (1, 10, 2) --> emtre 1 y 10 de 2 en 2
    
print("\nfor numero in range (1,10,2)") # cuenta hacia delante
for numero in range(1, 10, 2):
    print(numero, end="-")

print("\nfor numero in range (1,10,-1)") # cuenta hacia atrás
for numero in range(10, 1, -1):
    print(numero, end="-")


#creacion de listas con bucle for
lista_numeros_pares = list(range(0,101,2))
print(type(lista_numeros_pares))
print(lista_numeros_pares)

lista_numeros_pares = [x for x in range(0,101,2)]
print(lista_numeros_pares)

lista_pepes = ["pepe" for x in range(0,101,2)]
print(lista_pepes)

lista_pepes = ["pepe"*3 for x in range(0,101,2)]
print(lista_pepes)

#match
#muy parecido a switch
print("ejemplos de match")

edad=19
match edad:
    case 0:
        print("0")
    case 19:
        print("19")
    






#try
#with
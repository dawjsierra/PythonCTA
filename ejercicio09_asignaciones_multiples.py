x=5
y=10
z=8
x,y,z=y,z,x
print(x,y,z)

nombre, apellido, anyo, ciudad = 'fernando', "paniagua", 1971, "madrid"

nombre1 = "uno"
nombre2 = "dos"
nombre3 = "tres"
nombre1, nombre2, nombre3 = "tres", "uno", "dos"


print(dir()) #variable que maneja python internamente, dir tiene una estructura de datos de la clase list

print('n' in dir()) # no está n porque no estaba antes declarada
print('x' in dir()) # si que está porque estaba ya declarada

def funcion1():
    a=8
    print("final de la funcion")

funcion1()
print("final")
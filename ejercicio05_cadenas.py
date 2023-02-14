# CADENAS
cadena = "esto es una cadena $ 34"

#inmutable
#admite slicing

# manejo como objeto
#javier.sonreir()

# manejo como funcion
#sonreir(javier)

print(len(cadena))
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] #lista
dias2 = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo") #tupla
print(len( dias ))
print(len( dias2 ))


#funcion input

#metodo INDEX de la clase string, posicion =  variable_string.index(cadena_a_buscar)
#utilizando SLICING y el parametro sep de la funcion mostrar texto
#miimagen####png cuando el usuario introduzca miimagen.png
# loqueseademicasa.gif --> loqueseademicasa#####gif
# cv.docx --> cv#####docx

nombre_fichero = input("introduce el nombre del fichero:")
print("nombre del fichero -> ", nombre_fichero)
print(nombre_fichero[0:nombre_fichero.index(".")]+"#####"+nombre_fichero[nombre_fichero.index(".")+1:])
# CONVERSIONES

#cast de una variable -> conversion de tipo

a=5 #entero
b=5.1
c="5"

af = float(a)
print(af)
bi = int(b)
print(bi)
ci = int(c)
print(ci)
bs = str(b)
print(type(bs))

#funcion isinstance
# determina si una instancia (variable, objeto) es de una clase concreta

print(isinstance(c, str))

def sumar(a, b):
    return a+b

suma = sumar (3,8)
restar = sumar (3,8)

print(resultado)
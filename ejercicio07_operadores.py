# OPERADORES LOGICOS

"""

== IGUAL
!= DISTINTO
> MAYOR
>= MAYOR O IGUAL
< MENOR
<= IGUAL

and
or
not

"""

salario = 5000
edad = 21
numero_hijos = 3
altura = 170
peso = 85
ciudad = "zaragoza"

#salario es mayor o igual que 5000
print(salario >= 5000)

#salario es menor que 5000 o tiene hijos
print(salario<5000 or numero_hijos > 0)

""" def es_menor_5000(salario):
    print("es_menor_5000")
    return salario < 5000

def tiene_hijos(numero_hijos):
    print("tiene hijos")
    return numero_hijos > 0

print(es_menor_5000(salario) or tiene_hijos(numero_hijos)) """

#salario menor que 5000, tiene hijos, pesa mas de 80 kg y mide menos de 160
print(salario<5000 and numero_hijos>0 and altura<160)

#vive en zaragoza, pesa menos de 70 kilos, es mayor de edad y cobra mas de 10000
print(ciudad == "Zaragoza" and peso <70 and numero_hijos == 0 and edad>17 and salario > 10000)


#(No vive en Zaragoza ni en Madrid, pesa entre 60 y 70 kilos, no menos de 3 hijos, es mayor de edad) o cobra entre 10000 y 150000
print((ciudad != "Zaragoza" and ciudad !="Madrid" and peso>59 and peso<71 and numero_hijos>=3) or (salario>= 10000 or salario<=15000))

#mejora de la condicion anterior
vive_fuera = ciudad != "Zaragoza" and ciudad!="Madrid"
tiene_peso_medio = peso>=60 and peso<=70
es_mayor_edad = edad>17
salario_en_rango=salario>=10000 and salario<=150000
print((vive_fuera and tiene_peso_medio and numero_hijos>=3) or (salario_en_rango))
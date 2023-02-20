from comunes import dias_semana
ingresos2 = [10000, 12000, 13000, 8000, 3000, 2000, 1500, 28000]
ingresos = [10000, 12000, 13000, 8000, 3000, 2000, 1500]

# ¿como juntar ingresos con dias semana?

# solucion cutre
lista_ingresos = []
for indice in range (0,7):
    lista_ingresos.append([dias_semana[indice], ingresos[indice]])
print("\n",lista_ingresos,"\n")


# solucion guay
# hay que tener cuidado con el numero de items, ya que si en una hay mas que otra no te da fallo y no te coge el ultimo valor
lista_ingresos = list(zip(dias_semana, ingresos2))
print("\n INGRESOS2 --> ",lista_ingresos,"\n")

lista_ingresos = list(zip(dias_semana, ingresos))
print("\n INGRESOS --> ",lista_ingresos,"\n")

numero_clientes = (3,8,9)
nombre_clientes = ("Javier", "Saul", "Vanesa")
anyo_contratacion = [1999, 2015, 2018]
lista_clientes = tuple(zip(numero_clientes, nombre_clientes, anyo_contratacion, strict=True))
# con strict le indicamos que tenga que respetar la longitud de listas/tuplas. si tienen longitudes diferentes da error
print("\n LISTA CLIENTES -->",lista_clientes)






# Zip con tres elementos y error detectado
numero_clientes = (3,8,9)
nombre_clientes = ("Javier", "Saul", "Vanesa", "Angel")
anyo_contratacion = [1999, 2015, 2018]
try:
    lista_clientes = tuple(zip(numero_clientes, nombre_clientes, anyo_contratacion, strict=True))
except ValueError as e:
    print("Las listas no coinciden")
print(lista_clientes)




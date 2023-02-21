#EJERCICIO
    # crear una lista de la compra con tres productos
    # solicitar al usuario un producto y agregarlo a la lista
    # ordenar la lista
    # mostrar el contenido de la lista
    # solicitar al usuario un producto e indicar si está o no en está en la lista
    # solicitar al usuario un producto (que esté en la lista) y eliminarlo de la lista
    # solicitar un producto e insertarlo en el centro de la lista

try:

    cesta = ["Brócoli","Huevos","Gaseosa"]
    print(cesta)

    producto1 = input("INTRODUZCA UN PRODUCTO -->")
    cesta.append(producto1)

    cesta.sort()

    print(cesta,"\n")

    producto2 = input("¿Qué producto quiere comprobar si está en la cesta o no?")

    if(producto2 in cesta):
        print("EL PRODUCTO",producto2,"SE ENCUENTRA EN LA CESTA\n")
    else:
        print("EL PRODUCTO",producto2,"NO SE ENCUENTRA EN LA CESTA\n")
    
    producto3 = input("¿Desea eliminar un producto?")

    if(producto3 in cesta):
        cesta.remove(producto3)
        print("PRODUCTO ELIMINADO")
        print(cesta,"\n")
    else:
        print("EL PRODUCTO",producto3,"NO SE ENCUENTRA EN LA LISTA...\n")
    
    producto4 = input("¿Que producto desea introducir?")
    medio_cesta = int(cesta.__len__()/2)
    cesta.insert(medio_cesta, producto4)
    print("PRODUCTO",producto4,"AÑADIDO")
    print(cesta,"\n")
    


except ValueError as d:
    print(d)

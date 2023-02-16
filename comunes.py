dias_semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
clientes = ["Victor", "Vanesa", "Javier", "Alexander"]


def calcular_solvencia(cliente):
    return(len(cliente))


lista_solvencia=[[cliente, calcular_solvencia(cliente)] for cliente in clientes]
print(lista_solvencia)

# show
# remove nombres.txt
# remove nombres.txt fotografias.png
# remove nombres.txt fotografias.png autores.xls


comando = input("introduce un comando [show, remove]:")

match comando.split():
    case ["show"]:
        print("muestra todos los ficheros")
    case ["remove", *ficheros]:
        print("borrando...", end="")
        for fichero in ficheros:
            print(fichero, sep=",", end="")



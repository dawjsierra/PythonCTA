dividendo = 5
divisor = 0

try:
    resultado = dividendo/divisor
except ZeroDivisionError:
    print("division entre 0")
else:
    print("resultado -> ", resultado)
    #solo si hay error en el bloque try
finally: 
    print("fin del proceso")
    #se ejecuta siempre despues del try-except
print("EL FINAL DE TODO") # se ejecuta despues del try-except PERO NO OBLIGATORIAMENTE
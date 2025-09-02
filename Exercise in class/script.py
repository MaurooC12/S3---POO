# Autor: Mauricio Cepeda Villanueva
# Esto es una prueba para novatos
# 1. Realizar las tablas de multiplicar del número que usted ingrese
numProducto = int(input("Escriba un número del cual desee obtener las tablas de multiplicar: "))
for i in range(6):
   resultado = i * numProducto
   print(resultado)


# 2. Utilizando una función obtenga el número factorial de un número dado
numFactorial = int(input("Por favor ingrese un número para obtener su factorial: "))

def factorial(a):
    resultado = 1
    for i in range(1, a + 1):
        resultado = resultado * i
    return resultado


print(f"El factorial de {numFactorial} es: {factorial(numFactorial)}")

# 3. 
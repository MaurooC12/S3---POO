# Autor: Mauricio Cepeda Villanueva
# (De qué trata el archivo) Esto es una prueba para novatos
# Ejercicio 1 
# texto = input("Escriba un número del 1 al 10")
# print(texto)
#2 Realizar las tablas de multiplicar del número que usted ingrese
#numProducto = int(input("Escriba un número del cual desee obtener las tablas de multiplicar: "))
#for i in range(6):
#   resultado = i * numProducto
#   print(resultado)


#3 Utilizando una función obtenga el número factorial de un número dado
numFactorial = int(input("Por favor ingrese un número para obtener su factorial: "))

def factorial(a):
    resultado = 1
    for i in range(1, a + 1):
        resultado = resultado * i
    return resultado


print(f"El factorial de {numFactorial} es: {factorial(numFactorial)}")
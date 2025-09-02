# Autor: Mauricio Cepeda
# Primera versión

# 1. Estructuras de control
# if, for, while, switch, dowhile, 

# Prueba
# Estructure un programa que mencione si su calificación es meritoria. Una nota meritoria sería una nota de 4.5 a 5
nota = float(input("Para saber si su nota es meritoria o no escriba la nota obtenida en forma númerica entre 0 y 5: "))
if(nota>=4.5 and nota<=5):
    print("Esta nota es meritoria")
else:
    print("Esta nota no es meritoria")
    
# 18. Escribir un programa en Java que lea un número entero desde teclado y realiza la suma de los 100 número siguientes, mostrando el resultado en pantalla.
numeroIngresado = int(input("Por favor ingrese un número entero: "))
contador = 0
for i in range(numeroIngresado, numeroIngresado + 101):
    contador += i
print(f"La suma de 100 números siguientes a {numeroIngresado} es {contador}")

# 19. Escribir un programa en Java que convierta de euros a dólares. Recibirá un número decimal correspondiente a la cantidad en euros y contestará con la cantidad correspondiente en dolares.
cantidadEuros = float(input("Por favor ingrese la cantidad de euros que desee convertir a dólares. La cantidad ingresada debe ser número decimal: "))
convertidorDolares = cantidadEuros * 1.17
print(f"La cantidad de {cantidadEuros} Euros, es equivalente a {convertidorDolares} Dólares.")

# 20. Escribir un programa en Java que calcule el área de un rectángulo del cual se le proporcionará por el teclado su altura y anchura (números decimales).
alturaRectangulo = float(input("Por favor ingrese la altura del rectángulo en número decimal: "))
anchuraRectangulo = float(input("Por favor ingrese el ancho del rectángulo en número decimal: "))
print(f"El área del rectángulo con altura {alturaRectangulo} y ancho {anchuraRectangulo} es {anchuraRectangulo*alturaRectangulo} unidades cuadradas")

# 21. Escribir un programa en Java que lea dos números del teclado y diga cual es el mayor y cual el menor. 
numeroIngresadoUno = int(input("Por favor ingrese un número: "))
numeroIngresadoDos = int(input("Por favor ingrese otro número: "))
if(numeroIngresadoUno>numeroIngresadoDos):
    print(f"El número {numeroIngresadoUno} es mayor que {numeroIngresadoDos}")
elif(numeroIngresadoDos>numeroIngresadoUno):
    print(f"El número {numeroIngresadoDos} es mayor que {numeroIngresadoUno}")
else:
    print(f"Los números {numeroIngresadoDos} y {numeroIngresadoUno} son iguales")
    
# 24 Escriba un programa que lea los coeficientes a, b y c de una ecuación de segundo, y estudie si tiene o no solución. En caso positivo, las soluciones se calcularán e imprimirán en pantalla.
print("En este ejercicio estudiará si una ecuación de segundo grado de la forma (ax**2 + bx + c) tiene o no solución.")
coeficienteA = int(input("Por favor ingrese el coeficiente a: "))
coeficienteB = int(input("Por favor ingrese el coeficiente b: "))
coeficienteC = int(input("Por favor ingrese el coeficiente c: "))
discriminanteEcuacion = (coeficienteB**2)-4*(coeficienteA*coeficienteC)
solucionesEcuacion = (-coeficienteB+((coeficienteB**2)-4*(coeficienteA*coeficienteC))**1/2)/2*coeficienteA
if(discriminanteEcuacion<0):
    print(f"La ecuación {coeficienteA}x**2 + {coeficienteB}x + {coeficienteC} no tiene soluciones reales")
elif(discriminanteEcuacion==0):
    print(f"La ecuación {coeficienteA}x**2 + {coeficienteB}x + {coeficienteC} tiene una única solución y es {solucionesEcuacion}")
else:
    print("La ecuación {coeficienteA}x**2 + {coeficienteB}x + {coeficienteC} tiene 2 soluciones reales y son")
    print(f"Solución 1, x = {(-coeficienteB+((coeficienteB**2)-4*(coeficienteA*coeficienteC))**1/2)/2*coeficienteA}")
    print(f"Solución 2, x = {(-coeficienteB-((coeficienteB**2)-4*(coeficienteA*coeficienteC))**1/2)/2*coeficienteA}")
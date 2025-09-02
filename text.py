# Autor: Mauricio Cepeda
# Primera versión

# 1. Estructuras de control
# if, for, while, switch, dowhile, 

# Prueba
# Estructure un programa que mencione si su calificación es meritoria
# Una nota meritoria sería una nota de 4.5 a 5

'''nota = float(input("Escriba la nota obtenida en forma númerica entre 0 y 5"))
if(nota>=4.5 and nota<=5):
    print("Esta nota es meritoria")
else:'''''
# 19. Escribir un programa en Java que convierta de euros a dólares. Recibirá un número decimal correspondiente a la cantidad en euros y contestará con la cantidad correspondiente en dolares.
cantidadEuros = float(input("Por favor ingrese una cantidad de euros que desee convertir a dólares. La cantidad ha ingresar es en número decimal: "))
convertidorDolares = cantidadEuros * 1.17
print(f"La cantidad de {cantidadEuros} Euros, es equivalente a {convertidorDolares} Dólares.")

#24 Escriba un programa que lea los coeficientes a, b y c de una ecuación de segundo, y estudie si tiene o no solución. En caso positivo, las soluciones se calcularán e imprimirán en pantalla.
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
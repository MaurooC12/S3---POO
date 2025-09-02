numeroIngresadoUno = int(input("Por favor ingrese un número: "))
numeroIngresadoDos = int(input("Por favor ingrese otro número: "))
if(numeroIngresadoUno>numeroIngresadoDos):
    print(f"El número {numeroIngresadoUno} es mayor que {numeroIngresadoDos}")
elif(numeroIngresadoDos>numeroIngresadoUno):
    print(f"El número {numeroIngresadoDos} es mayor que {numeroIngresadoUno}")
else:
    print(f"Los números {numeroIngresadoDos} y {numeroIngresadoUno} son iguales")
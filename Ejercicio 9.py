añoB= int(input("Ingrese un año: "))

if añoB % 4 ==0 and añoB % 100 != 0:
    print("Es un año bisiesto")
elif añoB % 400==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

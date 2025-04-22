print("Adivina el numero secreto")

numero_secreto=7

while True:
    numero= int(input("Ingrese un numero: "))
    if numero < numero_secreto:
        print("El numero ingresado en menor al numero secreto")
    elif numero > numero_secreto:
        print("El numero ingresado en mayor al numero secreto")
    else:
        print("Felicidades, Numero correcto")
        break

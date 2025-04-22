print("IMC")
peso = float(input("Ingrese su peso: "))
altura= float(input("Ingrese su altura: "))

imc= peso/altura**2

if imc < 18.5:
    print("bajo peso")
elif 18.5 >= imc < 24.9:
    print("Normal")
elif 24.9 > imc < 29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidad")
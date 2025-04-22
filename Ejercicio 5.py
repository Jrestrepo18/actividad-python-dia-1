total_cuenta=float(input("Ingrese el total de la cuenta: "))
porcentaje=float(input("Ingrese que porcentaje desea 10 15 20 porciento:"))
if porcentaje == 10:
    propina=total_cuenta * (porcentaje/100)
    print(f"Su propina es: {propina}")
elif porcentaje == 15:
    propina=total_cuenta * (porcentaje/100)
    print(f"Su propina es: {propina}")
elif porcentaje == 20:
    propina=total_cuenta * (porcentaje/100)
    print(f"Su propina es: {propina}")
else:
    print("Porcentaje no valido")

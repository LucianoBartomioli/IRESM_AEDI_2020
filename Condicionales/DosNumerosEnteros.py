num1=int(input("Ingrese el primer numero entero: "))
num2=int(input("Ingrese el segundo numero entero: "))
if num1 > num2:
    CuadradoPrimero=num1 ** 2
    CuadradoSegundo = num2 ** 2
elif num1==num2:
    print("Los numeros son iguales")
else:
    CuadradoPrimero = num2 ** 2
    CuadradoSegundo = num1 ** 2


Division = CuadradoPrimero/CuadradoSegundo

print(f"El Resultado de la division es {Division}")
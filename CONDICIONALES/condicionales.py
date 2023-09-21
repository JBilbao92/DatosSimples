'''Todos los ejercicios realizados y corregidos estaran en comentario


fuente: https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

Ejercicio 1
edad = int(input("Introduzca su edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

Ejercicio 2
passw = "contraseña"
password = input("Introduzca su contraseña: ") 
if passw == password.lower():
    print("Contraseña Correcta")
else:
    print("Contraseña Erronea")

    
Ejercicio 3
divisor1 = int(input("Introduzca el divisor: "))
divisor2 = int(input("Introduzca el dividendo: "))
resto = int(divisor1%divisor2)
division = int(divisor1/divisor2)
if resto == 0:
    print("Error")
else:
    print(division)

Ejercicio 4
numero = int(input("Introduzca un número: "))
division = int(numero%2)
if division == 0:
    print("Su número es par")
else:
    print("Su numero es impar")

Ejercicio 5
edad = int(input("Introduzca su edad: "))
income = int(input("Introduzca sus ingresos: "))
if edad >= 16 and income >= 1000:
    print("Debe tributar")
else:
    print("Usted no debe tributar")

Ejercicio 6
sexo = input("Introduzca su género (M o H): ")
nombre = input("Introduzca su nombre: ")
if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Su grupo es: " + grupo)

Ejercicio 7
renta = int(input("Indique su renta: "))
if renta < 10000:
    tipo = "5%"
elif renta < 20000:
    tipo = "15%"
elif renta < 35000:
    tipo = "20%"
elif renta < 60000:
    tipo = "30%"
else:
    tipo = "45%"
print("Su tipo impositivo es " + tipo)

Ejercicio 8
rend = float(input("Indique su rendimiento (formato 0.X): "))
if rend < 0.4:
    result = "inaceptable" 
    bonus = "2400€"
elif rend < 0.6:
    result = "aceptable" 
    bonus = "4800€"
else:
    result = "meritorio" 
    bonus = "7200€"
print("Su resultado es " + result + ", su bonus es " + bonus + ".")

Ejercicio 9
edad = int(input("Introduzca su edad: "))
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10
print("El precio de su entrada es", precio, "€.")

Ejercicio 10
print("Bienvenido a Bella Napoli.\nNuestrostipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana")
tipo = input("Introduce el número de la pizza que desee: ")
if tipo == "1":
    print("Ingredientes\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella , tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
    print("Ingredientes pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozarella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente =="2":
        print("jamón")
    else:
        print("salmón")
'''

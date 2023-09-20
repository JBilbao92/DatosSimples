'''##En este archivo vienen todos los ejercicios, los ejercicios resueltos se dejaran como comentario

Fuente: https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

Ejercicio 1
print("¡Hola Mundo!")

Ejercicio 2
texto = "¡Hola Mundo!"
print(texto)

Ejercicio 3
nombre = input("Introduce tu nombre: ")
print("¡Hola " + nombre + "!")

Ejercicio 4
resultado = ((3+2)/(2*5))**2
print(resultado)

Ejercicio 5
Horas = float(input("Horas trabajadas: "))
Coste = float(input("Coste por horas: "))
Paga = Horas * Coste
print("Tu salario es", Paga, " €")

Ejercicio 6
n = int(input("Introduce un numero: "))
suma = (n*(n+1))/2
print("El sumatorio de los primos desde 1 hasta ", str(n), " es", str(suma))

Ejercicio 7
peso = input("Su peso es: ")
altura = input("Su altura es(en metros): ")
imc = round(float(peso)/(float(altura)**2))
print("Su imc es ", str(imc))

Ejercicio 8
n = int(input("Introduce un dividendo: "))
m = int(input("Introduce un divisor: "))
c = n//m
r = n%m
print(n , "entre", m, "da un cociente", c, "y un resto de", r)

Ejercicio 9
cantidad = int(input("Introduzca cantidad a invertir: "))
interes = int(input("Introduzca interés anual: "))
años = int(input("Introduzca años a invertir: "))
ganancia = int(cantidad*(interes/100+1)**años)
print("Su capital obenido será: ", ganancia)

Ejercicio 10
payasos = int(input("Numero de payasos: "))
muñecas = int(input("Numero de muñecas: "))
peso = int((payasos*112) + (muñecas*75))
print("El peso del paquete es", peso, "gramos")

Ejericio 11
inversion = float(input("Introduce inversion: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance el tercer año:" + str(round(balance3, 2)))

Ejercicio 12
precion = 3.49
descuento = int(3.49*0.6)
preciod = int(precion - descuento)
print("Precio Normal:", precion, "€")
print("Descuento:", descuento, "€")
print("Precio tras descuento:", preciod, "€")
'''
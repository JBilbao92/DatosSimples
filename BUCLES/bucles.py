'''Todos los ejercicios realizados y corregidos estaran en comentario


fuente: https://aprendeconalf.es/docencia/python/ejercicios/bucles/


Ejercicio 1
palabra = input("Introduce una palabra: ")
for i in range(10):
    print(palabra)

Ejercicio2
años = int(input("Introduce tu edad: "))
for i in range(años):
    print("Has cumplido " + str(i+1) + " años")

Ejercicio 3
numero = int(input("Introduzca un numero entero positivo: "))
for i in range(1, numero+1, 2):
    print(i, end=", ")

Ejercicio 4
numero = int(input("Introduzca un numero entero positivo: "))
for i in range(numero, -1, -1):
    print(i, end=", ")

Ejercicio 5
cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interes anual: "))
años = int(input("Años: "))
for i in range(años):
    cantidad *= 1 + interes / 100
    print("Dinero tras " + str(i+1) + " años" + str(round(cantidad, 2)))

Ejercicio 6
numero = int(input("Introduce la altura del triangulo (numero positivo): "))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")

Ejercicio 7
for i in range(1, 11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("")

Ejercicio 8
numero = int(input("Introduce la altura del triangulo: "))
for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

Ejercicio 10
numero = int(input("Introduzca numero entero positivo mayo que 2: "))
i = 2
while numero % i !=0:
    i += 1
if i == numero:
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo")

Ejercicio 11
palabra = input("Introduzca una palabra: ")
for i in range(len(palabra)-1, -1, -1):
    print(palabra[i])

Ejercicio 12
frase = input("Introduzca una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador +=1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

Ejercicio 13
while True:
    frase = input("Introduce una palabra:")
    if frase == "salir":
        break
    print(frase)
'''
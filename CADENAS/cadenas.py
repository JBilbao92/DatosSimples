'''Todos los ejercicios realizados y corregidos estaran en comentario


fuente: https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

Ejercicio 1 
nombre = input("Nombre: ")
n = input("Numero entero: ")
print((nombre + "\n") * int(n))

Ejercicio 2
nombre = input("Nombre completo: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())

Ejercicio 3
nombre = input("Nombre completo: ")
print(nombre.upper(), "tiene", str(len(nombre)), "letras")

Ejercicio 4
telf = input("Introduzca nº de teléfono en formato +XX-XXXXXXXXX-XX: ")
print("El número fijo es ", telf[4:-3])

Ejercicio 5
frase = input("Introduzca una frase: ")
print(frase[::-1])

Ejercicio 6
frase = input ("Introduzca una frase: ")
vocal = input ("Introduzca una vocal: ")
print(frase.replace(vocal, vocal.upper()))

Ejercicio 7
email = input("Indroduzca correo electronico: ")
print(email[:email.find("@")] + "@ceu.es")

Ejercicio 8
precio = input("Introduzca precio con decimales: ")
print(precio[:precio.find(".")], "€ y ", precio[precio.find(".")+1:], "céntimos.")

Ejercicio 9
fecha = input("Introduzca una fecha (formato dd/mm/aaaa): ")
dia = fecha[:fecha.find("/")]
mesaño = fecha[fecha.find("/")+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[mesaño.find("/")+1:]
print("Día", dia)
print("Mes", mes)
print("Año", año)

Ejercicio 10'''

'''Todos los ejercicios realizados y corregidos estaran en comentario


fuente: https://aprendeconalf.es/docencia/python/ejercicios/listas-tuplas/

Ejercicio 1
asignaturas = ["Mate", "Fisica", "Quimica", "Historia", "Lengua"]
print(asignaturas)

Ejercicio2
asignaturas = ["Mate", "Fisica", "Quimica", "Historia", "Lengua"]
for asignatura in asignaturas:
    print("Estudio " + asignatura)

Ejercicio 3
asignaturas = ["Mate", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    nota = input("Nota en " + asignatura + ":")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado " + notas[i])

Ejercicio 4
numero = []
for i in range (6):
    numero.append(int(input("Introduzca números ganadores: ")))
numero.sort()
print("Los números ganadores son " + str(numero))

Ejercicio 5
numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    print(numeros[-i], end=", ")

Ejercicio 6
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobada = []
for asignatura in asignaturas:
    puntos = float(input("Nota en " + asignatura + ":"))
    if puntos >= 5:
        aprobada.append(asignatura)
for asignatura in aprobada:
    asignaturas.remove(asignatura)
print("Tienes que repetir " + str(asignaturas))

Ejercicio 7
import string
string.ascii_lowercase
alfabeto = list(string.ascii_lowercase)
for i in range(len(alfabeto), 1, -1):
    if i % 3 == 0:
        alfabeto.pop(i-1)
print(alfabeto)

Ejercicio 8
palabra = input("Introduzca una palabra: ")
palabra_reves = palabra
palabra = list(palabra)
palabra_reves = list(palabra_reves)
palabra_reves.reverse()
if palabra == palabra_reves:
    print ("Palindromo")
else:
    print ("No es un palindromo")

Ejercicio 10
precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
print("Precio mínimo: " + str(min))
print("Precio máximo: " + str(max))

Ejercicio 11'''
vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)
producto = 0
for i in range(len(vector1)):
    producto += vector1[i]*vector2[i]
print("Resultado: " + str(producto))

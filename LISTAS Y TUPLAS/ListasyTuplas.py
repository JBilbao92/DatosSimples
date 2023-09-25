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

Ejercicio 5'''

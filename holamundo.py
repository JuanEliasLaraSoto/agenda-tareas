import numpy as np
print("holamundo")

def saludar(nombre):
    return f"Hola, {nombre}!"    
mensaje=saludar("juanito")
print(mensaje)

def es_par(n):
    if n%2==0:
        print("es par")
    else:
        print("es impar")

for numero in range(1,50):
    es_par(numero)


def contar_palabras(frase):
    split=frase.split()
    conteo={}
    for palabra in split:
        if conteo.__contains__(palabra):
            conteo[palabra]+=1
        else:
            conteo[palabra]=1
    return conteo
print(contar_palabras("juane es listo y es alto"))


def cargar_tareas(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

tareas=cargar_tareas("tareas.txt")
print(tareas)
with open("tareas-2.txt", "w", encoding="utf-8") as f:
    for tarea in tareas:
        f.write(tarea + "\n")

while True:
    print("\n1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        tareas=cargar_tareas("tareas-2.txt")

        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    elif opcion == "2":
        nueva = input("Nueva tarea: ")
        tareas=cargar_tareas("tareas-2.txt")
        tareas.append(nueva)
        with open("tareas-2.txt", "w", encoding="utf-8") as f:
            for tarea in tareas:
                f.write(tarea + "\n")    
    elif opcion == "3":
        break

    
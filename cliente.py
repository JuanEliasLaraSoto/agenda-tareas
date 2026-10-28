import requests

URL = "http://127.0.0.1:8000/tareas"


def listar():
    respuesta = requests.get(URL, timeout=5)
    respuesta.raise_for_status()
    tareas = respuesta.json()

    if not tareas:
        print("No hay tareas")
        return

    for tarea in tareas:
        print(f"{tarea['id']}. {tarea['texto']}")


def añadir(texto):
    respuesta = requests.post(URL, json={"texto": texto}, timeout=5)
    respuesta.raise_for_status()
    print(f"Creada: {respuesta.json()['texto']}")


def borrar(id):
    respuesta = requests.delete(f"{URL}/{id}", timeout=5)

    if respuesta.status_code == 404:
        print("Esa tarea no existe")
        return

    respuesta.raise_for_status()
    print(f"Borrada la tarea {respuesta.json()['borrada']}")


while True:
    print("\n1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Borrar tarea")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "4":
        break

    try:
        if opcion == "1":
            listar()
        elif opcion == "2":
            texto = input("Nueva tarea: ").strip()
            if texto:
                añadir(texto)
            else:
                print("La tarea no puede estar vacía")
        elif opcion == "3":
            try:
                id = int(input("Id de la tarea a borrar: "))
            except ValueError:
                print("Escribe un número")
                continue
            borrar(id)
        else:
            print("Opción no válida")
    except requests.exceptions.RequestException as e:
        print(f"No puedo hablar con el servidor: {e}")
        print("¿Está arrancado uvicorn?")

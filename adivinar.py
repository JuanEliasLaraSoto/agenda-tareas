import random
def jugar():
    secreto = random.randint(1, 100)
    intentos = 0

    while intentos < 7:
        try:
            numero = int(input("Adivina el número: "))
        except ValueError:
            print("Escribe un número válido")
            continue

        intentos += 1

        if numero < secreto:
            print("Más alto")
        elif numero > secreto:
            print("Más bajo")
        else:
            print(f"¡Acertaste en {intentos} intentos!")
            break
    else:
        print(f"Se acabaron los intentos. Era {secreto}")


while True:
    jugar()
    if input("¿Jugar otra vez? (s/n): ").lower() != "s":
        break

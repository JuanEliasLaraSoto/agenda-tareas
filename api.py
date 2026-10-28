import requests


def obtener_coordenadas(ciudad):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    respuesta = requests.get(
        url,
        params={"name": ciudad, "count": 1, "language": "es"},
        timeout=5,
    )
    respuesta.raise_for_status()  # lanza una excepción si el código no es 2xx
    datos = respuesta.json()

    if not datos.get("results"):
        return None

    resultado = datos["results"][0]
    return resultado["latitude"], resultado["longitude"], resultado["name"]


def obtener_tiempo(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    respuesta = requests.get(
        url,
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,wind_speed_10m",
        },
        timeout=5,
    )
    respuesta.raise_for_status()
    return respuesta.json()["current"]


while True:
    ciudad = input("Ciudad (o 'salir'): ").strip()

    if ciudad.lower() == "salir":
        break
    if not ciudad:
        continue

    try:
        coordenadas = obtener_coordenadas(ciudad)
        if coordenadas is None:
            print(f"No encontré la ciudad '{ciudad}'")
            continue

        lat, lon, nombre = coordenadas
        tiempo = obtener_tiempo(lat, lon)
        print(f"{nombre}: {tiempo['temperature_2m']} °C, viento {tiempo['wind_speed_10m']} km/h")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        break

from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# Función para obtener las coordenadas geográficas de una ciudad
def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="calculador_viaje")
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# Función para calcular la duración del viaje en base a la distancia y velocidad del medio de transporte
def calcular_viaje(ciudad_origen, ciudad_destino, medio_de_transporte):
    coordenadas_origen = obtener_coordenadas(ciudad_origen)
    coordenadas_destino = obtener_coordenadas(ciudad_destino)

    if coordenadas_origen and coordenadas_destino:
        distancia_km = geodesic(coordenadas_origen, coordenadas_destino).kilometers

        # Velocidades promedio estimadas según el medio de transporte en km/h
        velocidad_auto = 80
        velocidad_avion = 800

        # Calcular duración del viaje según el medio de transporte
        if medio_de_transporte == 'auto':
            duracion_horas = distancia_km / velocidad_auto
        elif medio_de_transporte == 'avion':
            duracion_horas = distancia_km / velocidad_avion
        else:
            duracion_horas = None

        if duracion_horas is not None:
            duracion_horas = round(duracion_horas, 2)
            distancia_millas = distancia_km * 0.621371  # Convertir kilómetros a millas
            duracion_horas_avion = round(distancia_km / velocidad_avion, 2)

            # Mostrar resultados
            print(f"Distancia entre {ciudad_origen.capitalize()} y {ciudad_destino.capitalize()}:")
            print(f"- {distancia_km:.2f} kilómetros / {distancia_millas:.2f} millas")
            print(f"Duración del viaje en {medio_de_transporte}: {duracion_horas:.2f} horas")

            # Mostrar narrativa del viaje
            print(f"Narrativa del viaje: Viajando desde {ciudad_origen.capitalize()} hasta {ciudad_destino.capitalize()} en {medio_de_transporte}.")

        else:
            print("Opción de medio de transporte no válida.")

    else:
        print("No se pudo obtener información de ubicación para una o ambas ciudades.")

# Función principal
def main():
    print("Bienvenido al sistema de cálculo de viaje")

    while True:
        ciudad_origen = input("Ingrese la Ciudad de Origen (Chile): ").strip().lower()
        ciudad_destino = input("Ingrese la Ciudad de Destino (Argentina): ").strip().lower()

        medio_de_transporte = input("Seleccione el medio de transporte (auto/avion): ").strip().lower()

        calcular_viaje(ciudad_origen, ciudad_destino, medio_de_transporte)

        opcion = input("¿Desea calcular otro viaje? (s/n): ").strip().lower()
        if opcion != 's':
            break

    print("Gracias por utilizar nuestro sistema de cálculo de viaje.")

if __name__ == "__main__":
    main()

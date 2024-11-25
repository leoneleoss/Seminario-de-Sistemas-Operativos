import threading
import time
import random

class Auto:
    def __init__(self, id_auto):
        self.id_auto = id_auto

    def __repr__(self):
        return f"Auto({self.id_auto})"

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.estacionamiento = []
        self.lock = threading.Lock()

    def añadir_auto(self, auto):
        with self.lock:
            if len(self.estacionamiento) < self.capacidad:
                self.estacionamiento.append(auto)
                print(f"Auto {auto.id_auto} añadido. Total: {len(self.estacionamiento)}")
            else:
                print("Estacionamiento lleno. No se puede añadir más autos.")

    def retirar_auto(self):
        with self.lock:
            if self.estacionamiento:
                auto = self.estacionamiento.pop(0)
                print(f"Auto {auto.id_auto} retirado. Total: {len(self.estacionamiento)}")
            else:
                print("Estacionamiento vacío. No se puede retirar autos.")

def añadir_autos(estacionamiento, frecuencia_entrada):
    id_auto = 1
    while True:
        auto = Auto(id_auto)
        estacionamiento.añadir_auto(auto)
        id_auto += 1
        time.sleep(frecuencia_entrada[0])

def retirar_autos(estacionamiento, frecuencia_salida):
    while True:
        estacionamiento.retirar_auto()
        time.sleep(frecuencia_salida[0])

def cambiar_frecuencia(frecuencia, tipo):
    while True:
        try:
            nueva_frecuencia = float(input(f"Ingrese nueva frecuencia para {tipo} (0.5, 1 o 2 segundos): "))
            if nueva_frecuencia in [0.5, 1, 2]:
                frecuencia[0] = nueva_frecuencia
                print(f"Frecuencia de {tipo} actualizada a {nueva_frecuencia} segundos.")
            else:
                print("Frecuencia inválida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

def main():
    capacidad = 12
    estacionamiento = Estacionamiento(capacidad)

    frecuencia_entrada = [random.choice([0.5, 1, 2])]
    frecuencia_salida = [random.choice([0.5, 1, 2])]

    hilo_entrada = threading.Thread(target=añadir_autos, args=(estacionamiento, frecuencia_entrada), daemon=True)
    hilo_salida = threading.Thread(target=retirar_autos, args=(estacionamiento, frecuencia_salida), daemon=True)

    hilo_frecuencia_entrada = threading.Thread(target=cambiar_frecuencia, args=(frecuencia_entrada, "entrada"), daemon=True)
    hilo_frecuencia_salida = threading.Thread(target=cambiar_frecuencia, args=(frecuencia_salida, "salida"), daemon=True)

    hilo_entrada.start()
    hilo_salida.start()
    hilo_frecuencia_entrada.start()
    hilo_frecuencia_salida.start()

    print("Programa de estacionamiento iniciado. Presione Ctrl+C para salir.")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

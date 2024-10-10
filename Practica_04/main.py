import os
import csv
from collections import deque
from prettytable import PrettyTable

# Función para cargar los procesos desde el archivo .txt
def cargar_procesos(archivo):
    procesos = []
    with open(archivo, 'r') as file:
        lector_csv = csv.reader(file)
        for linea in lector_csv:
            proceso = linea[0]
            duracion = int(linea[1])
            prioridad = int(linea[2])
            procesos.append([proceso, duracion, prioridad])
    return procesos

# Función para mostrar procesos en formato tabla usando PrettyTable
def mostrar_procesos_tabla(procesos):
    tabla = PrettyTable()
    tabla.field_names = ["Nombre del Proceso", "Duración", "Prioridad"]

    for proceso in procesos:
        tabla.add_row(proceso)

    print(tabla)

# Función para simular el algoritmo FIFO
def fifo(procesos):
    print("\nAlgoritmo FIFO:")
    tabla = PrettyTable()
    tabla.field_names = ["Nombre del Proceso", "Duración", "Prioridad", "Orden de Ejecución"]

    for i, proceso in enumerate(procesos, start=1):
        tabla.add_row([proceso[0], proceso[1], proceso[2], i])

    print(tabla)
    tiempo_total = sum(p[1] for p in procesos)
    print(f"Tiempo total de ejecución: {tiempo_total} unidades de tiempo")

# Función para simular el algoritmo SJF
def sjf(procesos):
    print("\nAlgoritmo SJF:")
    procesos_ordenados = sorted(procesos, key=lambda x: x[1])  # Ordenar solo por duración
    tabla = PrettyTable()
    tabla.field_names = ["Nombre del Proceso", "Duración", "Prioridad", "Orden de Ejecución"]

    for i, proceso in enumerate(procesos_ordenados, start=1):
        tabla.add_row([proceso[0], proceso[1], proceso[2], i])

    print(tabla)
    tiempo_total = sum(p[1] for p in procesos_ordenados)
    print(f"\nTiempo total de ejecución: {tiempo_total} unidades de tiempo")

# Función para simular el algoritmo de Prioridades
def prioridades(procesos):
    print("\nAlgoritmo de Prioridades:")
    procesos_ordenados = sorted(procesos, key=lambda x: x[2])  # Ordenar solo por prioridad
    tabla = PrettyTable()
    tabla.field_names = ["Nombre del Proceso", "Duración", "Prioridad", "Orden de Ejecución"]

    for i, proceso in enumerate(procesos_ordenados, start=1):
        tabla.add_row([proceso[0], proceso[1], proceso[2], i])

    print(tabla)
    tiempo_total = sum(p[1] for p in procesos_ordenados)
    print(f"\nTiempo total de ejecución: {tiempo_total} unidades de tiempo")

# Función para simular el algoritmo Round Robin
def round_robin(procesos, quantum=3):
    print("\nAlgoritmo Round Robin (Quantum = 3):")
    
    # Ordenar los procesos por prioridad antes de ejecutar el algoritmo
    procesos_ordenados = sorted(procesos, key=lambda x: x[2])  # Ordenar solo por prioridad
    cola_rr = deque(procesos_ordenados)
    tiempo_total = 0
    procesos_restantes = {p[0]: p[1] for p in procesos_ordenados}  # Diccionario de tiempos restantes

    # Mostrar encabezados de la tabla
    tabla = PrettyTable()
    tabla.field_names = ["Nombre del Proceso", "Tiempo Ejecutado", "Tiempo Restante", "Prioridad", "Tiempo Total"]

    # Mientras haya procesos en la cola
    while cola_rr:
        proceso = cola_rr.popleft()  # Tomar el primer proceso de la cola
        nombre, duracion, prioridad = proceso
        
        # Calcular el tiempo ejecutado en esta ronda
        tiempo_ejecucion = min(duracion, quantum)
        duracion -= tiempo_ejecucion
        tiempo_total += tiempo_ejecucion
        
        # Guardar el tiempo restante
        procesos_restantes[nombre] = duracion

        # Mostrar los resultados en la tabla
        tabla.add_row([nombre, tiempo_ejecucion, duracion, prioridad, tiempo_total])

        # Si el proceso no ha terminado, lo devolvemos a la cola
        if duracion > 0:
            cola_rr.append([nombre, duracion, prioridad])
    
    print(tabla)
    print(f"Tiempo total de ejecución: {tiempo_total} unidades de tiempo")

    
# Función principal
def main():
    archivo = input("Ingresa la ruta del archivo de procesos: ")
    procesos = cargar_procesos(archivo)

    # Mostrar los procesos en formato tabla
    print("\nProcesos cargados desde el archivo:")
    mostrar_procesos_tabla(procesos)

    # Ejecutar los algoritmos
    fifo(procesos)
    sjf(procesos)
    prioridades(procesos)
    round_robin(procesos)

if __name__ == "__main__":
    main()

# **PRACTICA 03 -  Algoritmos de Planificación (1) **

## **Antecedentes (Contexto)**
La planificación de procesos es un componente fundamental en la gestión de sistemas operativos, responsable de la asignación eficiente de recursos del sistema y la optimización del uso del tiempo de CPU. 
Este proyecto se centra en la simulación de dos algoritmos de planificación: FIFO (First In, First Out) y SJF (Shortest Job First). 
A través de la carga de procesos desde un archivo de texto, se busca facilitar la comprensión de la dinámica de estos algoritmos en un entorno práctico.

## **Metodología**

### Librerías Utilizadas
- **`csv`**: Para la lectura de datos desde un archivo de texto en formato CSV.
- **`prettytable`**: Para la visualización de procesos y resultados en un formato tabular legible.

### Funciones y Algoritmos
1. **`cargar_procesos(archivo):`** 
   - **Método utilizado**: Se utiliza la función `csv.reader()` para leer el archivo CSV que contiene los procesos.
   - Cada línea se descompone en nombre del proceso, duración y prioridad, que se almacenan en una lista.
   
     ```python
     with open(archivo, 'r') as file:
         lector_csv = csv.reader(file)
         for linea in lector_csv:
             proceso = linea[0]
             duracion = int(linea[1])
             prioridad = int(linea[2])
             procesos.append([proceso, duracion, prioridad])
     ```

2. **`mostrar_procesos_tabla(procesos): `**
   - **Método utilizado**: Utiliza `PrettyTable` para crear y mostrar una tabla con los procesos cargados, facilitando la visualización de datos.
   - Se añaden las filas a la tabla mediante un bucle que recorre la lista de procesos.
   
     ```python
     for proceso in procesos:
         tabla.add_row(proceso)
     ```

3. **`fifo(procesos): `**
   - **Método utilizado**: Este algoritmo procesa los procesos en el orden en que fueron cargados (FIFO).
   Se crea una tabla que muestra cada proceso, su duración, prioridad y su orden de ejecución. El tiempo total de ejecución se calcula sumando la duración de todos los procesos.
   
     ```python
     for i, proceso in enumerate(procesos, start=1):
         tabla.add_row([proceso[0], proceso[1], proceso[2], i])
     tiempo_total = sum(p[1] for p in procesos)
     ```

4. **`sjf(procesos): `**
   - **Método utilizado**: Este algoritmo ordena los procesos según su duración (de menor a mayor) utilizando la función `sorted()` y una función lambda como clave.
   - Luego, se crea una tabla similar a la de FIFO, mostrando el orden de ejecución basado en la duración. El tiempo total se calcula de la misma manera.
   
     ```python
     procesos_ordenados = sorted(procesos, key=lambda x: x[1])  # Ordenar solo por duración
     for i, proceso in enumerate(procesos_ordenados, start=1):
         tabla.add_row([proceso[0], proceso[1], proceso[2], i])
     tiempo_total = sum(p[1] for p in procesos_ordenados)
     ```

#### **Estructura del Programa**:
El programa comienza solicitando la ruta del archivo que contiene la información de los procesos. Luego, carga y muestra los procesos, seguido de la ejecución de los algoritmos FIFO y SJF, mostrando los resultados en tablas organizadas.

## **Conclusión**
El código presenta una simulación efectiva de los algoritmos FIFO y SJF para la planificación de procesos. Permite cargar procesos desde un archivo de texto, visualizar la información de manera clara y calcular el tiempo total de ejecución para cada algoritmo.

### Aspectos Funcionales:
- Carga de procesos desde un archivo.
- Visualización de procesos en formato tabla.
- Simulación y cálculo de tiempos de ejecución de los algoritmos FIFO y SJF.

### Áreas de Mejora:
- Implementación de otros algoritmos de planificación (como Round Robin o Prioridad).
- Manejo de errores en la carga de archivos para mejorar la robustez.
- Opción para que el usuario elija el algoritmo a utilizar.

## **Referencias**
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
- Tanenbaum, A. S., & Austin, T. (2012). *Operating Systems: Design and Implementation* (3rd ed.). Prentice Hall.
- PrettyTable. (n.d.). *PrettyTable Documentation*. Retrieved from [https://pypi.org/project/prettytable/](https://pypi.org/project/prettytable/)

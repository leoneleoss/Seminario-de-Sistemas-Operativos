# **Simulación de Algoritmos de Planificación de Procesos (FIFO, SJF, Prioridades, Round Robin)**

## **Antecedentes (Contexto)**
Este proyecto simula los algoritmos de planificación de procesos Prioridades y Round Robin, en adición a los algoritmos ya implementados (FIFO y SJF). La planificación de procesos es crucial en los sistemas operativos para gestionar eficientemente la ejecución de múltiples tareas. 
El algoritmo de Prioridades se enfoca en ejecutar procesos según su prioridad asignada, mientras que Round Robin distribuye equitativamente el tiempo de CPU entre los procesos con un quantum definido.

## **Metodología**

### Librerías Utilizadas
- **`csv`**: Para leer los datos de procesos desde un archivo en formato CSV.
- **`collections.deque`**: Para implementar una cola eficiente en el algoritmo de Round Robin.
- **`prettytable`**: Para visualizar los procesos y resultados en tablas.

### Funciones y Algoritmos

1. **`prioridades(procesos):`**: 
   - **Método utilizado**: La función `sorted()` ordena los procesos según su prioridad de menor a mayor. El proceso con la menor prioridad numérica se ejecuta primero.
   
        ```python
        procesos_ordenados = sorted(procesos, key=lambda x: x[2])  # Ordenar por prioridad
        for i, proceso in enumerate(procesos_ordenados, start=1):
            tabla.add_row([proceso[0], proceso[1], proceso[2], i])
        ```

2. **`round_robin(procesos, quantum=3)`**: 
   - **Método utilizado**: Round Robin es un algoritmo que asigna a cada proceso un tiempo fijo de ejecución (quantum). Si un proceso no termina en ese tiempo, se vuelve a poner en la cola de procesos. Aquí, `collections.deque` permite la rotación eficiente de procesos. La función también controla el tiempo restante de cada proceso en cada ronda.

    #### **Funcionamiento**:

    - **Cola de Procesos**: Se utiliza una **cola** (`deque`) para gestionar los procesos de forma cíclica. Los procesos se ordenan inicialmente por prioridad, y luego se manejan en ciclos.

        ```python
        cola_rr = deque(procesos_ordenados)
        ```
    - **Ejecución por Quantum**: Cada proceso se ejecuta durante un máximo de 3 unidades de tiempo. Si un proceso requiere más tiempo, se coloca de nuevo en la cola para ser ejecutado en el siguiente ciclo.

       ```python
            tiempo_ejecucion = min(duracion, quantum)
            duracion -= tiempo_ejecucion
       ```
    - **Actualización de Tiempos**: La función mantiene un registro del tiempo ejecutado y del tiempo restante para cada proceso. Los procesos que no hayan terminado su ejecución vuelven a la cola hasta que se completen. Luego se muestra en consola en forma de tabla

        ```python
        procesos_restantes[nombre] = duracion
        if duracion > 0:
        cola_rr.append([nombre, duracion, prioridad])

        tabla.add_row([nombre, tiempo_ejecucion, duracion, prioridad, tiempo_total])
        ```

#### **Estructura del Programa**:
El programa inicia solicitando un archivo de texto que contiene los procesos a planificar. Luego, estos se muestran en formato tabla y se ejecutan los algoritmos en el siguiente orden: FIFO, SJF, Prioridades y Round Robin. Cada algoritmo visualiza sus resultados en tablas y calcula el tiempo total de ejecución de los procesos.

## **Conclusión**
El código desarrollado ofrece una simulación clara y detallada de varios algoritmos de planificación de procesos. Se cargan procesos desde un archivo de texto, y se visualizan y ejecutan con diferentes estrategias de planificación, permitiendo observar el comportamiento y eficiencia de cada uno.

### Aspectos Funcionales:
- Simulación correcta de los algoritmos Prioridades y Round Robin.
- Control del quantum en Round Robin, donde los procesos se rotan hasta que todos se completan.
- Visualización clara de los resultados en tablas, incluyendo tiempos de ejecución y tiempos restantes para Round Robin.

### Áreas de Mejora:
- Podría mejorarse la gestión dinámica del quantum en Round Robin.
- Agregar controles para procesos con tiempos negativos o datos inválidos en el archivo de entrada.

## **Referencias**
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
- Container datatypes. (s. f.). Python Documentation. etrieved from [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
- PrettyTable. (n.d.). *PrettyTable Documentation*. Retrieved from [https://pypi.org/project/prettytable/](https://pypi.org/project/prettytable/)

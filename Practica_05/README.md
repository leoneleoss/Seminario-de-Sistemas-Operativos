# PRACTICA 05 -  Algoritmos de Planificación (3)

## **Antecedentes (Contexto)**

Este proyecto implementa una simulación de diferentes algoritmos de planificación de procesos, utilizando un archivo `.txt` que contiene una lista de procesos con su nombre, duración y prioridad. La simulación permite probar algoritmos como Round Robin, FIFO, SJF y planificación basada en prioridades. 
El objetivo principal es ayudar a entender cómo se gestionan los procesos en un sistema operativo a través de estas técnicas.

## **Metodología**

### Librerías Utilizadas
- **os**: Se utiliza para limpiar la consola durante la ejecución del programa.
- **csv**: Permite la lectura de archivos `.txt` como archivos delimitados por comas.
- **collections.deque**: Ayuda en la implementación del algoritmo Round Robin para gestionar la cola de procesos.
- **prettytable**: Facilita la visualización de los datos de los procesos en formato tabla.

### Funciones y Algoritmos
- **cargar_procesos(archivo)**: Carga los procesos desde el archivo `.txt` con su nombre, duración y prioridad.
- **agregar_procesos(procesos, archivo)**: Permite agregar nuevos procesos en tiempo real al archivo de procesos.
- **mostrar_procesos_tabla(procesos)**: Muestra los procesos en una tabla, usando PrettyTable.
- **fifo(procesos)**: Simula el algoritmo **First In, First Out (FIFO)**, donde los procesos se ejecutan en el orden de llegada.
- **sjf(procesos)**: Simula el algoritmo **Shortest Job First (SJF)**, donde los procesos con menor duración son ejecutados primero.
- **prioridades(procesos)**: Simula un algoritmo de planificación basado en la **prioridad** de cada proceso.
- **round_robin(procesos, quantum=3)**: Simula el algoritmo **Round Robin** con un quantum de 3 unidades de tiempo, organizando los procesos según su prioridad.

#### **Estructura del Programa**:
1. **Carga de procesos**: Se inicia cargando los procesos desde un archivo `.txt`.
2. **Selección de algoritmo**: El usuario elige qué algoritmo de planificación desea simular.
3. **Ejecución de algoritmos**: Dependiendo del algoritmo elegido, se muestra la ejecución en una tabla con detalles sobre el tiempo de ejecución, tiempo restante y prioridad.
4. **Adición de procesos**: Se permite agregar nuevos procesos, con la opción de colocarlos al inicio o al final de la lista de procesos, ademas de guardarlos en archivo.
5. **Visualización de resultados**: Se muestran los resultados de la ejecución de los algoritmos en tablas para una mejor comprensión.

## **Conclusión**

El programa entrega una simulación completa de los algoritmos de planificación de procesos, permitiendo entender el comportamiento de cada uno en un contexto práctico.

### Aspectos Funcionales:
El programa simula de manera efectiva los algoritmos de planificación de procesos FIFO, SJF, Round Robin y Prioridades. 
Las tablas generadas por **PrettyTable** permiten una visualización clara del orden de ejecución y los tiempos de cada proceso. 
Además, se ha implementado la funcionalidad de agregar nuevos procesos dinámicamente durante la ejecución del programa y un menu para elegir entre los algoritmos

### Áreas de Mejora:
- Mejorar el manejo de errores para asegurar que los datos ingresados sean válidos (por ejemplo, prevenir que se ingresen duraciones negativas o prioridades no válidas).
- Implementar una interfaz gráfica para una mejor experiencia del usuario.
- Extender la funcionalidad del algoritmo Round Robin para que el quantum sea configurable dinámicamente por el usuario.

## **Referencias**

Villalobos, J. (2021). *Python para impacientes*. TecnoBillo.  
Educative (2023). *Concurrent Programming in Python*. Educative.  
StatusNeo (2023). *Multithreading and Concurrency in Python*. StatusNeo.

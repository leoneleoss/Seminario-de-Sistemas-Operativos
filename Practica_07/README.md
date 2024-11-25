# PRACTICA 07 -  Administracion de Memoria (2)

## **Antecedentes (Contexto)**

Esta práctica tiene como objetivo implementar diferentes algoritmos de administración de memoria en un sistema operativo simulado utilizando la librería `Tkinter` en Python. La simulación consiste en asignar bloques de memoria a archivos según diferentes estrategias, como Primer Ajuste, Mejor Ajuste, Peor Ajuste y Siguiente Ajuste. Se presenta una interfaz gráfica que permite al usuario interactuar con los algoritmos y visualizar cómo se asignan los bloques de memoria a los archivos.

## **Metodología**

### Librerías Utilizadas

- **Tkinter**: Se utilizó para crear la interfaz gráfica que permite visualizar la asignación de memoria, interactuar con los algoritmos y cargar los archivos desde un archivo `.txt`.

### Funciones y Algoritmos

#### **Estructura del Programa**:

El programa está estructurado en una clase llamada `MemoriaApp`, que gestiona la interfaz gráfica y la lógica de los algoritmos de asignación de memoria. Los algoritmos de asignación de memoria disponibles son:

1. **Primer Ajuste (First Fit)**: Asigna un archivo al primer bloque de memoria que sea lo suficientemente grande para alojarlo.
2. **Mejor Ajuste (Best Fit)**: Asigna el archivo al bloque de memoria que mejor se ajuste a su tamaño.
3. **Peor Ajuste (Worst Fit)**: Asigna el archivo al bloque de memoria más grande disponible.
4. **Siguiente Ajuste (Next Fit)**: Similar al Primer Ajuste, pero comenzando desde el último bloque asignado.

#### **Funciones utilizadas**:

1. **`primer_ajuste(memoria, archivos)`**:
   - **Descripción**: Implementa el algoritmo de Primer Ajuste. Asigna los archivos a los primeros bloques de memoria que sean lo suficientemente grandes para alojarlos.
   - **Parámetros**:
     - `memoria`: Lista de bloques de memoria disponibles.
     - `archivos`: Lista de tuplas que representan los archivos a asignar (nombre, tamaño).
   - **Salida**: Lista de archivos asignados a los bloques de memoria correspondientes.

2. **`mejor_ajuste(memoria, archivos`)**:
   - **Descripción**: Implementa el algoritmo de Mejor Ajuste. Asigna los archivos al bloque de memoria que mejor se ajuste a su tamaño, buscando el bloque más pequeño que sea lo suficientemente grande.
   - **Parámetros**:
     - `memoria`: Lista de bloques de memoria disponibles.
     - `archivos`: Lista de tuplas que representan los archivos a asignar (nombre, tamaño).
   - **Salida**: Lista de archivos asignados a los bloques de memoria correspondientes.

3. **`peor_ajuste(memoria, archivos)`**:
   - **Descripción**: Implementa el algoritmo de Peor Ajuste. Asigna los archivos al bloque de memoria más grande disponible.
   - **Parámetros**:
     - `memoria`: Lista de bloques de memoria disponibles.
     - `archivos`: Lista de tuplas que representan los archivos a asignar (nombre, tamaño).
   - **Salida**: Lista de archivos asignados a los bloques de memoria correspondientes.

4. **`siguiente_ajuste(memoria, archivos)`**:
   - **Descripción**: Implementa el algoritmo de Siguiente Ajuste. Asigna los archivos comenzando desde el último bloque asignado y continúa en el siguiente bloque disponible.
   - **Parámetros**:
     - `memoria`: Lista de bloques de memoria disponibles.
     - `archivos`: Lista de tuplas que representan los archivos a asignar (nombre, tamaño).
   - **Salida**: Lista de archivos asignados a los bloques de memoria correspondientes.

### **Interfaz Gráfica**:

La interfaz gráfica utiliza la librería `Tkinter` para crear los siguientes componentes:

- **Radiobuttons** para seleccionar el algoritmo de administración de memoria (Primer Ajuste, Mejor Ajuste, Peor Ajuste, Siguiente Ajuste).
- **Botón para cargar archivos**: Permite al usuario cargar un archivo `.txt` que contiene la lista de archivos a asignar.
- **Botón para asignar archivos**: Ejecuta el algoritmo seleccionado y muestra la asignación de memoria.
- **Canvas**: Muestra visualmente los bloques de memoria y los archivos asignados en un diseño gráfico.

## **Conclusión**

### Aspectos Funcionales:

- El programa permite seleccionar y visualizar la asignación de archivos a bloques de memoria utilizando diferentes algoritmos de administración de memoria.
- La interfaz gráfica facilita la interacción con el programa y la comprensión de cómo los diferentes algoritmos asignan los recursos de memoria.

### Áreas de Mejora:

- Actualmente, los bloques de memoria y los archivos se representan de manera simple. Se podrían agregar más detalles visuales para mejorar la comprensión de la asignación de memoria.
- Los algoritmos podrían optimizarse para manejar casos más complejos, como la fragmentación interna y externa, y permitir una mejor gestión de la memoria.

## **Referencias**

- **Tkinter Documentation**: [https://docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- **Algoritmos de administración de memoria**: Conceptos sobre Primer Ajuste, Mejor Ajuste, Peor Ajuste y Siguiente Ajuste adaptados de la literatura de administración de sistemas operativos.

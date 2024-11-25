# PRACTICA 08 - Administración de Memoria (3)

## **Antecedentes (Contexto)**

La administración de memoria es una de las funciones clave en los sistemas operativos modernos. Su objetivo principal es gestionar de manera eficiente el espacio de memoria disponible, asignando y liberando bloques de memoria según sea necesario para que los programas en ejecución puedan acceder a los recursos de manera adecuada. En esta práctica, se implementan varios algoritmos de administración de memoria: Primer Ajuste, Mejor Ajuste, Peor Ajuste y Siguiente Ajuste. Cada uno tiene su propia estrategia para asignar bloques de memoria a los procesos que requieren espacio.

## **Metodología**

### Librerías Utilizadas

El programa se desarrolla utilizando la librería `tkinter` para la creación de la interfaz gráfica de usuario (GUI). Además, se emplean funciones estándar de Python como `filedialog` y `messagebox` para interactuar con archivos y mostrar mensajes emergentes.

- `tkinter`: Para crear la interfaz gráfica, gestionar la interacción del usuario y dibujar la memoria.
- `filedialog`: Para seleccionar archivos de texto donde se almacenan los archivos virtuales.
- `messagebox`: Para mostrar mensajes de error o confirmación al usuario.

### Funciones, Clases y Algoritmos

#### **Estructura del Programa**:

El programa consta de varias funciones y clases para implementar la interfaz gráfica y los algoritmos de administración de memoria. Los algoritmos implementados son:

1. **Primer Ajuste**: Asigna un bloque de memoria al primer espacio libre que sea suficientemente grande.
2. **Mejor Ajuste**: Asigna el bloque de memoria al espacio libre más pequeño que sea adecuado para el archivo.
3. **Peor Ajuste**: Asigna el bloque de memoria al espacio libre más grande disponible.
4. **Siguiente Ajuste**: Asigna el bloque de memoria al primer espacio disponible a partir del último bloque asignado.

El código contiene una clase `MemoriaApp`, que implementa la GUI donde los usuarios pueden interactuar con los algoritmos de administración de memoria y realizar las asignaciones de memoria a los archivos.

#### **Funcionamiento del Programa**:

1. **Agregar Bloques de Memoria**: Permite agregar bloques de memoria al sistema, especificando el tamaño y estado (disponible u ocupado).
2. **Agregar Archivos Virtuales**: Los usuarios pueden ingresar archivos con un nombre y tamaño para que sean asignados a la memoria.
3. **Asignar Archivos**: Al seleccionar un algoritmo de asignación, el programa realiza la asignación de los archivos a los bloques de memoria utilizando el algoritmo seleccionado.
4. **Limpiar Memoria**: Esta opción permite reiniciar la memoria, eliminando todos los bloques.

## **Conclusión**

### Aspectos Funcionales:

El programa cumple con la finalidad de simular la administración de memoria en un sistema operativo. Los algoritmos de asignación de memoria funcionan correctamente y permiten visualizar cómo se asignan los bloques de memoria a los archivos en función del algoritmo seleccionado. La interfaz gráfica es fácil de usar y permite al usuario interactuar con la simulación de forma intuitiva.

### Áreas de Mejora:

- **Interactividad**: Se podrían agregar más opciones para mostrar información detallada sobre los bloques de memoria y los archivos asignados.
- **Optimización de Recursos**: Mejorar la eficiencia de la visualización y de la asignación de memoria, especialmente en situaciones con grandes cantidades de bloques y archivos.
- **Compatibilidad**: Se podría mejorar la carga de archivos y la gestión de la memoria para funcionar mejor en diferentes sistemas operativos.

## **Referencias**

- Documentación oficial de [Tkinter](https://docs.python.org/3/library/tkinter.html).


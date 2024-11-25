# PRACTICA 06 - Administrador de memoria

## **Antecedentes (Contexto)**
La práctica consiste en la implementación de algoritmos de administración de memoria (Primer Ajuste y Mejor Ajuste) en un entorno visual interactivo utilizando la biblioteca `tkinter` en Python. La aplicación permite simular la asignación de bloques de memoria a archivos, demostrando cómo cada algoritmo asigna espacio de manera eficiente.

## **Metodología**

### Librerías Utilizadas
- `tkinter`: Utilizado para la creación de la interfaz gráfica de usuario (GUI).
- `filedialog`: Proporciona una ventana para seleccionar un archivo, permitiendo cargar datos desde un archivo `.txt`.

### Funciones y Algoritmos

#### **Estructura del Programa**:
1. **Clase `MemoriaApp`**: Controla la interfaz gráfica, las interacciones con el usuario y la gestión de los algoritmos.
   - `__init__()`: Inicializa los componentes de la interfaz.
   - `create_widgets()`: Crea y organiza los widgets en la ventana.
   - `cargar_archivos()`: Carga un archivo de texto con la lista de archivos y tamaños.
   - `asignar_archivos()`: Ejecuta el algoritmo seleccionado y muestra la asignación de memoria.
   - `dibujar_memoria()`: Dibuja los bloques de memoria y los archivos asignados en el lienzo.
   - `limpiar_memoria()`: Resetea la memoria y limpia el lienzo.
   - `redibujar_memoria()`: Redibuja la memoria cuando el tamaño de la ventana cambia.

2. **Funciones de los Algoritmos de Administración de Memoria**:
   - **`primer_ajuste(memoria, archivos)`**: Asigna archivos a los primeros bloques de memoria que sean lo suficientemente grandes.
   - **`mejor_ajuste(memoria, archivos)`**: Asigna archivos al bloque más pequeño que pueda acomodar el archivo.

## **Conclusión**

### Aspectos Funcionales:
- La aplicación permite simular la asignación de bloques de memoria a archivos utilizando dos algoritmos populares.
- La interfaz gráfica facilita la visualización del estado de la memoria y los archivos asignados, mejorando la comprensión de cómo funcionan los algoritmos de administración de memoria.

### Áreas de Mejora:
- Implementar un algoritmo de peor ajuste para comparar el rendimiento con los otros dos.
- Añadir validación para manejar errores en los archivos cargados (por ejemplo, formatos incorrectos).
- Mejorar la interfaz para mostrar información más detallada sobre la memoria y los archivos asignados.

## **Referencias**
- Python Tkinter Documentation: https://docs.python.org/3/library/tkinter.html

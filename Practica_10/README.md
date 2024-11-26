# PRACTICA 10 - Productor - Consumidor 1 (Estacionamiento)

## **Antecedentes (Contexto)**
El objetivo de esta práctica es implementar un simulador de estacionamiento con capacidad limitada, utilizando una interfaz gráfica para visualizar los espacios ocupados y libres. La simulación debe permitir agregar y retirar autos de manera automática, controlando la frecuencia de estos eventos, y emplear concurrencia mediante hilos para garantizar la funcionalidad en tiempo real.

## **Metodología**

### Librerías Utilizadas
- **tkinter**: Para la creación de la interfaz gráfica de usuario.
- **threading**: Para la ejecución concurrente de los procesos de agregar y retirar autos.
- **time**: Para la gestión de los intervalos de tiempo en los procesos.
- **random**: Para la selección aleatoria de espacios en el estacionamiento y colores representativos de los autos.

### Funciones, Clases y Algoritmos

#### **Clase `Estacionamiento`**:
- **`__init__(capacidad)`**: Inicializa la capacidad del estacionamiento, una lista de espacios vacíos y un bloqueo para la concurrencia segura.
- **`agregar_auto(auto)`**: Agrega un auto en un espacio vacío, si está disponible. Usa un bloqueo para evitar conflictos de acceso.
- **`retirar_auto()`**: Retira un auto de un espacio ocupado de forma aleatoria. También usa un bloqueo para evitar conflictos.

#### **Clase `App`**:
- **`__init__(root)`**: Configura la ventana principal y los hilos para agregar y retirar autos.
- **`create_ui()`**: Crea los elementos de la interfaz gráfica, incluyendo el lienzo para los espacios del estacionamiento y controles para ajustar las frecuencias.
- **`actualizar_frecuencia_agregar()`** y **`actualizar_frecuencia_retirar()`**: Permiten modificar las frecuencias de los procesos desde la interfaz.
- **`auto_agregar()`** y **`auto_retirar()`**: Funciones ejecutadas por hilos para manejar los procesos de agregar y retirar autos.
- **`actualizar_textbox(textbox, mensaje)`**: Actualiza los cuadros de texto de entrada y salida con mensajes sobre el estado del estacionamiento.

#### **Estructura del Programa**:
1. Inicialización del estacionamiento con capacidad fija.
2. Configuración de la interfaz gráfica con controles para ajustar parámetros.
3. Ejecución de hilos concurrentes para simular el agregado y retiro de autos.
4. Visualización en tiempo real de los cambios en el estacionamiento.

## **Conclusión**

### Aspectos Funcionales:
- El simulador permite agregar y retirar autos de manera dinámica, respetando la capacidad del estacionamiento.
- La interfaz gráfica facilita la comprensión visual de los estados del estacionamiento.
- El uso de hilos asegura que los procesos de agregado y retiro se ejecuten de manera concurrente sin bloqueos.

### Áreas de Mejora:
- Implementar un sistema de prioridad para el agregado o retiro de autos.
- Agregar un registro histórico de los autos ingresados y retirados.
- Optimizar el manejo de colores para una mejor experiencia visual.

## **Referencias**
- Documentación oficial de Python: 
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [threading](https://docs.python.org/3/library/threading.html)
- [time](https://docs.python.org/3/library/time.html)
- [random](https://docs.python.org/3/library/random.html)

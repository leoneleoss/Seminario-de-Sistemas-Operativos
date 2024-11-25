# PRACTICA 09 - Hilos

## **Antecedentes (Contexto)**

En esta práctica se explora el uso de hilos para animar elementos gráficos en una interfaz de usuario construida con `tkinter` y `Pillow` en Python. Se simula el movimiento de dos imágenes en direcciones opuestas, mostrando cómo los hilos permiten la ejecución simultánea de dos tareas, lo que es útil para la animación en tiempo real. Además, se implementan los cambios de dirección de las imágenes al colisionar con los bordes del lienzo, lo que demuestra cómo manejar interacciones y eventos en tiempo real usando múltiples hilos.

## **Metodología**

La animación de las imágenes se logra mediante dos hilos que ejecutan funciones distintas: una para mover una imagen de izquierda a derecha y la otra para mover una imagen de arriba hacia abajo. Ambos hilos se ejecutan de manera simultánea, permitiendo que las imágenes se desplacen y colisionen con los bordes, cambiando su dirección en cada colisión. 

Se utiliza el módulo `tkinter` para la creación de la interfaz gráfica, y `Pillow` para la manipulación de las imágenes. Los hilos son gestionados utilizando el módulo `threading` de Python, lo que permite el procesamiento concurrente sin bloquear la interfaz de usuario.

### Librerías Utilizadas

- `tkinter`: Para la creación de la interfaz gráfica y el lienzo donde se mueve las imágenes.
- `PIL` (Pillow): Para la carga y manipulación de las imágenes.
- `threading`: Para crear hilos que permiten la animación simultánea de las imágenes.
- `time`: Para controlar la velocidad del movimiento de las imágenes.

### Funciones y Algoritmos

#### **Estructura del Programa**:

1. **Función `move_left_to_right`**: 
   - Se encarga de mover la primera imagen de izquierda a derecha en el lienzo.
   - Si la imagen choca con los bordes, cambia de dirección y se mueve en la dirección contraria.
   - La función se ejecuta en un hilo independiente.

2. **Función `move_top_to_bottom`**:
   - Mueve la segunda imagen de arriba hacia abajo en el lienzo.
   - Al igual que la primera, cambia de dirección cuando choca con los bordes.
   - Esta función también se ejecuta en un hilo diferente.

3. **Función `start_animation`**:
   - Esta función es invocada cuando el usuario hace clic en el botón "Iniciar Animación".
   - Inicia los hilos para mover ambas imágenes y muestra un mensaje de inicio en el cuadro de texto.

4. **Interfaz Gráfica**:
   - La interfaz está formada por un lienzo donde se muestran las imágenes y un cuadro de texto donde se registran los mensajes de los hilos (por ejemplo, los cambios de dirección de las imágenes).

## **Conclusión**

### Aspectos Funcionales:

El programa cumple con el objetivo de demostrar el uso de hilos para realizar animaciones simultáneas en una interfaz gráfica. La animación de las imágenes, que se mueve de manera fluida en direcciones opuestas, es gestionada eficientemente mediante hilos. La interfaz de usuario es responsiva, lo que significa que se puede interactuar con ella mientras las animaciones ocurren en segundo plano.

### Áreas de Mejora:

- **Rendimiento**: Si bien el programa funciona bien en su forma actual, la animación podría beneficiarse de una mayor optimización en la gestión de hilos, especialmente si se añade más contenido o complejidad a la interfaz.
- **Control de hilos**: Actualmente, los hilos siguen ejecutándose indefinidamente. Se podría agregar una funcionalidad para detener los hilos cuando el usuario lo desee.
- **Mejor visualización de los mensajes de los hilos**: Los mensajes de los hilos en el cuadro de texto pueden volverse desordenados si el movimiento es rápido. Se podrían agregar más controles para gestionar el flujo de mensajes y evitar que se solapen.

## **Referencias**

- [Documentación de tkinter](https://docs.python.org/3/library/tkinter.html)
- [Documentación de Pillow](https://pillow.readthedocs.io/en/stable/)
- [Documentación de threading en Python](https://docs.python.org/3/library/threading.html)

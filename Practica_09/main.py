import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

def move_left_to_right(canvas, item, text_widget, image_width):
    # Mueve el elemento de izquierda a derecha y cambia de dirección al colisionar.
    dx = 5  # Velocidad en X
    while True:
        x, y = canvas.coords(item)  # Obtener las coordenadas centrales
        # Cambiar de dirección si choca con los bordes
        if x + image_width / 2 >= canvas.winfo_width() or x - image_width / 2 <= 0:
            dx = -dx
            text_widget.insert(tk.END, f"[Hilo 1] Cambio de dirección: dx={dx}\n")
        canvas.move(item, dx, 0)  # Mueve el objeto
        canvas.update()
        time.sleep(0.05)

def move_top_to_bottom(canvas, item, text_widget, image_height):
    # Mueve el elemento de arriba hacia abajo y cambia de dirección al colisionar."""
    dy = 5  # Velocidad en Y
    while True:
        x, y = canvas.coords(item)  # Obtener las coordenadas centrales
        # Cambiar de dirección si choca con los bordes
        if y + image_height / 2 >= canvas.winfo_height() or y - image_height / 2 <= 0:
            dy = -dy
            text_widget.insert(tk.END, f"[Hilo 2] Cambio de dirección: dy={dy}\n")
        canvas.move(item, 0, dy)  # Mueve el objeto
        canvas.update()
        time.sleep(0.05)

def start_animation():
    """Inicia la animación de las dos imágenes."""
    threading.Thread(target=move_left_to_right, args=(canvas, image_item1, text_widget, 100), daemon=True).start()
    threading.Thread(target=move_top_to_bottom, args=(canvas, image_item2, text_widget, 100), daemon=True).start()
    text_widget.insert(tk.END, "Hilos iniciados para el movimiento de las imágenes.\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Animación con Hilos y Colisión")
root.geometry("800x600")

# Crear el lienzo donde se moverán las imágenes
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Cargar las imágenes desde la carpeta actual
image_path1 = "Practica_09/cuyo.jpg"
image_path2 = "Practica_09/cuyo2.jpg"
image1 = Image.open(image_path1)
image1 = image1.resize((100, 100))  # Ajustar tamaño de la imagen
tk_image1 = ImageTk.PhotoImage(image1)

image2 = Image.open(image_path2)
image2 = image2.resize((100, 100))  # Ajustar tamaño de la imagen
tk_image2 = ImageTk.PhotoImage(image2)

# Calcular posiciones iniciales centradas
canvas_width = 600
canvas_height = 400
x_center = canvas_width // 2
y_center = canvas_height // 2

# Agregar las imágenes al lienzo
image_item1 = canvas.create_image(x_center - 100, y_center, image=tk_image1, anchor="center")  # A la izquierda del centro
image_item2 = canvas.create_image(x_center, y_center - 100, image=tk_image2, anchor="center")  # Arriba del centro

# Botón para iniciar la animación
start_button = tk.Button(root, text="Iniciar Animación", command=start_animation)
start_button.pack()

# Agregar un cuadro de texto para mostrar los procesos de los hilos
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_widget = tk.Text(text_frame, height=10, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=text_widget.yview)

# Mensaje inicial en el cuadro de texto
text_widget.insert(tk.END, "Preparando los hilos para animación...\n")

# Ejecutar la aplicación
root.mainloop()

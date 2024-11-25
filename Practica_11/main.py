import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import time

# Semáforos
file_lock = threading.Lock()  # Excluye escritores entre sí
reader_count_lock = threading.Lock()  # Protege el contador de lectores
reader_count = 0  # Número de lectores actualmente leyendo


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, "r") as file:
            return file.read()

    def write_file(self, content):
        with open(self.filename, "w") as file:
            file.write(content)


file_handler = FileHandler("shared_file.txt")


# Funciones para cada operación
def read_file(textbox):
    global reader_count
    with reader_count_lock:
        reader_count += 1
        if reader_count == 1:
            file_lock.acquire()  # Bloquea a los escritores

    content = file_handler.read_file()
    textbox.delete(1.0, tk.END)
    for char in content:
        textbox.insert(tk.END, char)
        textbox.update()
        time.sleep(0.1)  # Simula el delay por carácter

    with reader_count_lock:
        reader_count -= 1
        if reader_count == 0:
            file_lock.release()  # Libera a los escritores


def write_file(textbox):
    content = textbox.get(1.0, tk.END).strip()
    file_lock.acquire()  # Excluye a otros escritores y lectores
    file_handler.write_file(content)
    time.sleep(2)  # Simula el proceso de escritura
    file_lock.release()


def edit_file(textbox):
    textbox.config(state=tk.NORMAL)
    textbox.insert(tk.END, "\nEditing...\n")
    textbox.update()
    time.sleep(2)  # Simula el tiempo de edición
    textbox.delete("end-2l", "end")
    textbox.config(state=tk.DISABLED)


# Función para crear ventanas
def create_window(title):
    window = tk.Toplevel()
    window.title(title)
    window.geometry("400x300")

    textbox = ScrolledText(window, wrap=tk.WORD, state=tk.NORMAL)
    textbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    read_button = tk.Button(window, text="Leer", command=lambda: threading.Thread(target=read_file, args=(textbox,)).start())
    read_button.pack(side=tk.LEFT, padx=5, pady=5)

    edit_button = tk.Button(window, text="Editar", command=lambda: threading.Thread(target=edit_file, args=(textbox,)).start())
    edit_button.pack(side=tk.LEFT, padx=5, pady=5)

    save_button = tk.Button(window, text="Guardar", command=lambda: threading.Thread(target=write_file, args=(textbox,)).start())
    save_button.pack(side=tk.LEFT, padx=5, pady=5)


# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulación Lector-Escritor")
root.geometry("300x150")

main_label = tk.Label(root, text="Simulación del Algoritmo Lector-Escritor")
main_label.pack(pady=10)

btn_window1 = tk.Button(root, text="Ventana 1", command=lambda: create_window("Ventana 1"))
btn_window1.pack(pady=5)

btn_window2 = tk.Button(root, text="Ventana 2", command=lambda: create_window("Ventana 2"))
btn_window2.pack(pady=5)

btn_window3 = tk.Button(root, text="Ventana 3", command=lambda: create_window("Ventana 3"))
btn_window3.pack(pady=5)

root.mainloop()

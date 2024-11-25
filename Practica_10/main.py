import tkinter as tk
from tkinter import messagebox
import threading
import time
import random

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.lista_autos = [None] * capacidad  # Lista fija con espacios vacíos
        self.lock = threading.Lock()

    def agregar_auto(self, auto):
        with self.lock:
            espacios_disponibles = [i for i, auto in enumerate(self.lista_autos) if auto is None]
            if espacios_disponibles:
                espacio = random.choice(espacios_disponibles)
                self.lista_autos[espacio] = auto
                return espacio
            return None

    def retirar_auto(self):
        with self.lock:
            espacios_ocupados = [i for i, auto in enumerate(self.lista_autos) if auto is not None]
            if espacios_ocupados:
                espacio = random.choice(espacios_ocupados)
                self.lista_autos[espacio] = None
                return espacio
            return None

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Estacionamiento")
        self.root.geometry("600x550")

        # Estacionamiento
        self.estacionamiento = Estacionamiento(12)

        # Frecuencias iniciales
        self.frecuencia_agregar = 1
        self.frecuencia_retirar = 1

        # Crear UI
        self.create_ui()

        # Hilos
        self.hilo_agregar = threading.Thread(target=self.auto_agregar, daemon=True)
        self.hilo_retirar = threading.Thread(target=self.auto_retirar, daemon=True)

        # Iniciar hilos
        self.hilo_agregar.start()
        self.hilo_retirar.start()

    def create_ui(self):
        # Panel de estacionamiento
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack(pady=10)

        # Dibujar espacios del estacionamiento
        self.espacios = []
        for i in range(3):
            for j in range(4):
                rect = self.canvas.create_rectangle(
                    20 + j * 90, 20 + i * 90, 100 + j * 90, 100 + i * 90, fill="white", outline="black"
                )
                self.espacios.append(rect)

        # Frecuencia de agregar autos
        tk.Label(self.root, text="Frecuencia de agregar autos (segundos):").pack()
        self.entry_frecuencia_agregar = tk.Entry(self.root)
        self.entry_frecuencia_agregar.insert(0, "1")
        self.entry_frecuencia_agregar.pack()

        tk.Button(self.root, text="Actualizar Frecuencia Agregar", command=self.actualizar_frecuencia_agregar).pack(pady=5)

        # Frecuencia de retirar autos
        tk.Label(self.root, text="Frecuencia de retirar autos (segundos):").pack()
        self.entry_frecuencia_retirar = tk.Entry(self.root)
        self.entry_frecuencia_retirar.insert(0, "1")
        self.entry_frecuencia_retirar.pack()

        tk.Button(self.root, text="Actualizar Frecuencia Retirar", command=self.actualizar_frecuencia_retirar).pack(pady=5)

        # Debugger de hilos con textboxes
        tk.Label(self.root, text="Estado de procesos:").pack()
        self.textbox_entrada = tk.Text(self.root, height=2, width=40, state="disabled", bg="#f0f0f0")
        self.textbox_entrada.pack(pady=5)
        self.textbox_salida = tk.Text(self.root, height=2, width=40, state="disabled", bg="#f0f0f0")
        self.textbox_salida.pack(pady=5)

    def actualizar_frecuencia_agregar(self):
        try:
            self.frecuencia_agregar = float(self.entry_frecuencia_agregar.get())
            if self.frecuencia_agregar <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor válido para la frecuencia de agregar autos.")
            self.entry_frecuencia_agregar.delete(0, tk.END)
            self.entry_frecuencia_agregar.insert(0, "1")

    def actualizar_frecuencia_retirar(self):
        try:
            self.frecuencia_retirar = float(self.entry_frecuencia_retirar.get())
            if self.frecuencia_retirar <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor válido para la frecuencia de retirar autos.")
            self.entry_frecuencia_retirar.delete(0, tk.END)
            self.entry_frecuencia_retirar.insert(0, "1")

    def auto_agregar(self):
        while True:
            time.sleep(random.choice([0.5, 1, 2]) if self.frecuencia_agregar == 1 else self.frecuencia_agregar)
            auto = f"Auto-{random.randint(1000, 9999)}"
            espacio = self.estacionamiento.agregar_auto(auto)
            if espacio is not None:
                color = f"#{random.randint(0, 0xFFFFFF):06x}"  # Color aleatorio
                self.canvas.itemconfig(self.espacios[espacio], fill=color)
                self.actualizar_textbox(self.textbox_entrada, f"Se agregó un auto en el espacio {espacio + 1}.")
            else:
                self.actualizar_textbox(self.textbox_entrada, "Estacionamiento lleno.")

    def auto_retirar(self):
        while True:
            time.sleep(random.choice([0.5, 1, 2]) if self.frecuencia_retirar == 1 else self.frecuencia_retirar)
            espacio = self.estacionamiento.retirar_auto()
            if espacio is not None:
                self.canvas.itemconfig(self.espacios[espacio], fill="white")
                self.actualizar_textbox(self.textbox_salida, f"Se retiró un auto del espacio {espacio + 1}.")
            else:
                self.actualizar_textbox(self.textbox_salida, "Estacionamiento vacío.")

    def actualizar_textbox(self, textbox, mensaje):
        # Agrega mensajes a los textboxes
        textbox.config(state="normal")
        textbox.insert("end", mensaje + "\n")
        textbox.see("end")
        textbox.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

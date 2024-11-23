import tkinter as tk
from tkinter import filedialog

# Funciones de los algoritmos de administración de memoria

def primer_ajuste(memoria, archivos):
    bloques_asignados = []
    archivos_por_bloque = {i: [] for i in range(len(memoria))}
    
    for archivo in archivos:
        asignado = False
        for i in range(len(memoria)):
            if memoria[i] >= archivo[1] and not asignado:
                memoria[i] -= archivo[1]
                archivos_por_bloque[i].append(archivo)
                asignado = True
        if not asignado:
            bloques_asignados.append((archivo[0], -1, archivo[1]))  # No asignado
    
    # Convertir los archivos por bloque en la lista final
    for i in range(len(memoria)):
        for archivo in archivos_por_bloque[i]:
            bloques_asignados.append((archivo[0], i, archivo[1]))
    
    return bloques_asignados

def mejor_ajuste(memoria, archivos):
    bloques_asignados = []
    archivos_por_bloque = {i: [] for i in range(len(memoria))}
    
    for archivo in archivos:
        asignado = False
        # Ordenamos los bloques de memoria para encontrar el mejor ajuste
        memoria_sorted = sorted([(i, memoria[i]) for i in range(len(memoria))], key=lambda x: x[1])
        for i, espacio in memoria_sorted:
            if espacio >= archivo[1] and not asignado:
                memoria[i] -= archivo[1]
                archivos_por_bloque[i].append(archivo)
                asignado = True
        if not asignado:
            bloques_asignados.append((archivo[0], -1, archivo[1]))  # No asignado
    
    # Convertir los archivos por bloque en la lista final
    for i in range(len(memoria)):
        for archivo in archivos_por_bloque[i]:
            bloques_asignados.append((archivo[0], i, archivo[1]))
    
    return bloques_asignados


# Interfaz gráfica

class MemoriaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Algoritmos de Administración de Memoria")
        self.master.geometry("800x600")  # Tamaño más razonable para el ejemplo
        
        self.memoria = [512, 1024, 2048, 4096, 8192]  # Memoria dividida en 5 partes desiguales
        self.archivos = []  # Aquí almacenaremos los archivos leídos del archivo .txt
        
        self.create_widgets()

    def create_widgets(self):
        # Botón para seleccionar el algoritmo
        self.algoritmo_label = tk.Label(self.master, text="Selecciona un algoritmo:")
        self.algoritmo_label.pack(pady=10)
        
        self.algoritmo_var = tk.StringVar(value="Primer Ajuste")
        self.primer_ajuste_radio = tk.Radiobutton(self.master, text="Primer Ajuste", variable=self.algoritmo_var, value="Primer Ajuste")
        self.primer_ajuste_radio.pack()
        self.mejor_ajuste_radio = tk.Radiobutton(self.master, text="Mejor Ajuste", variable=self.algoritmo_var, value="Mejor Ajuste")
        self.mejor_ajuste_radio.pack()
        
        # Botón para seleccionar el archivo .txt
        self.cargar_archivos_button = tk.Button(self.master, text="Cargar Archivos", command=self.cargar_archivos)
        self.cargar_archivos_button.pack(pady=20)
        
        self.asignar_button = tk.Button(self.master, text="Asignar Archivos", command=self.asignar_archivos, state=tk.DISABLED)
        self.asignar_button.pack(pady=20)

        # Botón para limpiar la memoria
        self.limpiar_button = tk.Button(self.master, text="Limpiar Memoria", command=self.limpiar_memoria)
        self.limpiar_button.pack(pady=20)

        # Canvas para mostrar la memoria y los archivos
        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.redibujar_memoria)

    def cargar_archivos(self):
        # Solicitar al usuario que seleccione el archivo .txt
        archivo_path = filedialog.askopenfilename(title="Selecciona el archivo con la lista de archivos", filetypes=[("Text files", "*.txt")])
        
        if archivo_path:
            with open(archivo_path, "r") as file:
                self.archivos = []
                for line in file:
                    nombre, tamaño = line.strip().split(", ")
                    self.archivos.append((nombre, int(tamaño.replace("kb", ""))))
            
            # Habilitar el botón de asignar
            self.asignar_button.config(state=tk.NORMAL)

    def asignar_archivos(self):
        # Limpiar el lienzo
        self.canvas.delete("all")
        
        # Leer los archivos
        archivos = self.archivos
        
        # Seleccionar el algoritmo
        algoritmo = self.algoritmo_var.get()
        
        if algoritmo == "Primer Ajuste":
            bloques_asignados = primer_ajuste(self.memoria.copy(), self.archivos)
        elif algoritmo == "Mejor Ajuste":
            bloques_asignados = mejor_ajuste(self.memoria.copy(), self.archivos)

        
        # Mostrar la memoria y los bloques asignados
        self.dibujar_memoria(bloques_asignados)
    
    def dibujar_memoria(self, bloques_asignados):
        # Obtener las dimensiones actuales del canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Calcular la posición de inicio y las dimensiones de cada bloque
        memoria_inicio_x = 50
        memoria_y = 50
        memoria_altura = 100
        color = ["#FF6347", "#8A2BE2", "#5F9EA0", "#FFD700"]
        
        # Dibujar los bloques de memoria
        for i, espacio in enumerate(self.memoria):
            self.canvas.create_rectangle(memoria_inicio_x, memoria_y, memoria_inicio_x + 200, memoria_y + memoria_altura, outline="black", fill="#D3D3D3")
            self.canvas.create_text(memoria_inicio_x + 100, memoria_y + 50, text=f"Bloque {i+1} - {espacio}KB", font=("Helvetica", 12))
            memoria_inicio_x += 250  # Espaciado entre bloques de memoria

        # Dibujar los archivos apilados debajo de cada bloque
        archivo_inicio_y = memoria_y + memoria_altura + 20  # Posición inicial debajo de los bloques
        for i in range(len(self.memoria)):
            archivo_x = 50 + i * 250  # Posición X para cada bloque
            archivo_y = archivo_inicio_y
            for archivo, bloque, tamaño in bloques_asignados:
                if bloque == i:  # Solo mostrar los archivos asignados al bloque i
                    self.canvas.create_rectangle(archivo_x, archivo_y, archivo_x + 200, archivo_y + 50, outline="black", fill=color[i % len(color)])
                    self.canvas.create_text(archivo_x + 100, archivo_y + 25, text=f"{archivo} - {tamaño}KB", font=("Helvetica", 12))
                    archivo_y += 60  # Apilar los archivos dentro del bloque
            archivo_inicio_y = archivo_y  # Ajustar la altura para el siguiente bloque

    def limpiar_memoria(self):
        # Restablecer los valores de la memoria a su estado inicial
        self.memoria = [512, 1024, 2048, 4096, 8192]
        
        # Limpiar el lienzo
        self.canvas.delete("all")
        
        # Redibujar la memoria limpia
        self.dibujar_memoria([])

    def redibujar_memoria(self, event):
        # Redibujar la memoria cuando el canvas cambia de tamaño
        self.canvas.delete("all")
        self.dibujar_memoria([])

# Ejecutar la aplicación
def run():
    root = tk.Tk()
    app = MemoriaApp(root)
    root.mainloop()

run()

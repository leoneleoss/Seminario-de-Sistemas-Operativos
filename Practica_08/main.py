import tkinter as tk
from tkinter import filedialog, messagebox

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

def peor_ajuste(memoria, archivos):
    bloques_asignados = []
    archivos_por_bloque = {i: [] for i in range(len(memoria))}
    
    for archivo in archivos:
        asignado = False
        # Ordenar los bloques de memoria de mayor a menor
        memoria_sorted = sorted([(i, memoria[i]) for i in range(len(memoria))], key=lambda x: x[1], reverse=True)
        for i, espacio in memoria_sorted:
            if espacio >= archivo[1] and not asignado:
                memoria[i] -= archivo[1]
                archivos_por_bloque[i].append(archivo)
                asignado = True
        if not asignado:
            bloques_asignados.append((archivo[0], -1, archivo[1]))  # No asignado
    
    for i in range(len(memoria)):
        for archivo in archivos_por_bloque[i]:
            bloques_asignados.append((archivo[0], i, archivo[1]))
    
    return bloques_asignados

def siguiente_ajuste(memoria, archivos):
    bloques_asignados = []
    archivos_por_bloque = {i: [] for i in range(len(memoria))}
    ultimo_bloque = 0
    
    for archivo in archivos:
        asignado = False
        for i in range(ultimo_bloque, len(memoria)):
            if memoria[i] >= archivo[1] and not asignado:
                memoria[i] -= archivo[1]
                archivos_por_bloque[i].append(archivo)
                ultimo_bloque = (i + 1) % len(memoria)  # Avanzar al siguiente bloque
                asignado = True
        if not asignado:
            bloques_asignados.append((archivo[0], -1, archivo[1]))  # No asignado
    
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
        self.peor_ajuste_radio = tk.Radiobutton(self.master, text="Peor Ajuste", variable=self.algoritmo_var, value="Peor Ajuste")
        self.peor_ajuste_radio.pack()
        self.siguiente_ajuste_radio = tk.Radiobutton(self.master, text="Siguiente Ajuste", variable=self.algoritmo_var, value="Siguiente Ajuste")
        self.siguiente_ajuste_radio.pack()

        # Botones alineados en una línea
        button_frame = tk.Frame(self.master)  # Creamos un marco (frame) para los botones
        button_frame.pack(pady=20)

        self.agregar_bloque_button = tk.Button(button_frame, text="Agregar Bloque de Memoria", command=self.agregar_bloque)
        self.agregar_bloque_button.pack(side=tk.LEFT, padx=5)

        self.cargar_archivos_button = tk.Button(button_frame, text="Cargar Archivos", command=self.cargar_archivos)
        self.cargar_archivos_button.pack(side=tk.LEFT, padx=5)

        self.agregar_archivo_virtual_button = tk.Button(button_frame, text="Agregar Archivo Virtual", command=self.agregar_archivo_virtual)
        self.agregar_archivo_virtual_button.pack(side=tk.LEFT, padx=5)

        self.asignar_button = tk.Button(button_frame, text="Asignar Archivos", command=self.asignar_archivos, state=tk.DISABLED)
        self.asignar_button.pack(side=tk.LEFT, padx=5)

        self.limpiar_button = tk.Button(button_frame, text="Limpiar Memoria", command=self.limpiar_memoria)
        self.limpiar_button.pack(side=tk.LEFT, padx=5)
        
        # Canvas para mostrar la memoria y los archivos
        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.redibujar_memoria)

    def agregar_bloque(self):
        # Ventana para ingresar las características del nuevo bloque de memoria
        bloque_ventana = tk.Toplevel(self.master)
        bloque_ventana.title("Agregar Bloque de Memoria")

        # Entrada para el tamaño del bloque en KB
        tk.Label(bloque_ventana, text="Tamaño (KB):").pack(pady=5)
        tamano_entry = tk.Entry(bloque_ventana)
        tamano_entry.pack(pady=5)

        # Opción para el estatus (disponible u ocupado)
        tk.Label(bloque_ventana, text="Estatus (Disponible u Ocupado):").pack(pady=5)
        estatus_var = tk.StringVar(value="Disponible")
        estatus_menu = tk.OptionMenu(bloque_ventana, estatus_var, "Disponible", "Ocupado")
        estatus_menu.pack(pady=5)

        # Opción para elegir la posición (inicio o final)
        tk.Label(bloque_ventana, text="Posición (inicio o final):").pack(pady=5)
        posicion_var = tk.StringVar(value="Final")
        posicion_menu = tk.OptionMenu(bloque_ventana, posicion_var, "Inicio", "Final")
        posicion_menu.pack(pady=5)

        # Función para guardar el bloque
        def guardar_bloque():
            tamano = tamano_entry.get()
            estatus = estatus_var.get().lower()
            posicion = posicion_var.get().lower()

            # Validación de datos
            if not tamano or estatus not in ['disponible', 'ocupado'] or posicion not in ['inicio', 'final']:
                messagebox.showerror("Error", "Por favor, ingrese todos los datos correctamente.")
                return

            try:
                tamano = int(tamano)
            except ValueError:
                messagebox.showerror("Error", "El tamaño debe ser un número entero.")
                return

            if posicion == "inicio":
                self.memoria.insert(0, tamano)  # Agregar al inicio
            else:
                self.memoria.append(tamano)  # Agregar al final

            # Recargar la interfaz
            bloque_ventana.destroy()
            self.redibujar_memoria(None)

        # Botón para guardar el bloque
        tk.Button(bloque_ventana, text="Guardar", command=guardar_bloque).pack(pady=10)
    
    def agregar_archivo_virtual(self):
        # Ventana para ingresar las características del archivo virtual
        archivo_ventana = tk.Toplevel(self.master)
        archivo_ventana.title("Agregar Archivo Virtual")

        # Entrada para el nombre del archivo
        tk.Label(archivo_ventana, text="Nombre del archivo:").pack(pady=5)
        nombre_entry = tk.Entry(archivo_ventana)
        nombre_entry.pack(pady=5)

        # Entrada para el tamaño del archivo en KB
        tk.Label(archivo_ventana, text="Tamaño (KB):").pack(pady=5)
        tamano_entry = tk.Entry(archivo_ventana)
        tamano_entry.pack(pady=5)

        # Opción para elegir la posición (inicio o final)
        tk.Label(archivo_ventana, text="Posición (inicio o final):").pack(pady=5)
        posicion_var = tk.StringVar()
        posicion_entry = tk.Entry(archivo_ventana, textvariable=posicion_var)
        posicion_entry.pack(pady=5)

        # Función para abrir un archivo existente
        def seleccionar_archivo():
            archivo_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Text Files", "*.txt")])
            if archivo_path:
                return archivo_path
            else:
                messagebox.showerror("Error", "No se ha seleccionado un archivo.")
                return None

        # Función para guardar el archivo virtual
        def guardar_archivo():
            # Selección del archivo
            archivo_path = seleccionar_archivo()
            if not archivo_path:
                return

            nombre = nombre_entry.get()
            tamano = tamano_entry.get()
            posicion = posicion_var.get().lower()

            # Validación de datos
            if not nombre or not tamano or not posicion:
                messagebox.showerror("Error", "Por favor, ingrese todos los datos.")
                return

            try:
                tamano = int(tamano)
            except ValueError:
                messagebox.showerror("Error", "El tamaño debe ser un número entero.")
                return

            if posicion not in ['inicio', 'final']:
                messagebox.showerror("Error", "La posición debe ser 'inicio' o 'final'.")
                return

            # Crear la línea que representa el archivo virtual
            archivo_linea = f"{nombre}, {tamano}kb\n"

            # Leer el contenido actual del archivo y agregar la nueva línea
            with open(archivo_path, "r") as file:
                lines = file.readlines()

            if posicion == 'inicio':
                lines.insert(0, archivo_linea)  # Agregar al inicio
            else:
                if not lines[-1].endswith('\n'):
                    lines.append('\n')  # Asegurar que haya un salto de línea antes
                lines.append(archivo_linea)  # Agregar al final

            # Sobrescribir el archivo con las nuevas líneas
            with open(archivo_path, "w") as file:
                file.writelines(lines)

            archivo_ventana.destroy()
            self.cargar_archivos()  # Recargar archivos para actualizar la lista

        # Botón para guardar el archivo virtual
        tk.Button(archivo_ventana, text="Guardar", command=guardar_archivo).pack(pady=10)     
    
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
        elif algoritmo == "Peor Ajuste":
            bloques_asignados = peor_ajuste(self.memoria.copy(), self.archivos)
        elif algoritmo == "Siguiente Ajuste":
            bloques_asignados = siguiente_ajuste(self.memoria.copy(), self.archivos)
        
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
        self.canvas.delete("all")
        self.dibujar_memoria([])

# Ejecutar la aplicación
def run():
    root = tk.Tk()
    app = MemoriaApp(root)
    root.mainloop()

run()

import tkinter as tk
from tkinter import messagebox

# Definir el espacio de memoria (bloques de memoria disponibles en KB)
bloques_memoria = [300, 600, 350, 200, 750]  # Espacios de memoria disponibles en KB
rectangulos_memoria = []

# Función para leer archivos y tamaños desde un archivo .txt proporcionado por el usuario
def leer_archivos(ruta):
    archivos = []
    with open(ruta, "r") as f:
        for linea in f:
            nombre, tamano = linea.strip().split(", ")
            archivos.append((nombre, int(tamano[:-2])))  # Quitamos 'kb' y convertimos a entero
    return archivos

# Función para el algoritmo de Primer ajuste
def primer_ajuste(archivos, bloques_memoria):
    asignacion = [-1] * len(archivos)  # Inicializamos sin asignar (-1)
    for i, archivo in enumerate(archivos):
        for j, bloque in enumerate(bloques_memoria):
            if archivo[1] <= bloque:  # Si el archivo cabe en el bloque
                asignacion[i] = j  # Asignamos el bloque al archivo
                bloques_memoria[j] -= archivo[1]  # Reducimos el espacio disponible en el bloque
                break
    return asignacion

# Función para el algoritmo de Mejor ajuste
def mejor_ajuste(archivos, bloques_memoria):
    asignacion = [-1] * len(archivos)
    for i, archivo in enumerate(archivos):
        mejor_bloque = -1
        for j, bloque in enumerate(bloques_memoria):
            if archivo[1] <= bloque:
                if mejor_bloque == -1 or bloques_memoria[mejor_bloque] > bloque:
                    mejor_bloque = j
        if mejor_bloque != -1:
            asignacion[i] = mejor_bloque
            bloques_memoria[mejor_bloque] -= archivo[1]
    return asignacion

# Función para mostrar la asignación visualmente en una sola barra
def mostrar_asignacion_visual(archivos, asignacion, bloques_disponibles):
    for rect in rectangulos_memoria:
        canvas.delete(rect)
    
    rectangulos_memoria.clear()

    x_start = 50  # Inicio del primer rectángulo
    y_position = 100  # Fija la altura para todos los rectángulos
    canvas_width = root.winfo_width() - 100  # Ajustar para la barra completa

    # Calcular el tamaño total de memoria
    total_memoria = sum(bloques_memoria)

    for j, bloque in enumerate(bloques_disponibles):
        # Dibujar bloque de memoria
        bloque_width = int((bloque / total_memoria) * canvas_width)  # Escalamos el ancho según el tamaño total de la memoria
        rectangulo = canvas.create_rectangle(x_start, y_position, x_start + bloque_width, y_position + 50, outline="black", fill="white")
        canvas.create_text(x_start + (bloque_width // 2), y_position + 25, text=f"{bloque} KB", fill="black")
        rectangulos_memoria.append(rectangulo)
        
        # Dibujar archivos asignados en este bloque
        for i, archivo in enumerate(archivos):
            if asignacion[i] == j:
                # Dibujar asignación del archivo en el bloque
                archivo_width = int((archivos[i][1] / total_memoria) * canvas_width)
                archivo_rect = canvas.create_rectangle(x_start, y_position, x_start + archivo_width, y_position + 50, fill="red")
                canvas.create_text(x_start + archivo_width // 2, y_position + 25, text=f"{archivos[i][0]} ({archivos[i][1]} KB)", fill="white")
                x_start += archivo_width  # Mover el inicio del siguiente archivo
        
        # Desplazar el inicio del siguiente bloque
        x_start += bloque_width - sum([(archivos[i][1] / total_memoria) * canvas_width for i in range(len(archivos)) if asignacion[i] == j])

# Función principal del programa
def ejecutar_programa():
    ruta_archivo = entry_ruta.get()
    try:
        archivos = leer_archivos(ruta_archivo)
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {e}")
        return
    
    bloques_disponibles = bloques_memoria.copy()

    if var_algoritmo.get() == "Primer ajuste":
        asignacion = primer_ajuste(archivos, bloques_disponibles)
    elif var_algoritmo.get() == "Mejor ajuste":
        asignacion = mejor_ajuste(archivos, bloques_disponibles)
    else:
        messagebox.showerror("Error", "Debe seleccionar un algoritmo.")
        return

    # Mostrar la asignación visualmente en una sola barra
    mostrar_asignacion_visual(archivos, asignacion, bloques_memoria.copy())

# Configuración de la interfaz gráfica (Tkinter)
root = tk.Tk()
root.title("Administración de Memoria")
root.attributes('-fullscreen', True)  # Pantalla completa

# Crear etiquetas y entrada de texto para la ruta del archivo
frame_top = tk.Frame(root)
frame_top.pack(pady=10)
tk.Label(frame_top, text="Ruta del archivo .txt:").pack(side=tk.LEFT, padx=5)
entry_ruta = tk.Entry(frame_top, width=50)
entry_ruta.pack(side=tk.LEFT, padx=5)

# Selección del algoritmo
var_algoritmo = tk.StringVar(value="Primer ajuste")
tk.Radiobutton(root, text="Primer ajuste", variable=var_algoritmo, value="Primer ajuste").pack()
tk.Radiobutton(root, text="Mejor ajuste", variable=var_algoritmo, value="Mejor ajuste").pack()

# Botón para ejecutar el programa
tk.Button(root, text="Ejecutar", command=ejecutar_programa).pack(pady=10)

# Crear un canvas para la representación gráfica de los bloques de memoria
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Botón para salir de pantalla completa
def salir_pantalla_completa():
    root.attributes('-fullscreen', False)

tk.Button(root, text="Salir de pantalla completa", command=salir_pantalla_completa).pack(pady=10)

root.mainloop()

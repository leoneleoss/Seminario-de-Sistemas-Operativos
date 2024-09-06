import os
import fnmatch
import time

# Lista de extensiones malignas a bloquear
malicious_extensions = ['.exe', '.bat', '.vbs']

# Función para eliminar archivos con extensiones malignas y retornar el número de archivos eliminados
def delete_malicious_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Verificar si el archivo tiene una extensión maligna
            if any(fnmatch.fnmatch(file, f'*{ext}') for ext in malicious_extensions):
                file_path = os.path.join(root, file)
                print(f'\nDetectado archivo malicioso: {file_path}')
                
                try:
                    # Intentar eliminar el archivo
                    os.remove(file_path)
                    # Verificar si el archivo fue eliminado correctamente
                    if not os.path.exists(file_path):
                        print(f'Archivo eliminado correctamente: {file_path}')
                        count += 1
                    else:
                        print(f'\nError: no se pudo eliminar el archivo: {file_path}')
                except Exception as e:
                    # Manejar cualquier excepción que ocurra durante la eliminación
                    print(f'\nError al intentar eliminar el archivo: {file_path}. Detalles: {e}')
    return count

if __name__ == "__main__":
    # Solicitar la ruta de la carpeta al usuario
    folder_to_monitor = input(r"Introduce la ruta de la carpeta que deseas monitorizar: ")
    
    print("\nPara detener el programa, presione Ctrl+C")
    try:
        while True:
            # Limpieza de archivos maliciosos
            deleted_files = delete_malicious_files(folder_to_monitor)

            if deleted_files == 0:
                print("\nMonitoreo completado. No se detectaron más archivos maliciosos.")
                
            # Esperar 10 segundos antes de comprobar de nuevo
            time.sleep(10)
            
    except KeyboardInterrupt:
        print("\nMonitoreo detenido.\n")


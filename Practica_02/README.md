# **Procesamiento por Lotes en Python (2)**

## **Contexto**

El procesamiento por lotes se puede utilizar para gestionar y eliminar archivos peligrosos de manera eficiente. Este programa está diseñado para detectar y eliminar automáticamente archivos con extensiones potencialmente dañinas (`.exe`, `.bat`, `.vbs`) en un directorio especificado, ayudando a mantener la integridad y seguridad del sistema.

## **Metodología**

### Librerías Utilizadas

- **`os`**: Permite interactuar con el sistema de archivos para navegar por directorios y eliminar archivos.
- **`fnmatch`**: Facilita la coincidencia de patrones en nombres de archivos para identificar aquellos con extensiones específicas.
- **`time`**: Utilizada para pausar el programa, permitiendo realizar verificaciones a intervalos regulares.

### Funciones y Algoritmos
1. **`delete_malicious_files()`**:
    El algoritmo de la función delete_malicious_files() está diseñado para buscar y eliminar archivos con extensiones maliciosas dentro de un directorio y sus subdirectorios, utilizando los métodos estándar del módulo os y fnmatch. A continuación, te explico paso a paso cómo funciona y los métodos involucrados:

    1. **Entrada de la Función**

    La función recibe un argumento `directory`, que es la ruta del directorio donde se realizará la búsqueda de archivos maliciosos.

    2. **Inicialización del Contador**

        ```python 
            count = 0:
        ``` 
    Se inicializa un contador `count` que llevará el número de archivos maliciosos eliminados. Este valor será devuelto al final de la función.

    3. **Recorrido del Directorio y Subdirectorios**

    Se utiliza `os.walk(directory)` para recorrer recursivamente todos los archivos y carpetas en el directorio proporcionado. `os.walk()` devuelve tres valores:
    - `root`: La ruta actual del directorio.
    - `dirs`: Una lista con los nombres de las subcarpetas dentro del directorio actual.
    - `files`: Una lista con los nombres de los archivos dentro del directorio actual.

    4. **Búsqueda de Archivos con Extensiones Maliciosas**

    Para cada archivo en la lista `files`, se verifica si su nombre coincide con alguna de las extensiones maliciosas definidas en `malicious_extensions`. Para esto, se usa `fnmatch.fnmatch(file, f'*{ext}')`:
    - `fnmatch` compara el nombre del archivo (`file`) con un patrón que contiene una extensión maliciosa.
    - `any(...)` se utiliza para determinar si el archivo coincide con alguna de las extensiones maliciosas en la lista.


    5. **Construcción de la Ruta Completa del Archivo**

    Si el archivo es malicioso, se construye su ruta completa usando `os.path.join(root, file)`, combinando la ruta del directorio actual (`root`) con el nombre del archivo (`file`). Esto es necesario para eliminar el archivo, ya que `os.remove()` necesita la ruta completa.

    6. **Intento de Eliminar el Archivo**

    Se intenta eliminar el archivo malicioso usando `os.remove(file_path)`. Si la eliminación es exitosa, se comprueba inmediatamente si el archivo ya no existe usando `os.path.exists(file_path)`. Si el archivo ha sido eliminado correctamente, se aumenta el contador `count`. Si ocurre alguna excepción (por ejemplo, falta de permisos), el programa captura la excepción y muestra un mensaje de error.

    7. **Devolución del Contador**

    La función devuelve el número de archivos eliminados, que es el valor del contador `count`. Esto permite al programa principal saber si todavía hay archivos maliciosos en el sistema.


   - **Métodos Utilizados**

    - **`os.walk(directory)`**: Este método recorre un directorio y todas sus subcarpetas, devolviendo la ruta del directorio actual, las subcarpetas y los archivos contenidos en cada directorio.

    - **`fnmatch.fnmatch(filename, pattern)`**: Este método compara el nombre de un archivo con un patrón. En este caso, usamos `*{ext}` como patrón para buscar archivos que terminan con una de las extensiones maliciosas definidas.

    - **`os.path.join(path, filename)`**: Combina la ruta de un directorio (`path`) y el nombre de un archivo (`filename`) para formar una ruta completa hacia ese archivo.

    - **`os.remove(path)`**: Elimina el archivo especificado en `path`. Si la eliminación es exitosa, el archivo ya no existirá en el sistema.

    - **`os.path.exists(path)`**: Verifica si el archivo o directorio especificado en `path` aún existe en el sistema. Se utiliza después de `os.remove()` para confirmar que el archivo fue eliminado correctamente.

    - **`try-except`**: Este bloque de código se usa para manejar errores que puedan ocurrir durante la eliminación de archivos, como problemas de permisos u otros errores del sistema operativo.

    - **Estructura del Programa**:
    - **Entrada del Usuario**: Solicita la ruta del directorio a monitorear.
    - **Monitoreo Continuo**: Ejecuta la función de limpieza en intervalos de 10 segundos.
    - **Interrupción del Programa**: Permite detener el monitoreo con Ctrl+C.

## **Conclusión**
Entendí como hacer un programa eficaz para detectar y eliminar archivos con extensiones maliciosas haciendo uso de ciertas librerias. 

### Aspectos Funcionales:

- **Detección y Eliminación**: Identifica y elimina archivos `.exe`, `.bat`, y `.vbs`, con mensajes informativos sobre el estado de cada archivo.
- **Monitoreo Continuo**: Revisa el directorio a intervalos regulares para detectar nuevos archivos maliciosos.

### Áreas de Mejora:

- **Expansión de Tipos de Archivos**: Ampliar la lista de extensiones para incluir otras amenazas.
- **Optimización del Rendimiento**: Mejorar la eficiencia en el manejo de grandes volúmenes de archivos.
- **Interfaz de Usuario**: Desarrollar una interfaz gráfica o de línea de comandos más avanzada.

## **Referencias**

- Python Software Foundation. (n.d.). *os — Miscellaneous operating system interfaces*. Recuperado de [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)
- Python Software Foundation. (n.d.). *fnmatch — Unix filename pattern matching*. Recuperado de [https://docs.python.org/3/library/fnmatch.html](https://docs.python.org/3/library/fnmatch.html)
- Python Software Foundation. (n.d.). *time — Time access and conversions*. Recuperado de [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)

# **Procesamiento por Lotes en Python**

## **Contexto**

Este proyecto aborda el tema del **"Procesamiento por lotes en programación"**. El procesamiento por lotes es una técnica que se utiliza para manejar grandes volúmenes de datos en bloques o lotes, en lugar de procesar los datos uno a uno en tiempo real. Este enfoque es útil para operaciones complejas y para manejar grandes conjuntos de datos de manera eficiente.

El código proporcionado realiza procesamiento por lotes sobre un archivo CSV que contiene direcciones IPv6, cadenas de texto y direcciones IP. La tarea es leer el archivo línea por línea (en lotes) y transformar los datos según los requisitos especificados:

1. **Conversión de Hexadecimal a Decimal**: Se convierten direcciones IPv6 de formato hexadecimal a decimal.
2. **Extracción de Información Específica**: Se extrae la segunda cadena de texto de cada línea.
3. **Conversión de IP a Hexadecimal**: Se convierte la dirección IP de formato decimal a hexadecimal.
4. **Escritura de Resultados**: Se generan y almacenan los resultados transformados en un nuevo archivo.

Este enfoque de procesamiento por lotes permite manejar eficientemente la conversión y limpieza de datos a gran escala sin necesidad de realizar estas operaciones en tiempo real. El código sigue un flujo de trabajo típico en el procesamiento por lotes: lectura de datos, procesamiento en bloque y escritura de resultados, lo que facilita la gestión de grandes volúmenes de datos y asegura que las operaciones se realicen de manera ordenada y consistente.

## **Metodología**

### Librerías Utilizadas

- **`re`**: Librería para expresiones regulares en Python, utilizada para validar cadenas hexadecimales.

### Funciones y Algoritmos

1. **`clean_hex(hex_str)`**:
   - **Propósito**: Elimina cualquier información después de una barra (`/`) en una cadena hexadecimal.
   - **Algoritmo**: Divide la cadena en la barra y toma la primera parte.

   ```python
   def clean_hex(hex_str):
       return hex_str.split('/')[0]
   ```
2. **`hex_to_decimal(hex_str):`**

    - Propósito: Convierte una cadena hexadecimal a un valor decimal.
    - Algoritmo: Utiliza int(hex_str, 16) para la conversión y maneja excepciones si la conversión falla.

3. **`ip_to_hex(ip_str):`**

    - Propósito: Convierte una dirección IP en formato decimal a hexadecimal.
    - Algoritmo: Divide la IP en octetos, convierte cada octeto a hexadecimal y los une con puntos (.).

3. **`process_line(line):`**

    - Propósito: Procesa una línea del archivo, realiza conversiones necesarias y extrae datos relevantes.
    - Algoritmo: Divide la línea en partes, limpia y convierte valores hexadecimales, extrae la segunda cadena de texto y convierte la IP a hexadecimal.

4. **`process_file(input_file, output_file):`**

    - Propósito: Lee un archivo de entrada, procesa cada línea usando process_line y escribe los resultados en un archivo de salida.
    - Algoritmo: Abre los archivos de entrada y salida, procesa línea por línea y guarda los resultados.

## **Conclusión**
El código proporciona una solución efectiva para procesar y transformar datos en formato CSV. Las características funcionales incluyen:

- Conversión de direcciones IPv6 de hexadecimal a decimal.
- Extracción de la segunda cadena de texto.
- Conversión de direcciones IP de decimal a hexadecimal.

### Aspectos Funcionales:

- Conversión y limpieza de datos realizadas correctamente.
- Manejo de errores y advertencias.

### Áreas de Mejora:

- Validación de Datos: Mejorar la verificación de formatos para manejar más casos de datos erróneos o inesperados.
- Optimización del Rendimiento: Considerar la optimización para archivos de gran tamaño.
- Manejo de Excepciones: Mejorar el manejo de excepciones y los mensajes de error.

## **Referencias**

- re — Regular expression operations. (s. f.). Python Documentation. https://docs.python.org/3/library/re.html

- re — Regular expression operations. (s. f.-b). Python Documentation. https://docs.python.org/3/library/re.html#re.fullmatch

- Built-in types. (s. f.). Python Documentation. https://docs.python.org/3/library/stdtypes.html#str.split

- Built-in types. (s. f.-b). Python Documentation. https://docs.python.org/3/library/stdtypes.html#str.join


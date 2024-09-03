import re

def clean_hex(hex_str):
    """Limpia una cadena hexadecimal, eliminando cualquier cosa después de '/'."""
    return hex_str.split('/')[0]

def hex_to_decimal(hex_str):
    """Convierte una cadena hexadecimal a decimal, manejando errores."""
    try:
        return int(hex_str, 16)
    except ValueError:
        print(f"Advertencia: Valor hexadecimal inválido: {hex_str}")
        return None

def ip_to_hex(ip_str):
    """Convierte una dirección IP en formato decimal a hexadecimal."""
    parts = ip_str.split('.')
    # Asegurarse de que cada parte de la IP esté en formato hexadecimal de dos dígitos
    hex_parts = [f"{int(part):02X}" for part in parts]
    return '.'.join(hex_parts)

def process_line(line):
    """Procesa una línea de datos del archivo según las instrucciones dadas."""
    parts = line.strip().split(',')
    
    # Verificar que hay suficientes partes
    if len(parts) < 6:
        print(f"Advertencia: Línea con formato incorrecto: {line}")
        return None

    # Primer campo: direcciones IPv6 en hexadecimal
    hex_parts = parts[0].split(':')
    
    # Limpiar valores hexadecimales
    cleaned_hex_parts = [clean_hex(part) for part in hex_parts]
    
    # Convertir hexadecimales a decimales, ignorar valores no válidos
    decimal_parts = []
    for part in cleaned_hex_parts:
        if re.fullmatch(r'[0-9A-Fa-f]+', part):  # Verificar si es un valor hexadecimal válido
            decimal_value = hex_to_decimal(part)
            if decimal_value is not None:
                decimal_parts.append(decimal_value)
    
    # Segunda cadena de texto
    second_text = parts[2]
    
    # Últimos datos: dirección IP
    ip_address = parts[-1]
    ip_hex = ip_to_hex(ip_address)
    
    # Formatear el resultado
    result = f"{second_text} : {' : '.join(map(str, decimal_parts))} : {ip_hex}"
    return result

def process_file(input_file, output_file):
    """Procesa un archivo de entrada y escribe el resultado en un archivo de salida."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            result = process_line(line)
            if result:
                outfile.write(result + '\n')

# Ejemplo de uso
input_filename = 'Practica_01/input.txt'
output_filename = 'Practica_01/output.txt'
process_file(input_filename, output_filename)
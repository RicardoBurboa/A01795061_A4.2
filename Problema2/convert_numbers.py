"""Módulos del sistema, tiempo y tablas."""
import sys
import time
from prettytable import PrettyTable


def convert_numbers(file_path):
    """Función que convierte números decimales a binarios y hexadecimales."""
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"Error: Archivo '{file_path}' no encontrado.")
        return

    start_time = time.time()

    numbers = []
    for line in data:
        try:
            number = int(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Error: Número inválido encontrado: {line.strip()}")

    binary_results = []
    hexadecimal_results = []
    ns_table = PrettyTable(["Decimal", "Binario", "Hexadecimal"])
    for number in numbers:
        if number > 0:
            binary_results.append(decimal_to_binary(abs(number)))
            hexadecimal_results.append(decimal_to_hexadecimal(abs(number)))
        elif number == 0:
            binary_results.append(0)
            hexadecimal_results.append(0)
        else:
            binary_results.append(decimal_to_binary_2s_complement(number))
            hexadecimal_results.append(decimal_to_hex_2s_complement(number))
        ns_table.add_row([number, binary_results[-1], hexadecimal_results[-1]])

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Imprimir resultados en la pantalla.
    print(ns_table)
    print(f"Tiempo Transcurrido: {elapsed_time} segundos")

    # Escribir los resultados a ConvertionResults.txt
    with open("ConvertionResults.txt", "w", encoding="UTF-8") as result_file:
        result_file.write(ns_table.get_string()+"\n")
        result_file.write(f"Tiempo Transcurrido: {elapsed_time} segundos\n")


def decimal_to_binary(decimal_num):
    """Función que transforma un número decimal a binario."""
    binary_num = ""

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2

    return binary_num


def decimal_to_hexadecimal(decimal_num):
    """Función que transforma un número decimal a hexadecimal."""
    hex_chars = "0123456789ABCDEF"
    hexadecimal_num = ""

    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num = hex_chars[remainder] + hexadecimal_num
        decimal_num //= 16

    return hexadecimal_num


def decimal_to_binary_2s_complement(num, num_bits=10):
    """Función que transforma un número decimal negativo a binario."""
    if num >= 0:
        binary = bin(num)[2:].zfill(num_bits)
    else:
        positive_bin = bin(abs(num))[2:].zfill(num_bits)
        invrd_bin = ''.join('1' if bit == '0' else '0' for bit in positive_bin)

        carry = 1
        result = ''
        for bit in invrd_bin[::-1]:
            if bit == '1' and carry == 1:
                result = '0' + result
            elif bit == '0' and carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = bit + result

        binary = result.zfill(num_bits)

    return binary


def decimal_to_hex_2s_complement(num, num_digits=10):
    """Función que transforma un número decimal negativo a hexadecimal."""
    if num >= 0:
        hex_str = hex(num & (2**32-1))[2:].zfill(num_digits)
    else:
        pos_hex = hex(abs(num) & (2**32-1))[2:].zfill(num_digits)
        inv_hex = ''.join(hex(15 - int(digit, 16))[2:] for digit in pos_hex)

        carry = 1
        result = ''
        for digit in inv_hex[::-1]:
            current = int(digit, 16) + carry
            if current > 15:
                result = hex(current % 16)[2:] + result
                carry = 1
            else:
                result = hex(current)[2:] + result
                carry = 0

        hex_str = result.zfill(num_digits)

    return hex_str.upper()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py fileWithData.txt")
    else:
        convert_numbers(sys.argv[1])

"""Módulos del sistema y para cálcular tiempos."""
import sys
import time


# Función para el problema 1 que computa estadísticas.
def compute_statistics(file_path):
    """Función que computa estadísticas."""
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
            number = float(line.strip())
            numbers.append(number)
        except ValueError:
            print(f"Error: Número inválido encontrado: {line.strip()}")

    mean = sum(numbers) / len(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = (variance) ** (1/2)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Imprimir resultados en la pantalla.
    print(f"Conteo: {len(numbers)}")
    print(f"Promedio: {mean}")
    print(f"Mediana: {median}")
    print(f"Moda: {', '.join(map(str, mode))}")
    print(f"Desviación Estándar: {(variance) ** (1/2)}")
    print(f"Varianza: {variance}")
    print(f"Tiempo Transcurrido: {elapsed_time} segundos")

    # Escribir los resultados a StatisticsResults.txt
    with open("StatisticsResults.txt", "w", encoding="UTF-8") as result_file:
        result_file.write(f"Conteo: {len(numbers)}\n")
        result_file.write(f"Promedio: {mean}\n")
        result_file.write(f"Mediana: {median}\n")
        result_file.write(f"Moda: {', '.join(map(str, mode))}\n")
        result_file.write(f"Desviación Estándar: {std_dev}\n")
        result_file.write(f"Varianza: {variance}\n")
        result_file.write(f"Tiempo Transcurrido: {elapsed_time} segundos\n")


def calculate_mode(number_list):
    """Función para calcular la moda."""
    rpts = {}
    for number in number_list:
        rpts[number] = rpts.get(number, 0) + 1
    mode = [key for key, value in rpts.items() if value == max(rpts.values())]
    return mode


def calculate_median(number_list):
    """Función para calcular la mediana."""
    sorted_data = sorted(number_list)
    mid = len(number_list) // 2
    step = (sorted_data[mid] + sorted_data[~mid]) / 2
    median = step / 2 if len(number_list) % 2 == 0 else sorted_data[mid]
    return median


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py fileWithData.txt")
    else:
        compute_statistics(sys.argv[1])

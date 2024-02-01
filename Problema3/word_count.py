"""Modules"""
import sys
import time
from prettytable import PrettyTable


def word_count(file_path):
    """Función que cuenta la frecuencia de cada palabra."""
    w_count = {}
    start_time = time.time()

    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"Error: Archivo '{file_path}' no encontrado.")
        return

    for line in data:
        words = line.split()
        for word in words:
            word = word.lower()
            w_count[word] = w_count.get(word, 0) + 1

    s_c = dict(sorted(w_count.items(), key=lambda item: item[1], reverse=True))

    words_table = PrettyTable(["Palabra", "Frecuencia"])
    freq_total = 0
    for word in s_c:
        freq_total += int(s_c[word])
        words_table.add_row([word, s_c[word]])

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Imprimir resultados en la pantalla.
    print(words_table)
    print(f"Gran Total: {freq_total}\n")
    print(f"Tiempo Transcurrido: {elapsed_time} segundos")

    # Escribir los resultados a ConvertionResults.txt
    with open("WordCountResults.txt", "w", encoding="UTF-8") as result_file:
        result_file.write(words_table.get_string()+"\n")
        result_file.write(f"Gran Total: {freq_total}\n")
        result_file.write(f"Tiempo Transcurrido: {elapsed_time} segundos\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python word_count.py fileWithData.txt")
    else:
        word_count(sys.argv[1])

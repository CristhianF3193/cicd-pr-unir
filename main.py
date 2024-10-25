"""License: Apache
Organization: UNIR"""

import os
import sys

# Definición de constantes
DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False

# Función para ordenar una lista
def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"No puede ordenar {type(items)}")
    return sorted(items, reverse=(not ascending))

# Función para eliminar duplicados de una lista
def remove_duplicates_from_list(items):
    return list(set(items))

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Variables predeterminadas
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES

    # Manejo de argumentos de línea de comandos
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
    else:
        print("Se debe indicar el fichero como primer argumento")
        print("El segundo argumento indica si se quieren eliminar duplicados")
        sys.exit(1)

    # Leer y procesar el archivo
    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        # Palabras predeterminadas si el archivo no existe
        print(f"El fichero {filename} no existe")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    # Eliminar duplicados si se requiere
    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    # Ordenar y mostrar la lista de palabras
    print(sort_list(word_list))


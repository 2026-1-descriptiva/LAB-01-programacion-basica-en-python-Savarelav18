"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    # Lee el archivo data.csv
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    # Inicializa un diccionario para almacenar los valores asociados a cada clave
    key_values = {}

    # Procesa cada línea del archivo
    for line in lines:
        # Divide la línea en columnas
        columns = line.strip().split('\t')
        # La columna 5 es la que contiene el diccionario codificado
        dict_str = columns[4]
        # Divide el diccionario en pares clave-valor
        pairs = dict_str.split(',')
        for pair in pairs:
            key, value = pair.split(':')
            value = int(value)
            if key not in key_values:
                key_values[key] = []
            key_values[key].append(value)

    # Calcula el valor mínimo y máximo para cada clave
    result = []
    for key, values in key_values.items():
        min_value = min(values)
        max_value = max(values)
        result.append((key, min_value, max_value))

    # Ordena el resultado por clave
    result.sort(key=lambda x: x[0])

    return result

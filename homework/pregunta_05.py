"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    with open('files/input/data.csv', 'r') as file:
        data = file.readlines()

    result = {}
    for line in data:
        columns = line.strip().split('\t')
        letter = columns[0]
        number = int(columns[1])
        if letter in result:
            max_value, min_value = result[letter]
            max_value = max(max_value, number)
            min_value = min(min_value, number)
            result[letter] = (max_value, min_value)
        else:
            result[letter] = (number, number)

    sorted_result = sorted(result.items())
    final_result = [(letter, max_min[0], max_min[1]) for letter, max_min in sorted_result]
    return final_result

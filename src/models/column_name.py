# crea una funcion que reciba como argumento una lista (del nombre de las columnas) y retorne la lista de las columnas depuradas, debe cambiar todo a mayusculas y quitar espacios en blanco al inicio y al final de cada nombre de columna.

def clean_columns(columns_list: list[str]) -> list[str]:
    """
    Limpia los nombres de las columnas de una lista.
    
    Este método recibe una lista de nombres de columnas y los convierte a mayúsculas, además
    elimina los espacios en blanco al inicio y al final de cada nombre de columna.
    
    Parámetros:
    columns_list (list[str]): Una lista de nombres de columnas.
    
    Retorna:
    list[str]: Una lista de nombres de columnas limpios.
    """
    return [column.strip().replace('  ', ' ').replace('  ', ' ').replace(' ', '_').upper() for column in columns_list]
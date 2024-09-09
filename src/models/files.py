import os

def get_file_name() -> list[str]:
    """
    Obtiene una lista de nombres de archivos que cumplen con ciertos criterios.
    
    Este método recorre los archivos en el directorio 'bases/pagos/' y agrega a una lista
    aquellos archivos que tienen la extensión '.xlsx' y contienen 'Base Pagos' en su nombre.
    Finalmente, retorna la lista de nombres de archivos que cumplen con estos criterios.
    
    Retorna:
    list[str]: Una lista de nombres de archivos que cumplen con los criterios especificados.
    """
    file_list = []
    for file in os.listdir('bases/pagos/'):
        if file.endswith('.xlsx') and 'Base Pagos' in file:
            file_list.append(file)
    return file_list
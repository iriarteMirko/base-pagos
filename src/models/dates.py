from datetime import datetime

def get_last_date(dates_list: list[datetime]) -> datetime:
    """
    Obtiene la última fecha de una lista de fechas.
    
    Este método recorre una lista de objetos datetime y encuentra la fecha más reciente.
    Compara cada fecha en la lista con la fecha más reciente encontrada hasta el momento
    y actualiza la fecha más reciente si encuentra una fecha posterior.
    
    Parámetros:
    dates_list (list[datetime]): Una lista de objetos datetime.
    
    Retorna:
    datetime: La fecha más reciente en la lista.
    """
    last_date = dates_list[0]
    for date in dates_list:
        if date > last_date:
            last_date = date
    return last_date

def get_date(file_list: list[str]) -> str:
    """
    Obtiene la última fecha de una lista de nombres de archivos.
    
    Este método recorre una lista de nombres de archivos, extrae las fechas de los nombres
    de los archivos, convierte las fechas a objetos datetime y encuentra la fecha más reciente.
    Finalmente, retorna la fecha más reciente en formato de cadena 'dd.mm.yyyy'.
    
    Parámetros:
    file_list (list[str]): Una lista de nombres de archivos que contienen fechas en su nombre.
    
    Retorna:
    str: La fecha más reciente en formato 'dd.mm.yyyy'.
    """
    dates_list = []
    for file in file_list:
        fecha_list =  file.split(' ')[-1].split('.')[:3]
        dates_list.append(datetime.strptime(fecha_list[0] + '.' + fecha_list[1] + '.' + fecha_list[2], '%d.%m.%Y'))
    return get_last_date(dates_list).strftime('%d.%m.%Y')
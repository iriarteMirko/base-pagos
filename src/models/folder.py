from datetime import datetime
import os

def validate_or_create_folder() -> str:
    """
    Valida o crea una carpeta con la fecha de hoy y una subcarpeta 'agencias'.
    
    Este método verifica si existe una carpeta con la fecha de hoy dentro de una carpeta 'reporte'.
    Si no existe, la crea junto con una subcarpeta llamada 'agencias'. Finalmente, retorna la ruta
    de la carpeta creada o validada.
    
    Retorna:
    str: La ruta de la carpeta creada o validada.
    """
    today_date = datetime.today().strftime('%Y.%m.%d')
    
    report_folder = 'reporte'
    
    today_folder = os.path.join(report_folder, today_date)
    
    if not os.path.exists(today_folder):
        os.makedirs(today_folder)
    
    if not os.path.exists(today_folder+'/agencias'):
        os.makedirs(today_folder+'/agencias')
    
    return today_folder
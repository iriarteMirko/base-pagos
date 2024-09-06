from datetime import datetime
import os

def validar_o_crear_carpeta() -> str:
    fecha_hoy = datetime.today().strftime('%Y.%m.%d')
    
    carpeta_reporte = 'reporte'
    
    carpeta_hoy = os.path.join(carpeta_reporte, fecha_hoy)
    
    if not os.path.exists(carpeta_hoy):
        os.makedirs(carpeta_hoy)
    
    if not os.path.exists(carpeta_hoy+'/agencias'):
        os.makedirs(carpeta_hoy+'/agencias')
    
    return carpeta_hoy
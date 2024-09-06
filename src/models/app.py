from datetime import datetime
from tkinter import messagebox
from optimizar_asignacion import optimizar_asignacion
from load_asignacion import cargar_asignacion

import tkinter as tk
import pandas as pd
import os

class App:
    def __init__(self):
        self.fecha_hoy = datetime.today().strftime('%Y.%m.%d')
        self.mes_actual = datetime.today().strftime('%m%Y')
        self.carpeta_reporte = 'reporte'
        self.carpeta_hoy = os.path.join(self.carpeta_reporte, self.fecha_hoy)
        self.df_asignacion = None
        self.asignacion_path = 'bases/asignacion/base_asignacion_20240902.xlsx'
        self.asignacion_optimizada = 'bases/asignacion/base_asignacion'+ self.mes_actual +'.xlsx'
    
    def base_asignacion(self):
        if self.asignacion_optimizada not in os.listdir('bases/asignacion'):
            optimizar_asignacion(self.asignacion_path, self.asignacion_optimizada)
        self.df_asignacion = cargar_asignacion(self.asignacion_optimizada)
    
    def create_app(self):
        pass
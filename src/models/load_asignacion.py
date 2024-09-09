from tkinter import messagebox
import tkinter as tk
import pandas as pd


def load_asignacion(asignacion_path: str) ->pd.DataFrame | None:
    """
    Este método muestra una ventana emergente que solicita confirmación al usuario para cargar una base de datos 
    de asignación desde un archivo Excel especificado por la ruta 'asignacion_path'. Si el usuario confirma, 
    el archivo se carga en un DataFrame y se muestra un mensaje con la forma (shape) del DataFrame. 
    Si ocurre un error durante la carga, se muestra un mensaje de error.
    
    Parámetros:
    asignacion_path (str): La ruta del archivo Excel que contiene la base de datos de asignación.
    
    Retorna:
    pd.DataFrame | None: El DataFrame si la carga es exitosa, o None si se cancela o si ocurre un error.
    """
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    
    result = messagebox.askquestion("Confirmación", "¿Cargar base de asignación?", icon='warning')
    if result == 'yes':
        try:
            df_asignacion = pd.read_excel(asignacion_path)
            messagebox.showinfo("Información", "Base de asignación cargada correctamente"
                                + "\nShape: " + str(df_asignacion.shape))
            return df_asignacion
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar base de asignación: {e}")
            return None
    return None
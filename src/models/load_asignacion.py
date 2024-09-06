from tkinter import messagebox
import tkinter as tk
import pandas as pd


def cargar_asignacion(asignacion_path: str) ->pd.DataFrame | None:
    try:
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        
        result = messagebox.askquestion("Confirmación", "¿Cargar base de asignación?", icon='warning')
        if result == 'yes':
            df_asignacion = pd.read_excel(asignacion_path)
            messagebox.showinfo("Información", "Base de asignación cargada correctamente"
                                + "\nShape: " + str(df_asignacion.shape))
            return df_asignacion
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar base de asignación: {e}")
        return None
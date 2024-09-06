from tkinter import messagebox
import pandas as pd


def optimizar_asignacion(asignacion_path: str, asignacion_final: str) -> None:
    try:
        df_asignacion = pd.read_excel(asignacion_path)
        shape_inicial = str(df_asignacion.shape)
        
        columnas = [col.upper() for col in df_asignacion.columns]
        df_asignacion.columns = columnas
        
        cols_asignacion = ['CODIGO', 'ID_FLAG', 'CONT_18', 'NOMBRE', 'TIPO_CARTERA', 'TIPO_FONDO', 'CLAVE', 'AGENCIA CORRECTA']
        df_asignacion = df_asignacion[cols_asignacion]
        
        df_asignacion['CONT_18'] = df_asignacion['CONT_18'].apply(lambda x: str(int(x)).zfill(18) if pd.notna(x) else x)
        df_asignacion['CODIGO'] = df_asignacion['CODIGO'].astype('Int64').astype(str).str.zfill(8)
        
        df_asignacion['ID_FLAG'] = 0
        conteo_cc = df_asignacion['CODIGO'].value_counts()
        df_asignacion['ID_FLAG'] = df_asignacion['CODIGO'].map(conteo_cc)
        
        df_asignacion['TIPO_CARTERA'] = df_asignacion['TIPO_CARTERA'].fillna('NULL')
        df_asignacion['TIPO_FONDO'] = df_asignacion['TIPO_FONDO'].fillna('NULL')
        
        shape_final = str(df_asignacion.shape)
        
        df_asignacion.to_excel(asignacion_final, index=False)
        
        messagebox.showinfo("Información", "Base de asignación optimizada correctamente" 
                            + "\nShape inicial: " + shape_inicial
                            + "\nShape final: " + shape_final)
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar base de asignación: {e}")
        return None
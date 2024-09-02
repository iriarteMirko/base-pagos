import pandas as pd

asignacion_path = 'bases/base_asignacion_20240813.xlsx'
df_asignacion = pd.read_excel(asignacion_path)

cols_asignacion = ['codigo', 'ID_FLAG', 'cont_18', 'nombre', 'TIPO_CARTERA', 'TIPO_FONDO', 'clave', 'AGENCIA CORRECTA']
df_asignacion = df_asignacion[cols_asignacion]

df_asignacion['cont_18'] = df_asignacion['cont_18'].apply(lambda x: str(int(x)).zfill(18) if pd.notna(x) else x)
df_asignacion['codigo'] = df_asignacion['codigo'].astype('Int64').astype(str).str.zfill(8)

df_asignacion.to_excel('bases/base_asignacion.xlsx', index=False)
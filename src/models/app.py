from datetime import datetime
from src.models.optimize_asignacion import optimize_asignacion
from src.models.load_asignacion import load_asignacion
from src.utils.resource_path import resource_path
from tkinter import messagebox
from customtkinter import *
import PIL.Image
import threading
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
        # Colores #
        self.color_1 = "#004481"
        self.color_2 = "#2DCCCD"
    
    def base_asignacion(self):
        if self.asignacion_optimizada not in os.listdir('bases/asignacion'):
            optimize_asignacion(self.asignacion_path, self.asignacion_optimizada)
        self.df_asignacion = load_asignacion(self.asignacion_optimizada)
    
    def centrar_ventana(self, ventana: CTk):
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        ventana.update_idletasks()
        ventana_width = ventana.winfo_reqwidth()
        ventana_height = ventana.winfo_reqheight()
        x = (screen_width - ventana_width) // 2
        y = (screen_height - ventana_height) // 2
        ventana.geometry(f"+{x}+{y}")
    
    def deshabilitar_botones(self):
        pass
    
    def habilitar_botones(self):
        pass
    
    def create_app(self):
        self.app = CTk()
        self.app.title("BBVA")
        icon_path = resource_path("src/images/bbva-pe.ico")
        if os.path.isfile(icon_path):
            self.app.iconbitmap(icon_path)
        else:
            messagebox.showwarning("ADVERTENCIA", "No se encontró el archivo 'icono.ico' en la ruta: " + icon_path)
        self.app.resizable(True, True)
        set_appearance_mode("dark")
        
        main_frame = CTkFrame(self.app)
        main_frame.pack_propagate(1)
        main_frame.pack(fill="both", expand=True)
        
        ############## TITULO ##############
        frame_title = CTkFrame(main_frame)
        frame_title.pack(padx=10, pady=(10, 0), fill="both", expand=True, anchor="center", side="top")
        
        titulo = CTkLabel(frame_title, text="BBVA", font=("Arial",20,"bold"))
        titulo.pack(padx=(30,0), fill="both", expand=True, anchor="center", side="left")
        
        image = PIL.Image.open(resource_path("src/images/bbva-png.png"))
        image_duda = CTkImage(image, size=(15, 15))
        self.boton_duda = CTkButton(
            frame_title, image=image_duda, text="", corner_radius=25, border_color=self.color_1,
            fg_color="transparent", hover_color=self.color_2, width=50, command=self.app.destroy)
        self.boton_duda.pack(padx=5, pady=5, ipadx=0, ipady=5, anchor="center", side="left")
        
        image = PIL.Image.open(resource_path("src/images/bbva-png.png"))
        image_config = CTkImage(image, size=(15, 15))
        self.boton_config = CTkButton(
            frame_title, image=image_config, text="", corner_radius=25, border_color=self.color_1,
            fg_color="transparent", hover_color=self.color_2, width=50, command=self.app.destroy)
        self.boton_config.pack(padx=(0,5), pady=5, ipadx=0, ipady=5, anchor="center", side="left")
        
        ############## EJECUTAR ##############
        self.boton_ejecutar = CTkButton(
            main_frame, text="EJECUTAR", text_color="black", font=("Calibri",20,"bold"), fg_color="gray", 
            hover_color=self.color_2, border_color="black", border_width=3, corner_radius=25, height=50, 
            command=self.app.destroy)
        self.boton_ejecutar.pack(padx=10, pady=(10, 0), fill="both", expand=True, anchor="center", side="top")
        
        ############## PROGRESSBAR ##############
        self.progressbar = CTkProgressBar(
            main_frame, mode="indeterminate", orientation="horizontal", progress_color=self.color_1, height=10, border_width=0)
        self.progressbar.pack(padx=10, pady=(10, 0), fill="both", expand=True, anchor="center", side="top")
        
        ############## © ##############
        label_copyrigth = CTkLabel(main_frame, text="© Creado por Mirko Iriarte (P042833)", font=("Calibri",11), text_color=self.color_1)
        label_copyrigth.pack(padx=10, pady=0, fill="both", expand=True, anchor="center", side="bottom")
        
        self.centrar_ventana(self.app)
        self.app.mainloop()
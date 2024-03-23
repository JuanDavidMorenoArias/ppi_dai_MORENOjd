#Librerias para creacion de la app
import tkinter as tk
from tkinter import ttk, messagebox
# Importo la clase de inicio de sesion, registro y funciones
from login import LogInFrame
from intro import IntroFrame
import utils

# Ctypes para que al ejecutar aparezca mi icono en la TaskBar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class App():
    # Init va a correr cada que llamemos la clase como en la linea App()
    def __init__(self):

        self.root = tk.Tk() # crea instancia de la app
        utils.fueltrack_window_style(self.root)
        self.main_show() # Muestra todox
        self.root.mainloop()
        return

    def main_show(self):

        # FRAME DE TITULO, LOGO Y "BY ME"
        self.intro_frame = IntroFrame(self.root)

        # FRAME DE INICIO DE SESION 
        self.login_frame = LogInFrame(self.root,self.on_login)

    def on_login(self, login_successful):
        if login_successful:
            self.intro_frame.destroy()
            self.login_frame.destroy()

                    

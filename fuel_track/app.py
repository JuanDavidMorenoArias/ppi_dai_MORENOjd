#Librerias para creacion de la app
import tkinter as tk
# Importo la clase de inicio de sesion, registro y funciones
from login import LogInFrame
from intro import IntroFrame

import utils
import events
# Ctypes para que al ejecutar aparezca mi icono en la TaskBar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class App():
    # Init va a correr cada que llamemos la clase como en la linea App()
    def __init__(self):

        self.root = tk.Tk() # crea instancia de la app
        utils.fueltrack_window_style(self.root)
        self.entry_show() # Muestra todox
        self.root.mainloop()
        return

    def entry_show(self):

        # FRAME DE TITULO, LOGO Y "BY ME"
        self.intro_frame = IntroFrame(self.root)
        self.intro_frame.place(relx=0.27,rely=0.5,anchor='center')

        # FRAME DE INICIO DE SESION 
        self.login_frame = LogInFrame(self.root,self.on_login)
        self.login_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.login_frame.connect_focus_events()
    
    def on_login(self, login_successful):
        if login_successful:
            self.intro_frame.destroy()
            self.login_frame.destroy()


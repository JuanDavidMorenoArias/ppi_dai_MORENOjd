#Librerias para creacion de la app
import tkinter as tk
from tkinter import ttk, messagebox

# Importa desde la librería Pillow para trabajar con imágenes
from PIL import Image, ImageTk  

# Importo la clase de inicio de sesion
from login import LogInFrame
from register import RegisterFrame

# Ctypes para que al ejecutar aparezca mi icono en la TaskBar
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



class App():
    # Init va a correr cada que llamemos la clase como en la linea App()
    def __init__(self):
        self.root = tk.Tk() # crea instancia de la app
        self.root.geometry('1000x600') # tamaño de ventana
        self.root.resizable(False,False) # no se le podra cambiar el tamaño
        self.root.title('Fueltrack') # titulo de la ventana   
        self.root.config(background='white')
        self.root.iconbitmap("Images/FueltrackIcon.ico") # Imagen en la barra de titulo    
        self.existing_users = self.load_existing_users()
        self.main_show() # Muestra todox
        self.root.mainloop()
        return
    
    # Obtiene los usuarios que ya estan creados
    def load_existing_users(self):
        try: # Leer los nombres de usuario existentes desde el archivo users.txt
            with open('users.txt','r') as file:
                existing_users = {}
                for line in file.readlines():
                    username, password = line.strip().split(',')
                    existing_users[username] = password
            return existing_users
        except FileNotFoundError: # Si no existe el archivo, mas adelante lo creara
            return {}

    def main_show(self):

        # TITULO
        title_image = Image.open("Images/FuelTrackRootTitle.png")
        title_image_tk = ImageTk.PhotoImage(title_image)
        titulito = ttk.Label(self.root, image=title_image_tk,background='white')
        titulito.image = title_image_tk
        titulito.place(relx=0.27, rely=0.7, anchor='center') # FuelTrack

        # ICONO
        icon_image = Image.open("Images/FuelTrackIconImage.png").resize((300,300))
        icon_image_tk = ImageTk.PhotoImage(icon_image)
        logo = ttk.Label(self.root, image=icon_image_tk,background='white')
        logo.image = icon_image_tk
        logo.place(relx=0.27, rely=0.36, anchor='center') # Logotipo Fueltrack

        # BY ME
        by_me = ttk.Label(self.root, text="With love by Juan David Moreno", font=("Forte", 20),foreground='orange')  
        by_me.config(background='white')     
        by_me.place(relx=0.27, rely=0.84, anchor='center') # With love by Juan David Moreno

        # FRAME DE INICIO DE SESION 
        self.login_frame = LogInFrame(self.root,self.switch_to_register,self.existing_users)
        self.login_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.login_frame.connect_focus_events()

    def switch_to_register(self): # El boton de sign up me mande al registro 

        # Destruir la ventana de inicio de sesión
        self.login_frame.destroy()
        # Crear y mostrar la ventana de registro
        self.register_frame = RegisterFrame(self.root, self.switch_to_login,self.existing_users)
        self.register_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.register_frame.connect_focus_events()

    def switch_to_login(self): # El boton de sign in me mande al inicio de sesion

        # Destruir la ventana de registro
        self.register_frame.destroy()
        # Crear y mostrar la ventana de inicio de sesión
        self.login_frame = LogInFrame(self.root, self.switch_to_register,self.existing_users)
        self.login_frame.place(relx=0.75, rely=0.5, anchor='center')
        self.login_frame.connect_focus_events()
        
#Lo necesario para que se ejecute la App cuando se corra este archivo main
if __name__ == '__main__':
    App()
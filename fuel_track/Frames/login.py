
# Importo librerias
import tkinter as tk
from tkinter import ttk, messagebox
import utils
import Frames.register as register

class LogInFrame(tk.Frame):
    # En esta clase 
    def __init__(self,parent, login_callback):
        super().__init__(parent, width=350, height=350, background='white')
        # Yo: el mismo frame
        self.me = self
        # para cerrar
        self.login_callback = login_callback
        # parent: la ventana padre 
        self.parent = parent
        # activa la creacion de widgets
        self.create_widgets()

        
    
    # Creacion de los widgets como botones, entries y textos para la interfaz de inicio de sesion.
    def create_widgets(self): 
        # Texto "Sign In"
        self.heading = ttk.Label(self, text='Sign In', foreground='orange', background='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(relx=0.5, rely=0.1, anchor='center')
        # El entry (espacio para insertar el Username)
        self.user = tk.Entry(self, width=30, foreground='gray', border=0,background='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
        self.user.place(relx=0.1, rely=0.3)
        self.user.insert(0, 'Username')
        self.write_line_user = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.37)
        # El entry (espacio para insertar el Password)
        self.code = tk.Entry(self, width=30, foreground='gray', border=0,background='white', font=('Microsoft YaHei UI Light', 12, 'bold'))
        self.code.place(relx=0.1, rely=0.5)
        self.code.insert(0, 'Password')
        self.write_line_code = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.57)
        # Boton para confirmar que iniciamos sesion con ese Username y Password
        self.sign_in_button = tk.Button(self, cursor='hand2', width=42, pady=7, border=0, text='Sign In',background='orange', foreground='white')
        self.sign_in_button.place(relx=0.1, rely=0.7)
        self.sign_in_button.config(command=self.sign_in)
        # Texto que guia al usuario al registro si no tiene cuenta creada aun
        self.register_getaway = ttk.Label(self, text=r"Don't have an account?",background='white', foreground='black', font=('Microsoft YaHei UI Light', 9, 'bold'))
        self.register_getaway.place(relx=0.20, rely=0.87)
        # Boton cuyo comando nos lleva al registro, eliminando este frame y agregando el del registro
        self.sign_up_button = tk.Button(self, width=8, text='Sign Up',background='white', border=0, cursor='hand2', foreground='orange')
        self.sign_up_button.place(relx=0.65, rely=0.87)
        self.sign_up_button.config(command=self.switch_to_register)

    def connect_focus_events(self):
        # Username
        self.user.bind('<FocusIn>', lambda event: utils.user_on_enter(self.user))
        self.user.bind('<FocusOut>', lambda event: utils.user_on_leave(self.user))
        # Password
        self.code.bind('<FocusIn>', lambda event: utils.code_on_enter(self.code))
        self.code.bind('<FocusOut>', lambda event: utils.code_on_leave(self.code))

    def switch_to_register(self): # El boton de sign up me mande al registro 

        # Destruir la ventana de inicio de sesión
        self.place_forget()
        # Crear y mostrar la ventana de registro
        self.register_frame = register.RegisterFrame(self.parent, self.me)
        self.register_frame.place(relx=0.75,rely=0.5, anchor='center')
        self.register_frame.connect_focus_events()
    

    # El metodo que va ligado al Boton de sign in, que abrira todo lo demas si se inicia sesion :)
    def sign_in(self):
        # lista de los usuarios creados hasta el momento
        existing_users = utils.load_existing_users()
        username = self.user.get().strip()
        password = self.code.get().strip()
        
        # Pregunta si el usuario esta creado
        if username not in existing_users: #si no esta creado envia error
            messagebox.showerror('Error','User not found!')
    
        # ahora pregunta si la contraseña coincide con la creada por el usuario
        else: # si no coincide envia error
            if existing_users[username] != password:
                messagebox.showerror('Error', 'Incorrect password!')
            
            else:
                self.user.delete(0, 'end')
                self.code.delete(0, 'end')
                messagebox.showinfo('Welcome back','Logged in successfully!')
                self.login_callback(True)


    def reshow(self):
        self.place(relx=0.75,rely=0.5, anchor='center')

    
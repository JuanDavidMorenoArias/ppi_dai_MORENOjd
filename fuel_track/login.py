
# Importo librerias
import tkinter as tk
from tkinter import ttk, messagebox

import focuses

class LogInFrame(tk.Frame):
    # En esta clase 
    def __init__(self,parent,switch_to_register, existing_users):
        super().__init__(parent, width=350, height=350, background='white')
        # parent: la ventana padre 
        self.parent = parent
        # switch es el metodo para ir al registro
        self.switch_to_register = switch_to_register
        # almacena los usuarios
        self.existing_users = existing_users
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
        self.user.bind('<FocusIn>', lambda event: focuses.user_on_enter(self.user))
        self.user.bind('<FocusOut>', lambda event: focuses.user_on_leave(self.user))
        self.code.bind('<FocusIn>', lambda event: focuses.code_on_enter(self.code))
        self.code.bind('<FocusOut>', lambda event: focuses.code_on_leave(self.code))
    
    
    # El metodo que va ligado al Boton de sign in, que abrira todo lo demas si se inicia sesion :)
    def sign_in(self):
        username = self.user.get().strip()
        password = self.code.get().strip()

        if username not in self.existing_users:
            messagebox.showerror('Error','User not found!')
        else:
            if self.existing_users[username] != password:
                messagebox.showerror('Error', 'Incorrect password!')
            else:
                messagebox.showinfo('Welcome back','Logged in successfully!')
            

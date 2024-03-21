
# Importo librerias
import tkinter as tk
from tkinter import ttk

class LogInFrame(tk.Frame):
    # En esta clase 
    def __init__(self,parent,switch_to_register):
        super().__init__(parent, width=350, height=350, background='white')
        # parent: la ventana padre 
        self.parent = parent
        # switch es el metodo para ir al registro
        self.switch_to_register = switch_to_register
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

    # Los siguientes son metodos que agregan calidad, focus in and out para los entries que creé
    # cuando enfoco al entry, desaparece el "username" en gris y escribo en negro
    def user_on_enter(self, e):
        name = self.user.get()
        if name == 'Username':
            self.user.delete(0, 'end')
            self.user.config(foreground='black')

    # cuando desenfoco el entry, aparece el "username" en gris (si no hay nada escrito)
    def user_on_leave(self, e):
        name = self.user.get()
        if name == '':
            self.user.config(foreground='gray')
            self.user.insert(0, 'Username')

    # cuando enfoco al entry, desaparece el "Password" en gris, escribo en negro y en asteriscos para ocultar
    def code_on_enter(self, e):
        namei = self.code.get()
        if namei == 'Password':
            self.code.delete(0, 'end')
            self.code.config(foreground='black',show='*')
            
    # cuando desenfoco el entry, aparece el "Password" en gris (si no hay nada escrito)
    def code_on_leave(self, e):
        namei = self.code.get()
        if namei == '':
            self.code.config(foreground='gray',show='')
            self.code.insert(0, 'Password')
            
    # conecto mediante el metodo bind() las funciones que cree con los eventos FocusIn and Out
    def connect_focus_events(self):
        self.user.bind('<FocusIn>', self.user_on_enter)
        self.user.bind('<FocusOut>', self.user_on_leave)
        self.code.bind('<FocusIn>', self.code_on_enter)
        self.code.bind('<FocusOut>', self.code_on_leave)

    # El metodo que va ligado al Boton de sign in, que abrira todo lo demas si se inicia sesion :)
    def sign_in(self):
        username = self.user.get()
        password = self.code.get()

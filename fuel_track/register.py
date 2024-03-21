# Importo mis librerias
import tkinter as tk
from tkinter import ttk, messagebox
import re

class RegisterFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent,switch_to_login):
        super().__init__(parent, width=350, height=450, background='white')
        # Parent: la ventana padre
        self.parent = parent
        #switch es el metodo para ir al inicio de sesion
        self.switch_to_login = switch_to_login
        # almacena los usuarios
        self.existing_users = self.load_existing_users() 
        # activa la creacion de widgets
        self.create_widgets()

    # Obtiene los usuarios que ya estan creados
    def load_existing_users(self):
        try: # Leer los nombres de usuario existentes desde el archivo users.txt
            with open('users.txt','r') as file:
                existing_users = [line.split(',')[0] for line in file.readlines()]
            return existing_users
        except FileNotFoundError: # Si no existe el archivo, mas adelante lo creara
            return []
                
    # Creacion de los widgets del frame, botones, entries y labels de texto
    def create_widgets(self):
        # Texto "Sign Up"
        self.heading = ttk.Label(self, text='Sign Up', foreground='orange', background='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(relx=0.5, rely=0.14, anchor='center')
        # El entry (espacio para insertar el Username)
        self.user = tk.Entry(self, width=30, foreground='gray', background='white', border=0, font=('Microsoft YaHei UI Light', 12, 'bold'))
        self.user.place(relx=0.1, rely=0.3)
        self.user.insert(0, 'Username')
        self.write_line_user = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.35)
        # El entry (espacio para insertar el Password)
        self.code = tk.Entry(self, width=30, foreground='gray', background='white', border=0, font=('Microsoft YaHei UI Light', 12, 'bold'))
        self.code.place(relx=0.1, rely=0.45)
        self.code.insert(0, 'Password')
        self.write_line_code = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.50)
        # El entry (espacio para confirmar la Password antes escrita)
        self.confirm_code = tk.Entry(self, width=30, foreground='gray', background='white', border=0, font=('Microsoft YaHei UI Light', 12, 'bold'))
        self.confirm_code.place(relx=0.1, rely=0.6)
        self.confirm_code.insert(0, 'Confirm Password')
        self.write_line_confirm = tk.Frame(self,width=300,height=2,background='black').place(relx=0.1,rely=0.65)
        # Boton para confirmar que nos registramos con ese Username y Password
        self.sign_up_button = tk.Button(self, cursor='hand2', width=42, pady=7, border=0, text='Create account', background='orange', foreground='white')
        self.sign_up_button.place(relx=0.1, rely=0.76)
        self.sign_up_button.config(command=self.signup)
        # Texto que guia al usuario al Inicio de sesion si ya tiene una cuenta creada
        self.login_getaway = ttk.Label(self, text=r"I have an account", background='white', foreground='black', font=('Microsoft YaHei UI Light', 9, 'bold'))
        self.login_getaway.place(relx=0.25, rely=0.91)
        # Boton cuyo comando nos lleva al logeo, eliminando este frame y agregando el del logeo
        self.sign_in_button = tk.Button(self, width=8, text='Sign In', background='white', border=0, cursor='hand2', foreground='orange')
        self.sign_in_button.place(relx=0.59, rely=0.91)
        self.sign_in_button.config(command=self.switch_to_login)
    
    # Los siguientes son metodos que agregan calidad, focus in and out para los entries que creé
    # cuando enfoco al entry, desaparece el "username" en gris y escribo en negro
    # tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad
    def user_on_enter(self, e):
        name = self.user.get()
        self.user.delete(0, 'end')
        if name == 'Username':
            self.user.config(foreground='black')
        else:
            self.user.insert(0,name.strip())

    # cuando desenfoco el entry, aparece el "username" en gris (si no hay nada escrito)
    def user_on_leave(self, e):
        name = self.user.get()
        if name == '':
            self.user.config(foreground='gray')
            self.user.insert(0, 'Username')

    # cuando enfoco al entry, desaparece el "Password" en gris, escribo en negro 
    # tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad
    def code_on_enter(self, e):
        name = self.code.get()
        self.code.delete(0, 'end')
        if name == 'Password':
            self.code.config(foreground='black')
        else:
            self.code.insert(0,name.strip())

    # cuando desenfoco el entry, aparece el "Password" en gris (si no hay nada escrito)
    def code_on_leave(self, e):
        name = self.code.get()
        if name == '':
            self.code.config(foreground='gray')
            self.code.insert(0, 'Password')

    # cuando enfoco al entry, desaparece el "Confirm Password" en gris, escribo en negro 
    # tambien se encarga de eliminar espacios en blanco para eliminar sensibilidad        
    def confirm_on_enter(self, e):
        name = self.confirm_code.get()
        self.confirm_code.delete(0, 'end')
        if name == 'Confirm Password':
            self.confirm_code.config(foreground='black')
        else: self.confirm_code.insert(0,name.strip())
    
    # cuando desenfoco el entry, aparece el "Confirm Password" en gris (si no hay nada escrito)
    def confirm_on_leave(self, e):
        name = self.confirm_code.get()
        if name == '':
            self.confirm_code.config(foreground='gray')
            self.confirm_code.insert(0, 'Confirm Password')

    # conecto mediante el metodo bind() las funciones que cree con los eventos FocusIn and Out
    def connect_focus_events(self):
        self.user.bind('<FocusIn>', self.user_on_enter)
        self.user.bind('<FocusOut>', self.user_on_leave)
        self.code.bind('<FocusIn>', self.code_on_enter)
        self.code.bind('<FocusOut>', self.code_on_leave)
        self.confirm_code.bind('<FocusIn>', self.confirm_on_enter)
        self.confirm_code.bind('<FocusOut>', self.confirm_on_leave)

    # Funcion para el boton de Create Account, 
    def signup(self):
        
        # Recolecta los datos para comparar
        username = self.user.get().strip()
        password = self.code.get().strip()
        confirm = self.confirm_code.get().strip()

        # Verificar que ningun campo quede vacio
        if not (username and password and confirm):
            messagebox.showerror('Error', 'Please fill in all fields')
            return
        
        # Verificar si la contraseña y el confirm coinciden
        if password != confirm:
            messagebox.showerror('Error', 'Passwords do not match')
            return
        
        #Verificar que el nombre de usuario no este ya en uso
        if username in self.existing_users:
            messagebox.showerror('Error', 'Username already in use')
            return
        
        # Verificar el patrón de la contraseña usando una expresión regular
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
            messagebox.showerror('Error',
                                 'Password must be at least 8 characters long and contain'
                                 'at least one lowercase letter, one uppercase letter, and one digit')
            return
        
        # Si el registro cumplio con todo, guarda al usuario y contraseña
        with open('users.txt', 'a') as file:
            file.write(f"{username},{password}\n")

        # Actualiza la lista de usuarios existentes
        self.existing_users.append(username)

        # Mostra el mensaje de exito
        messagebox.showinfo('Success', 'Account created succesfully')



    
# Importo librerias
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  

class IntroFrame(tk.Frame):
    # En esta clase 
    def __init__(self,parent):
        super().__init__(parent, width=500, height=600, background='white')
        # activa la creacion de widgets
        self.create_widgets()

    def create_widgets(self):

        title_image = Image.open("Images/FuelTrackRootTitle.png")
        title_image_tk = ImageTk.PhotoImage(title_image)
        titulito = ttk.Label(self, image=title_image_tk,background='white')
        titulito.image = title_image_tk
        titulito.place(relx=0.5, rely=0.7, anchor='center') # FuelTrack

        # ICONO
        icon_image = Image.open("Images/FuelTrackIconImage.png").resize((300,300))
        icon_image_tk = ImageTk.PhotoImage(icon_image)
        logo = ttk.Label(self, image=icon_image_tk,background='white')
        logo.image = icon_image_tk
        logo.place(relx=0.5, rely=0.36, anchor='center') # Logotipo Fueltrack

        # BY ME
        by_me = ttk.Label(self, text="With love by Juan David Moreno", font=("Forte", 20),foreground='orange')  
        by_me.config(background='white')     
        by_me.place(relx=0.5, rely=0.84, anchor='center') # With love by Juan David Moreno

import tkinter as tk
from tkinter import ttk

class HomeFrame(tk.Frame):
    # En esta clase
    def __init__(self,parent):
        super().__init__(parent,width=995, height=525, background='red',
                         highlightbackground='white', highlightthickness=0)    
        self.parent = parent
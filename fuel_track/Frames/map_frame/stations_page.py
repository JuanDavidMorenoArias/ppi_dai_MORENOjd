import customtkinter as ctk
from Frames.map_frame.settings import *
from geopy.geocoders import Nominatim

import tkintermapview

class StationsFrame(ctk.CTkFrame):
    # En esta clase
    def __init__(self,parent):
        super().__init__(parent,width=995, height=525, 
                        fg_color=SIDE_PANEL_BG)    
        self.parent = parent

        self.map_widgt = MapWidget(self)

    
class MapWidget(tkintermapview.TkinterMapView):
    def __init__(self,parent):
        super().__init__(parent,width=796,height=525,corner_radius=5)

        self.place(relx=0.2,rely=0)
        self.set_location_pos()

    def set_location_pos(self):
        self.set_address("Facultad de minas, Medellín,Colombia")
        self.set_zoom(14)
        
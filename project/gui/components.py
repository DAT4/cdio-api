import tkinter as tk
from PIL import Image, ImageTk
from .db import DatabaseView, DBType

class ImageView(tk.Label):
    def __init__(self, img, dim, pos, master=None):
        super().__init__(master)
        self.master = master
        x,y = pos
        self.grid(row=x, column=y, padx=5, pady=5)
        self.set_image(img.copy(), dim)

    def set_image(self, img, dim):
        img = Image.fromarray(img)
        img = img.resize(dim, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.imgtk = img
        self.config(image=img)


class InfoView(tk.Frame):
    def __init__(self, stuff, pos, master=None):
        super().__init__(master)
        self.master = master
        x,y = pos
        self.grid(row=x, column=y, padx=5, pady=5)
        self.create_widgets(stuff)

    def create_widgets(self, stuff):
        self.num    = ImageView(stuff['num'], (50,50), (0,0), master=self)
        self.sym    = ImageView(stuff['sym'], (50,50), (0,1), master=self)
        self.db_num = DatabaseView(stuff['num'], DBType.NUMBER,(1,0), master=self)
        self.db_sym = DatabaseView(stuff['sym'], DBType.SYMBOL,(1,1), master=self)

import tkinter as tk
from cvengine import edge as im
from .components import ImageView, InfoView

class CardScollerView(tk.Frame):
    def __init__(self, images, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.images = images
        self.index = 0
        self.create_widgets()
        self.showtime()

    def go_left(self):
        self.index = (self.index+1)%len(self.images)
        self.showtime()

    def go_right(self):
        self.index = (self.index-1)%len(self.images)
        self.showtime()

    def showtime(self):
        img = im.get(self.images[self.index])
        stuff = im.get_the_stuff(img)
        self.info = InfoView(stuff, (0,1), master=self)
        self.card = ImageView(stuff['card'], (300,500), (1,1), master=self)

    def exit(self):
        self.master.set_menu_view()

    def create_widgets(self):
        self.btn_left = tk.Button(self, text='<', command=self.go_left, height=10)
        self.btn_left.grid(row=1, column=0, padx=5, pady=5)

        self.btn_right = tk.Button(self, text='>', command=self.go_right, height=10)
        self.btn_right.grid(row=1, column=2, padx=5, pady=5)

        self.btn_exit = tk.Button(self, text='exit', command=self.exit)
        self.btn_exit.grid(row=2, column=1, padx=5, pady=5)


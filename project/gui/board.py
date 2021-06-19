import tkinter as tk
from itertools import chain
from cvengine import edge as im
from .components import ImageView

def make_positions():
    def is_place(x,y): return y!=1 or x!=1 and x!=2
    return list(chain(*[[(x,z)
        for z in y]
        for x,y in enumerate([[x
            for x in range(7) if is_place(x,y)]
            for y in range(2)])]))

class BoardView(tk.Frame):
    def __init__(self, image_path, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        card_images = im.cards_from_board(im.get(image_path))

        self.create_widgets(card_images)

    def exit(self):
        self.master.set_menu_view()

    def create_widgets(self, cards):
        self.cards = [ImageView(img,(150,250), pos, master=self)
                for img,pos
                in zip(cards, make_positions())]

        self.btn_exit = tk.Button(self, text='exit', command=self.exit)
        self.btn_exit.grid(row=3, column=0, padx=5, pady=5)


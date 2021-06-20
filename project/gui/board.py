import tkinter as tk
from itertools import chain
from cvengine import edge as im
from .components import ImageView
from .cardscroller import CardScollerView

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
        self.images = im.split_board(im.get(image_path))
        self.master = master
        self.grid()
        self.create_widgets(self.images)

    def scroll(self):
        cards = [im.get_card(x) for x in self.images]
        self.scroller = CardScollerView(stuff, master=self)

    def exit(self):
        self.master.set_menu_view()

    def create_widgets(self, images):
        self.cards = [ImageView(img,(150,250), pos, master=self)
                for img,pos
                in zip(im.cards_from_list(images), make_positions())]

        self.btn_exit = tk.Button(self, text='exit', command=self.exit)
        self.btn_exit.grid(row=3, column=0, padx=5, pady=5)

        self.btn_scrollview = tk.Button(self, text='scroll', command=self.scroll)
        self.btn_scrollview.grid(row=4, column=0, padx=5, pady=5)


import tkinter as tk
from tkinter import filedialog
from os import listdir

class MenuView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def get_board(self):
        image_path = tk.filedialog.askopenfilename()
        self.master.set_board_view(image_path)

    def get_images_from_folder(self):
        path = tk.filedialog.askdirectory()
        images_in_path = [f'{path}/{x}'
                for x in listdir(path)
                if x[-3:] == 'jpg']
        self.master.set_card_scroller_view(images_in_path)

    def create_widgets(self):
        self.btn_load = tk.Button(self, text='load folder', command=self.get_images_from_folder)
        self.btn_load.grid(row=0, column=0, padx=5, pady=5)

        self.btn_load = tk.Button(self, text='load board', command=self.get_board)
        self.btn_load.grid(row=1, column=0, padx=5, pady=5)


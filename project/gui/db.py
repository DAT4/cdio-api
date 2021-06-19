import os
import tkinter as tk
from enum import Enum
from database.mongo import MongoDB

def start_db():
    mongo_uri = os.environ['CDIO_MONGO_PASS']
    return MongoDB(mongo_uri)

class DBType(Enum):
    NUMBER = 1
    SYMBOL = 2

DATABASE = start_db()

OPTIONS = {
        DBType.NUMBER: [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
            ],
        DBType.SYMBOL: [
                "S",
                "D",
                "C",
                "H",
            ],
        }

SAVEFUNCS = {
        DBType.SYMBOL: DATABASE.save_symbol,
        DBType.NUMBER: DATABASE.save_number,
        }


class DatabaseView(tk.Frame):
    def __init__(self, image, db_type, pos, master=None):
        super().__init__(master)
        x, y            = pos
        self.image      = image
        self.db_type    = db_type
        self.master     = master
        self.options    = OPTIONS[db_type]
        self.choice     = tk.StringVar(self)

        self.grid(row=x, column=y)
        self.choice.set(self.options[0])

        self.create_widgets()

    def save_choice(self):
        SAVEFUNCS[self.db_type](self.image, self.choice.get())

    def create_widgets(self):
        self.menu   = tk.OptionMenu(self,self.choice, *self.options)
        self.btn    = tk.Button(self, text="save", command=self.save_choice)
        self.menu.grid(row=0, column=0, padx=5,pady=5)
        self.btn.grid(row=0, column=1, padx=5,pady=5)


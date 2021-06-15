from core import *
from os import listdir
import cv2 as cv
import tkinter as tk
from tkinter import OptionMenu, StringVar, filedialog, Tk
from tkinter import Text, W, N, E, S, Button
from tkinter.ttk import Frame, Style, Label
from PIL import Image, ImageTk
from database import *


OPTIONS_SYM = [
    "S",
    "D",
    "C",
    "H"
]

OPTIONS_NUM = [
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
    "K"
]

t, b = None, None

root = Tk()
root.geometry("400x600")
root.resizable(width=0, height=0)
root.title("CDIO - Final Project")

images = None
index = 0
path    = filedialog.askdirectory()
images  = [f'{path}/{x}'for x in listdir(path) if x[-3:] == 'jpg'] 

def go_left(): 
    global index, images
    index = (index+1)%len(images)
    get_image(images[index])

def go_right(): 
    global index, images
    index = (index-1)%len(images)
    print(index)
    print(images[index])
    get_image(images[index])

def save_num():
    save_number(t,variable_num.get())

def save_sym():
    save_symbol(b,variable_sym.get())

def get_image(path):
    global t,b
    img     = find_card(get(path))
    t, b    = extract_cornor(img)

    top = Image.fromarray(t)
    top = top.resize((100,100), Image.ANTIALIAS)
    top = ImageTk.PhotoImage(top)

    bot = Image.fromarray(b)
    bot = bot.resize((100,100), Image.ANTIALIAS)
    bot = ImageTk.PhotoImage(bot)

    img = Image.fromarray(img)
    img = img.resize((200,300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    panel1.imgtk = top 
    panel1.config(image=top)
    panel2.imgtk = bot 
    panel2.config(image=bot)
    panel3.imgtk = img
    panel3.config(image=img)


leftbtn     = Button(root, text="<", width=1, height=20, command=go_left)
rightbtn    = Button(root, text=">", width=1, height=20, command=go_right)

oframe      = Frame(root, width=200, height=100)
uframe      = Frame(oframe, width=200, height=500)
lframe      = Frame(oframe, width=300, height=500)

panel1      = Label(master=uframe)
panel2      = Label(master=uframe)
panel3      = Label(master=lframe)

variable_sym = StringVar(uframe)
variable_sym.set(OPTIONS_SYM[0]) # default value
dropdown_sym = OptionMenu(uframe,variable_sym, *OPTIONS_SYM)

variable_num = StringVar(uframe)
variable_num.set(OPTIONS_NUM[0]) # default value
dropdown_num = OptionMenu(uframe,variable_num, *OPTIONS_NUM)

save_num_btn = Button(uframe, text="save num", command=save_num)
save_sym_btn = Button(uframe, text="save sym", command=save_sym)

leftbtn.grid(row=0, column=0,padx=10, pady=5)
oframe.grid(row=0, column=1,padx=10, pady=5)
rightbtn.grid(row=0, column=2,padx=10, pady=5)

dropdown_num.grid(row=1, column=0, padx=10, pady=5)
dropdown_sym.grid(row=1, column=1, padx=10, pady=5)

save_num_btn.grid(row=2, column=0, padx=10, pady=5)
save_sym_btn.grid(row=2, column=1, padx=10, pady=5)


uframe.grid(row=0, column=0, padx=10, pady=5)
lframe.grid(row=1, column=0, padx=10, pady=5)

panel1.grid(row=0, column=0, padx="10", pady="10")
panel2.grid(row=0, column=1, padx="10", pady="10")

panel3.grid(row=0, column=1, padx="10", pady="10")


get_image(images[index])
root.mainloop()

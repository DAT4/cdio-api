from core import *
from os import listdir
import cv2 as cv
import tkinter as tk
from tkinter import filedialog, Tk, RIGHT, LEFT, BOTH, RAISED, CENTER
from tkinter import Text, W, N, E, S, Button
from tkinter.ttk import Frame, Style, Label
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x500")
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

def get_image(path):
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

leftbtn.grid(row=0, column=0,padx=10, pady=5)
oframe.grid(row=0, column=1,padx=10, pady=5)
rightbtn.grid(row=0, column=2,padx=10, pady=5)

uframe.grid(row=0, column=0, padx=10, pady=5)
lframe.grid(row=1, column=0, padx=10, pady=5)

panel1.grid(row=0, column=0, padx="10", pady="10")
panel2.grid(row=0, column=1, padx="10", pady="10")

panel3.grid(row=0, column=1, padx="10", pady="10")


get_image(images[index])
root.mainloop()

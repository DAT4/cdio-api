from core import *
from os import listdir
import cv2 as cv
import tkinter as tk
from tkinter import OptionMenu, StringVar, filedialog, Tk
from tkinter import Text, W, N, E, S, Button
from tkinter.ttk import Frame, Style, Label
from PIL import Image, ImageTk
from database import *

root = Tk()
root.geometry("400x600")
root.resizable(width=0, height=0)
root.title("CDIO - Final Project")

index = 0
images  = [x['number'] for x in get_all_nums()] 

def go_left(): 
    global index, images
    index = (index+1)%len(images)
    get_image(images[index])

def go_right(): 
    global index, images
    index = (index-1)%len(images)
    get_image(images[index])

def get_image(image):

    img = Image.fromarray(image)
    img = img.resize((100,100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    panel1.imgtk = img 
    panel1.config(image=img)


leftbtn     = Button(root, text="<", width=1, height=20, command=go_left)
rightbtn    = Button(root, text=">", width=1, height=20, command=go_right)

oframe      = Frame(root, width=200, height=100)

panel1      = Label(master=oframe)

leftbtn.grid(row=0, column=0,padx=10, pady=5)
oframe.grid(row=0, column=1,padx=10, pady=5)
rightbtn.grid(row=0, column=2,padx=10, pady=5)

panel1.grid(row=0, column=0, padx="10", pady="10")

get_image(images[index])
root.mainloop()

from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox


def function1():
    os.system("py testing.py")


def function2():
    os.system("py take_images.py")


def function6():
    window.destroy()


def ask_cancel():
    if tk.messagebox.askokcancel('Exit', "Do you really want to exit ? "):
        tk._exit()
    tk.mainloop()


window = Tk()
window.title("Face recognition application")
window.geometry('600x450')
bgi = PhotoImage(file="imagesforwindows/bg1.png")
mylabel = Label(window, image=bgi)
mylabel.place(x=0, y=0)

btn1 = Button(window, text="New user", bg="#000080", fg="#ffffff", font='Helvetica 12 bold', command=function2,
              width=15).place(x=80, y=340)
btn2 = Button(window, text="Recognize user", bg="#000080", fg="#ffffff", font='Helvetica 12 bold', command=function1,
              width=15).place(x=350, y=340)
btn4 = Button(window, text="Exit", bg="#8B0000", fg="#ffffff", font='Helvetica 12 bold', command=ask_cancel,
              width=20).place(x=190, y=400)
p1 = PhotoImage(file='imagesforwindows/icon.png')
window.iconphoto(False, p1)

window.mainloop()

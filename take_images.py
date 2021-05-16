import tkinter as tk
from tkinter import *
import os
from tkinter import messagebox
import cv2

path = 'imagescaptured'
myList = os.listdir(path)
window = Tk()
window.title("Add user")
myimage=Canvas(window,height=450,width = 600)
myimage.pack(fill="both", expand = "True")
bgi=PhotoImage(file="imagesforwindows/bg2.png")
myimage.create_image(0,0,image=bgi,anchor="nw")
myimage.create_text(120,40,text="Enter your name :",font=("Helvetica 12 bold"),fill="white")

inputtxt = tk.Entry(window)

myimage.create_window(270, 40, window=inputtxt,width=140, height=25)

inp = inputtxt.get()


def show_input():
    if len(inputtxt.get()) == 0:
        tk.messagebox.showerror("Error", "Name cannot be 'None'")
        return False
    elif f'{inputtxt.get()}.jpg' in myList:
        tk.messagebox.showerror("Error", "Name already exists")
        return False
    else:
        name = inputtxt.get()
        tk.messagebox.showinfo(title="Capture", message="We will take a photo of you")
        return capture()


btn1 = Button(window, text="Capture", command=show_input, bg="#000080", fg="#ffffff", font='Helvetica 10 bold',
              width=11).place(x=400, y=25)
btn2 = Button(window, text="Home", command=exit, bg="#8B0000", fg="#ffffff", font='Helvetica 12 bold', width=15).place(
    x=220, y=400)


def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure?"):
        window.destroy()


def capture():
    name = inputtxt.get()
    num_of_images = 0
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    vid = cv2.VideoCapture(0)
    while True:

        ret, img = vid.read()
        new_img = None
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = detector.detectMultiScale(image=grayimg, scaleFactor=1.1, minNeighbors=5)
        for x, y, w, h in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "Face Detected", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
            cv2.putText(img, str(str(num_of_images) + " imagesforwindows captured"), (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255))
            new_img = img[y:y + h, x:x + w]
        cv2.imshow("FaceDetection", img)
        key = cv2.waitKey(1) & 0xFF

        try:
            cv2.imwrite(str(path + "/" + name + ".jpg"), new_img)
            num_of_images += 1
        except:

            pass
        if key == ord("q") or key == 27 or num_of_images > 20:
            break
    cv2.destroyAllWindows()

p1 = PhotoImage(file='imagesforwindows/icon.png')
window.iconphoto(False, p1)
window.mainloop()

import cv2
import numpy as np
import face_recognition
import os
from tkinter import *

path = 'imagescaptured'
mylistofimages=os.listdir(path)
print(mylistofimages)
images = []
listnames=[]
for element in mylistofimages:
    img = cv2.imread(f'{path}/{element}')
    images.append(img)
    listnames.append(os.path.splitext(element)[0])
print(listnames)


def findEncodings(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode =face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

print(len(findEncodings(images)))

encodeListKnown = findEncodings(images)
print('Encoding Complete')

capture = cv2.VideoCapture(0)
while True:
    # this will capture our image
    success,img = capture.read()
    # on va diminuer la taille de l'image dont le but d'accelerer le processus
    imageSmaller=cv2.resize(img,(0,0),None,0.25,0.25)
    imageSmaller=cv2.cvtColor(imageSmaller,cv2.COLOR_BGR2RGB)
    faceCurrentframe = face_recognition.face_locations(imageSmaller)
    encoding_currentframe=face_recognition.face_encodings(imageSmaller, faceCurrentframe)
    for encodeface, facelocation in zip(encoding_currentframe, faceCurrentframe):
        comparefaces = face_recognition.compare_faces(findEncodings(images),encodeface)
        facesdistances = face_recognition.face_distance(findEncodings(images),encodeface)
        print(facesdistances)
        indexminvalue = np.argmin(facesdistances)
        if comparefaces[indexminvalue]:
            name = listnames[indexminvalue]
            y1,x2,y2,x1=facelocation
            # on a multiplié les 4 mesures du imagelocation par 4 car on a diminué la taille de l'image dernierement
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            # encadrer l'imagesforwindows et ecrivant le nom de ch

            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),(cv2.FONT_HERSHEY_COMPLEX),1,(255,255,255),2)
            print(True)
            capture.release()
            window = Tk()
            window.title("User recognized")
            window.geometry('600x450')
            myimage = Canvas(window, height=450, width=600)
            myimage.pack(fill="both", expand="True")
            bgi = PhotoImage(file="imagesforwindows/bg2.png")
            myimage.create_image(0, 0, image=bgi, anchor="nw")
            myimage.create_text(120, 40, text="Hello "+name, font=("Helvetica 12 bold"), fill="white")
            btn2 = Button(window, text="Home", command=exit, bg="#8B0000", fg="#ffffff", font='Helvetica 12 bold',
                          width=15).place(
                x=220, y=400)

            window.mainloop()
        else:
            y1, x2, y2, x1 = facelocation
            # on a multiplié les 4 mesures du imagelocation par 4 car on a diminué la taille de l'image dernierement
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            # encadrer l'imagesforwindows et ecrivant le nom de ch
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, "inknown", (x1 + 6, y2 - 6), (cv2.FONT_HERSHEY_COMPLEX), 1, (0, 255, 255), 2)
            print("non enregistré")



    cv2.imshow('webcam',img)
    cv2.waitKey(1)






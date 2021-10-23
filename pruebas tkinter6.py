from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils


cap = None
root = Tk()

btnIniciar = Button(root, text="Iniciar", width=45, command="")
btnIniciar.grid(column=0, row=0, padx=5, pady=5)



btnFinalizar = Button(root, text="Finalizar", width=45, command="")
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)


lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)


root.title("LiSa")
root.geometry('800x600')
imagen=PhotoImage(file="sentadilla.png")
fondo=Label(root, image=imagen) .place(x=0,y=40)
root.mainloop()



root.mainloop()    
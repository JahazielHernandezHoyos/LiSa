from tkinter import *
import PIL
import imutils
import cv2
import mediapipe as mp


cap = None
ventana = Tk()
ventana.geometry('800x600')





btnIniciar = Button(ventana, text="Iniciar", width=45, command=mediapipe)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(ventana, text="Finalizar", width=45, command="")
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)


lblVideo = Label(ventana)
lblVideo.grid(column=0, row=1, columnspan=2)


ventana.title("LiSa")
# imagen=PhotoImage(file="sentadilla.png")
# fondo=Label(ventana, image=imagen) .place(x=0,y=40)
# ventana.mainloop()





ventana.mainloop()    
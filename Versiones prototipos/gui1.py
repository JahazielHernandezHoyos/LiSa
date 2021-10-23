from tkinter import *
import tkinter as tk
window = Tk()
window.title("LiSa")
window.geometry('800x600')
imagen=PhotoImage(file="sentadilla.png")
fondo=Label(window, image=imagen) .place(x=0,y=0)
window.mainloop()

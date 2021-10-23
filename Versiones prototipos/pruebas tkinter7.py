from tkinter import *

root = Tk()
lbred = Label(root,text="Red",fg="Red",relief=GROOVE)
lbred.pack(fill=X)
lbblue = Label(root,text="azul",fg="blue",relief=GROOVE)
lbblue.pack(fill=Y)         # El control llena el control desocupado en la dirección horizontal
root.mainloop()
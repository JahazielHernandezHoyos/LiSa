from tkinter import *
import tkinter
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import mediapipe as mp

ventana = tkinter.Tk()
ventana.geometry("640x480")

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#cap = cv2.VideoCapture("video_0002.mp4")
cap = cv2.VideoCapture(0)

def mediapipe():
    with mp_pose.Pose(static_image_mode=False) as pose:

        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

            if results.pose_landmarks is not None:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
                    mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

btnIniciar = Button(ventana, text="Iniciar", width=30, command=mediapipe)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(ventana, text="Finalizar", width=30, command="")
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

lbred = Label(ventana,text="Numero de sentadiilas",fg="Red",relief=GROOVE, bg="blue")
lbred.grid(column=2, row=5, padx=40, pady=40)

lbblue = Label(ventana,text="Calificacion",fg="blue",relief=GROOVE, bg="red")
lbblue.grid(column=2, row=20, padx=40, pady=40)

ventana.mainloop()    

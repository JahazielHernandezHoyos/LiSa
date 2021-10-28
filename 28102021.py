from tkinter import *
import tkinter
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import mediapipe as mp
import numpy as np
from math import acos, degrees

ventana = tkinter.Tk()
ventana.configure(bg= "#9EDED5")
ventana.geometry("1200x500")
#cap = cv2.VideoCapture("Multimedia\sentadilla.mp4")
cap = cv2.VideoCapture(0)

def mediapipe():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    ARRIBA = False
    ABAJO = False
    count = 0
    with mp_pose.Pose(
        static_image_mode=False) as pose:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            frame = cv2.flip(frame, 1)
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            if results.pose_landmarks is not None:
                mp_drawing.draw_landmarks( frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(128, 250, 250), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(255,255,255), thickness=2))
                x1 = int(results.pose_landmarks.landmark[24].x * width)
                y1 = int(results.pose_landmarks.landmark[24].y * height)
                x2 = int(results.pose_landmarks.landmark[26].x * width)
                y2 = int(results.pose_landmarks.landmark[26].y * height)
                x3 = int(results.pose_landmarks.landmark[28].x * width)
                y3 = int(results.pose_landmarks.landmark[28].y * height)
                p1 = np.array([x1, y1])
                p2 = np.array([x2, y2])
                p3 = np.array([x3, y3])
                l1 = np.linalg.norm(p2 - p3)
                l2 = np.linalg.norm(p1 - p3)
                l3 = np.linalg.norm(p1 - p2)
                # Calcular el ángulo
                angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                if angle >= 160:
                        ARRIBA = True
                if ARRIBA == True and ABAJO == False and angle <= 90:
                        ABAJO = True
                if ARRIBA == True and ABAJO == True and angle >= 160:
                        count += 1
                        ARRIBA = False
                        ABAJO = False
                #print("count: ", count)
                # Visualización
                aux_image = np.zeros(frame.shape, np.uint8)
                cv2.line(aux_image, (x1, y1), (x2, y2), (0, 255, 255), 20)
                cv2.line(aux_image, (x2, y2), (x3, y3), (0, 255, 255), 20)
                cv2.line(aux_image, (x1, y1), (x3, y3), (0, 255, 255), 5)
                contours = np.array([[x1, y1], [x2, y2], [x3, y3]])
                cv2.fillPoly(aux_image, pts=[contours], color=(70, 70, 70))
                output = cv2.addWeighted(frame, 1, aux_image, 0.8, 0)
                cv2.circle(output, (x1, y1), 6, (0, 0, 0), 4)
                cv2.circle(output, (x2, y2), 6, (255, 255, 255), 4)
                cv2.circle(output, (x3, y3), 6, (255, 255, 255), 4)
                cv2.rectangle(output, (0, 0), (60, 60), (255, 255, 255), -1)
                cv2.putText(output, str(int(angle)), (x2 + 30, y2), 1, 1.5, (128, 250, 250), 2)
                cv2.putText(output, str(count), (10, 50), 1, 3.5, (0, 0, 0), 2)
                cv2.putText(output, "Angulo debe llegar a 80", (50, 50), 1, 1, (0, 0, 0), 2)
                cv2.imshow("output", output)

            cv2.imshow("Frame", frame)

            # Aqui se coloca la condicion para el contador de sentadillas y el numero para que haga su cierre o llamar otra funcion
            if count == 20:
                break
            if cv2.waitKey(1) & 0xFF == 27:
                break     
             
        cap.release()
        cv2.destroyAllWindows()
        

def finalizar_limpiar():
    cap.release()
    cv2.destroyAllWindows()
    ventana.destroy() 

btnIniciar = Button(ventana, text="Iniciar Sesion de sentadillas", width=30, command=mediapipe)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(ventana, text="Finalizar", width=30, command=finalizar_limpiar)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

lbblue = Label(ventana,text="CÓMO HACER BIEN LAS SENTADILLAS\n" 
        "Abre tus piernas hasta el ancho de tus hombros. \n"
        "Junta tus manos o estira tus brazos en un ángulo de 90 grados.\n"
        "Cuando vayas a bajar, mantén los glúteos hacia atrás.\n" 
        "Haz como si fueras a sentarte en una silla imaginaria. \n"
        "Es importante que las rodillas no sobrepasen la punta de tus pies,\n" 
        "siempre deben quedar por detrás. Debes intentar mantener \n"
        "la espalda erguida en todo momento y evitar inclinarte demasiado hacia adelante. \n"
        "Cuando bajes, inspira, te será más fácil bajar y mantener la espalda recta.",
        fg="black",relief=GROOVE, bg="white")
lbblue.grid(column=1, row=1, padx=40, pady=40)

ventanidaabajo = Label(ventana,text="Despues de 10 sentadillas se cerrara el programa",fg="black",relief=GROOVE, bg="white")
ventanidaabajo.grid(column=0, row=3, padx=20, pady=20)



imagen=PhotoImage(file="sentadilla1.png")
fondo=Label(ventana, image=imagen) .grid(column=0, row=1)

ventana.mainloop() 


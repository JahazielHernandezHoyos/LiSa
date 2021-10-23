from tkinter import *
import tkinter
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = None
root = Tk()


def iniciar():
    global cap
    cap = cv2.VideoCapture(0)
    visualizar()

def mediapipe(frame):
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
    return frame
    # with mp_pose.Pose(
    # min_detection_confidence=0.5,
    # min_tracking_confidence=0.5) as pose:

    #     if cap is not None:
    #         ret, frame = cap.read()
    #         if ret == True:
    #             frame = imutils.resize(frame, width=640)
    #             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #             # To improve performance, optionally mark the image as not writeable to
    #             # pass by reference.
    #             frame.flags.writeable = False
    #             frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #             results = pose.process(frame)

    #             # Draw the pose annotation on the image.
    #             frame.flags.writeable = True
    #             frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #             mp_drawing.draw_landmarks(
    #                 frame,
    #                 results.pose_landmarks,
    #                 mp_pose.POSE_CONNECTIONS,
    #                 landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    #             im = Image.fromarray(frame)
    #             img = ImageTk.PhotoImage(image=im)

    #             lblVideo.configure(image=img)
    #             lblVideo.image = img
    #             lblVideo.after(10, visualizar)

    #             mi_Frame=Frame()
    #             mi_Frame.pack(side='left') #Configurar el metodo pack()
    #             mi_Frame.config(bg="blue")
    #             mi_Frame.config(width="150", height="150")

    #             return frame

def visualizar():
    global cap
    ret, frame = cap.read()
    if ret == True:
        frame = imutils.resize(frame, width=640)
        frame = mediapipe(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, visualizar)
    else:
        lblVideo.image = ""
        cap.release()

def finalizar():
    global cap
    cap.release()



btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)

root.mainloop()    




# cap = cv2.VideoCapture(0)

#   while cap.isOpened():
#     ret, frame = cap.read()
    

    
#     # Flip the image horizontally for a selfie-view display.
#     cv2.imshow('MediaPipe Pose', cv2.flip(frame, 1))
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()


import cv2
import tkinter as tk
from PIL import Image, ImageTk


cap = cv2.VideoCapture(0)

window = tk.Tk()
window.title("Live Webcam Feed")
label = tk.Label(window)
label.pack()

def update_frame():
    ret, frame = cap.read()
    if ret:

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)  # 1 = horizontal flip, 0 = vertical, -1 = both
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    
    label.after(10, update_frame)

update_frame()

window.mainloop()
cap.release()

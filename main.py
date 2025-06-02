import tkinter as tk
import time
import cv2
from PIL import Image, ImageTk

from webcam.capture import WebcamCapturer
from webcam.inference import ObjectDetector
from webcam.display import DisplayFrames

from model.load_model import model
import numpy as np
import warnings
warnings.filterwarnings("ignore", message=".*torch.cuda.amp.autocast.*is deprecated.*")


frames = WebcamCapturer(src = 0, width = 640, height = 480, fps = 30)
detector = ObjectDetector(model,0.4)
displayer = DisplayFrames(color = (36,255,12), thickness = 2, font = cv2.FONT_HERSHEY_SIMPLEX)


window = tk.Tk()
window.title("Live Webcam Feed")
label = tk.Label(window)
label.pack()

prev_frame_time = 0

def update_frame():
    global prev_frame_time

    frame = frames.read()
    detections = detector.predict(frame)
    print(detections)
    
    new_frame_time = time.time()
    fps = int(1/(new_frame_time-prev_frame_time))
    prev_frame_time = new_frame_time
    
    frame = displayer.draw_frames(frame,detections,fps)
    
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    label.after(10, update_frame)

update_frame()

window.mainloop()

frames.release()
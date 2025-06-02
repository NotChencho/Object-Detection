import cv2

class WebcamCapturer():

    def __init__(self, src = 0, width = 640, height = 480, fps = 24):

        self.cap = cv2.VideoCapture(src)
        
        # Width
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        # Height
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        # Frames per second
        self.cap.set(cv2.CAP_PROP_FPS, fps)

        # For veryfuing
        self.v_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.v_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.v_fps = self.cap.get(cv2.CAP_PROP_FPS)
        print(f"Webcam initialized: Width={self.v_width}, Height={self.v_height}, FPS={self.v_fps}")


    def read(self):

        ret, frame = self.cap.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)  # 1 = horizontal flip, 0 = vertical, -1 = both
            return frame
        
        else:
            return None
    
    def release(self):

        self.cap.release()

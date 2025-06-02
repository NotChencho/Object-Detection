import numpy as np

class ObjectDetector():

    def __init__(self, model = "yolov5n.pt", conf_threshold = 0.5):

        self.model = model
        self.conf_threshold = conf_threshold
    
    def predict(self, frame):
        
        result = self.model(frame)
        df = result.pandas().xyxy[0]
        df = df[df.confidence >= self.conf_threshold].drop(columns=["class"])

        out = np.array(df)

        if out.shape[0] > 0:
            return out
        
        else:
            None
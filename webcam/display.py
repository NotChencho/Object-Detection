import cv2

class DisplayFrames():
        
        def __init__(self, color = (36,255,12), thickness = 2, font = cv2.FONT_HERSHEY_SIMPLEX):
                
                self.color = color
                self.thickness = thickness
                self.font = font
        
        def draw_frames(self, inp, detections, fps):

            frame = cv2.putText(inp,f"FPS: {str(fps)}", (570, 20), self.font, 0.5, self.color, self.thickness)
        
            if detections is None or len(detections) == 0:
    
                  return frame

            else:

                for detection in detections:

                    x1 = int(detection[0])
                    y1 = int(detection[1])
                    x2 = int(detection[2])
                    y2 = int(detection[3])
                
                    y3 = int(detection[1]) -10

                    pt1 = (x1, y1)
                    pt2 = (x2, y2)

                    pt3 = (x1,y3)

                    frame = cv2.rectangle(inp, pt1, pt2, color=self.color, thickness=self.thickness)
                    frame = cv2.putText(frame,f"{detection[5]}: {round(detection[4],3)}", pt3, self.font, 0.5, self.color, self.thickness)

                return frame

from ultralytics import YOLO
import numpy
import cv2
import os

#Activate Webcam
model = YOLO('Component_Detection/Versions/v.5 200epoc/weights/best.pt')
detection_output = model.predict(source="0", conf=0.25, stream=False, save=True)

# Display tensor array
print(detection_output)

# Display numpy array
print(detection_output[0].numpy())
from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import numpy
import cv2
import os

version_dir = ['Component_Detection/Versions/v.1 1epoc/weights/best.pt', 'Component_Detection/Versions/v.2 5epoc/weights/best.pt', 'Component_Detection/Versions/v.3 20epoc/weights/best.pt', 'Component_Detection/Versions/v.4 100epoc/weights/best.pt', 'Component_Detection/Versions/v.5 200epoc/weights/best.pt']
def ai(input):
    # load a pretrained YOLOv8n model
    model = YOLO(version_dir[int(input.replace('v', ''))-1])
    # predict on an image
    f = open('Component_Detection/versions.txt')
    lines = f.read().split('\n')
    print(lines)
    for path in get_relative_paths():
        detection_output = model.predict(source='Component_Detection/Test/'+path, conf=0.25, save=True) #Webcam (source="0", conf=0.25,stream=True)
    # Display tensor array
    print(detection_output)

    # Display numpy array
    print(detection_output[0].numpy())
def get_relative_paths():
    directory = "Component_Detection\Test"
    relative_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            relative_paths.append(relative_path)
    return relative_paths
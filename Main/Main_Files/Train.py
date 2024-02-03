from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML 'yolov8(n,s,m,l,x).yaml'

# Train the model
results = model.train(data='Component_Detection\config.yaml', epochs=200)
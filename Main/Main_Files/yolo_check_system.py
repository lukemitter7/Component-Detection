import ultralytics
ultralytics.checks()

from roboflow import Roboflow
rf = Roboflow(api_key="ufdRg3M1TJhzxlDSFYOQ")
project = rf.workspace("new-workspace-rzrja").project("pcb-phir-se-labeling")
dataset = project.version(2).download("yolov8")

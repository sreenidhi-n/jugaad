from ultralytics import YOLO

model = YOLO("E:/CID-internship/CID-ImageProcessing/Backend_models/jugaad/last.pt")

results = model("E:/CID-internship/CID-ImageProcessing/Backend_models/jugaad/crowd_cigarette.jpg")
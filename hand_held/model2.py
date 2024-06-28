from ultralytics import YOLO
from PIL import Image
import io


# Load your trained YOLO model
model = YOLO('E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/cigarette.pt') 
# model.eval()

def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return image

def predict(image):
    results = model(image)
    return results
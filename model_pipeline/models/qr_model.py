from ultralytics import YOLO
from PIL import Image
import io

class QR_BAR:
    __model_path = None
    __model = None
    def __init__(self, model_path):
        self.__model_path = model_path

    def load_model(self):
        
        self.__model = YOLO(self.__model_path) 
        return self.__model

from concurrent.futures import ThreadPoolExecutor
from header_files.predict_headers import *

class PredictionManager:
    __models = {}
    
    def __init__(self):
        self.__models = {}

    def __prediction(self, model, multimedia_path):
        model_name = model.get('model_name')
        model_instance = model.get('model')
        new_folder = f'E:/CID-internship/CID-ImageProcessing/Backend_models/jugaad/model_pipeline/{model_name}'

        if model_name == 'Cigarettes':
            print('cigs')
            predict_instance = Predict_Cigarettes()
            predict_instance.predict(model_instance, multimedia_path, new_folder)

        if model_name == 'Drugs':
            print('drugs')
            predict_instance = Predict_Drugs()
            predict_instance.predict(model_instance, multimedia_path, new_folder)

        if model_name == 'QR_BAR':
            print('qr')
            predict_instance = Predict_QR()
            predict_instance.predict(model_instance, multimedia_path, new_folder)

        if model_name == 'Hand_Held':
            predict_instance = Predict_Objects()
            predict_instance.predict(model_instance, multimedia_path, new_folder)
        if model_name == 'Nudity':
            print('Nudity')
            predict_instance = Predict_Nudity()
            predict_instance.predict(model_instance, multimedia_path, new_folder)

        else:
            print(f"No prediction class found for model name: {model_name}")

    def predict(self, models_loaded, multimedia_path):
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.__prediction, models_loaded.get(model_name), multimedia_path)
                for model_name in models_loaded
            ]
            for future in futures:
                future.result()
        return 'Predictions done'

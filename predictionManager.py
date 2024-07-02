from predict import Predictor
# from drug_model import Drug
from concurrent.futures import ThreadPoolExecutor


class PredictionManager:
    __models = {}
    def __init__(self):
        self.__models = {}

    def prediction(self, model, multimedia_path):
        if model.get('model_name') == 'Cigarettes':
            # model_loader = Cigarettes(model_path)
            # self.__models[model_name] = model_loader.load_model()
            predict_instance = Predictor()
            name = model.get('model_name')
            new_folder = f'Playground/{name}'
            predict_instance.yolo_predictor(model.get('model'), multimedia_path, new_folder)
        if model.get('model_name') == 'Drugs':
            # model_loader = Cigarettes(model_path)
            # self.__models[model_name] = model_loader.load_model()
            predict_instance = Predictor()
            name = model.get('model_name')
            new_folder = f'Playground/{name}'
            predict_instance.yolo_predictor(model.get('model'), multimedia_path, new_folder)

    def predict(self, models_loaded, multimedia_path):
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.prediction, models_loaded.get(model), multimedia_path)
                for model in models_loaded
            ]
        for future in futures:
            future.result()
        return 'Predictions done'
    

from cigarette_model import Cigarettes
from drug_model import Drugs


class ModelManager:
    __models = {}
    def __init__(self):
        self.__models = {}

    def activate_model(self, model_name, model_path, model_activate):
        if model_name == 'Cigarettes'and model_activate:
            model_loader = Cigarettes(model_path)
            loaded_model = model_loader.load_model()
            self.append_model_info(model_name, loaded_model)

        if model_name == 'Drugs'and model_activate:
            model_loader = Drugs(model_path)
            loaded_model= model_loader.load_model()
            self.append_model_info(model_name, loaded_model)


    def append_model_info(self, model_name, loaded_model):
        model_info = {
            "model_name": model_name,
            "model": loaded_model
        }

        self.__models[model_name] = model_info

    def activate_models(self, models):
        for model in models:
            model_name = model.get('model_name')
            model_path = model.get('model_path')
            model_activate = model.get('activate')
            if model_name and model_path:
                self.activate_model(model_name, model_path, model_activate)
        active_models = self.get_active_models()
        return active_models
    
    def get_active_models(self):
        return self.__models

'''
from concurrent.futures import ThreadPoolExecutor
from cigarette_model import Cigarettes
# from drug_model import Drug

class ModelManager:
    def __init__(self):
        self.__models = {}

    def activate_model(self, model_name, model_path):
        if model_name == 'Cigarettes':
            model_loader = Cigarettes(model_path)
            self.__models[model_name] = model_loader.load_model()
        # Add more conditions here for other models
        # elif model_name == 'Drug':
        #     model_loader = Drug(model_path)
        #     self.__models[model_name] = model_loader.load_model()

    def activate_models(self, models):
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.activate_model, model.get('model_name'), model.get('model_path'))
                for model in models if model.get('model_name') and model.get('model_path')
            ]
            # Ensure all futures have completed
            for future in futures:
                future.result()
        return self.get_active_models()

    def get_model(self, model_name):
        return self.__models.get(model_name)

    def get_active_models(self):
        return list(self.__models.keys())
'''

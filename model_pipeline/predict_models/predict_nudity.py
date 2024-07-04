import os
import shutil

class Predict_Nudity:
    
    __image = None
    def __init__(self):
        pass     
        
    def predict(self, model, multimedia_path, new_folder):
        from models.nudenet import NudeDetector
        if not os.path.exists(new_folder):
            os.makedirs(new_folder,exist_ok=True)

        nude_detector = NudeDetector()

        labels = [
            "BUTTOCKS_EXPOSED",
            "FEMALE_BREAST_EXPOSED",
            "FEMALE_GENITALIA_EXPOSED",
            "MALE_BREAST_EXPOSED",
            "ANUS_EXPOSED",
            "BELLY_EXPOSED",
            "MALE_GENITALIA_EXPOSED",
        ]

        if(os.path.exists(multimedia_path) and os.path.isdir(multimedia_path)):
            files = os.listdir(multimedia_path)
            for filename in files:
                image_path = os.path.join(multimedia_path,filename)
                output = nude_detector.detect(image_path)
                existing_folders = [name for name in os.listdir(new_folder) if os.path.isdir(os.path.join(new_folder, name))]

                i = 1
                nudity_detected = False
                for item in output:
                    
                    if item["class"] in labels and item["score"] > 0.5:
                        nudity_detected = True
                        print(output, filename)
                        while True:
                            folder_name = f'image_{i}'
                            if folder_name not in existing_folders:
                                image_folder = os.path.join(new_folder, folder_name)
                                os.makedirs(image_folder)
                                break
                            i += 1
                            
                        print("Nudity detected")
                        censored_image_path = os.path.join(image_folder, 'censored_image.jpg')  
                        nude_detector.censor(image_path, censored_image_path)
                        shutil.copy(image_path, image_folder)
                        break  

                if not nudity_detected:
                    print("No nudity detected.")



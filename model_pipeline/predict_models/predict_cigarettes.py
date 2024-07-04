import os
import shutil

class Predict_Cigarettes:
    __image = None
    def __init__(self):
        pass     
        
    def predict(self, model, multimedia_path, new_folder):
        # output = model(multimedia_path)
        if os.path.exists(multimedia_path) and os.path.isdir(multimedia_path):
            files = os.listdir(multimedia_path)
            for file_name in files:
            
                file_path = os.path.join(multimedia_path, file_name)
                output = model(file_path)
        
                for result in output:
                    for box in result.boxes:
                        if(len(box)>0):
                            os.makedirs(new_folder, exist_ok=True)
                            target_path = os.path.join(new_folder, file_name)
                            shutil.copy(file_path, target_path)


# import os
# import shutil
# import torch

# class Predict_Cigarettes:
#     def __init__(self):
#         pass
        
#     def predict(self, model, multimedia_path, new_folder):
#         if os.path.exists(multimedia_path) and os.path.isdir(multimedia_path):
#             files = os.listdir(multimedia_path)
#             for file_name in files:
#                 file_path = os.path.join(multimedia_path, file_name)
                
#                 # Ensure model is in CUDA mode if applicable
#                 if torch.cuda.is_available():
#                     device = torch.device("cuda")
#                     model.to(device)
#                     # file_path_cuda = file_path.cuda()  # Adjust as per your model's input requirements
#                 else:
#                     file_path_cuda = file_path
                
#                 try:
#                     output = model(file_path_cuda)
                    
#                     for result in output:
#                         for box in result.boxes:
#                             if len(box) > 0:
#                                 os.makedirs(new_folder, exist_ok=True)
#                                 target_path = os.path.join(new_folder, file_name)
#                                 shutil.copy(file_path, target_path)
                
#                 except Exception as e:
#                     print(f"Error processing {file_path}: {str(e)}")

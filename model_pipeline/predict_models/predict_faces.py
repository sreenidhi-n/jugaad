# from FaceRecognition import FaceRecognition
# import cv2
# import os
# import time


# class RunFace:
#     def __init__(self):
#         self.face_recognition = FaceRecognition()

#     def runface(self, dir_path):
#         start_time = time.time()
#         input_folder = os.path.join(dir_path, "Input")
        
#         for filename in os.listdir(input_folder):
#             if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
#                 image_path = os.path.join(input_folder, filename)
#                 image = cv2.imread(image_path)
#                 image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                
#                 bboxes = self.face_recognition.detect_faces(image)
#                 if bboxes:
#                     self.face_recognition.save_faces(image, bboxes, image_path, dir_path)

#         end_time = time.time()
#         total_time = end_time - start_time
#         print(f"Total time taken: {total_time} seconds")

# # Create an instance of RunFace and run the face detection
# instance = RunFace()
# instance.runface("D:/PES_Classes/CIDInternship_2024/ImageProcessing/Face_Detection")

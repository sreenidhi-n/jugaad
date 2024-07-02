from FaceRecognition import detect_faces, save_faces
import cv2
import os
import time


class RunFace:
    def __init__(self):
        pass

    def runface(input_folder):
        start_time = time.time()
        #input_folder = "D:\\PES_Classes\\CIDInternship_2024\\ImageProcessing\\Face_Detection"
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                image_path = os.path.join(input_folder, filename)
                image = cv2.imread(image_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                
                bboxes = detect_faces(image)
                if bboxes:
                    save_faces(image, bboxes, image_path)

        end_time = time.time()
        total_time = end_time - start_time
        print(f"Total time taken: {total_time} seconds")
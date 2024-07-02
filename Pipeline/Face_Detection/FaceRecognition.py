import cv2
import os
import random
import time
from mtcnn.mtcnn import MTCNN
import face_recognition


class FaceRecognition:
    
    def __init__(self):
        pass

    def __check_match(self, face_1_encoding, face_2_encoding):
        return face_recognition.compare_faces([face_1_encoding], face_2_encoding)[0]

    def detect_faces(self,image):
        detector = MTCNN()
        return detector.detect_faces(image)

    def __get_random_image(self,folder):
        entries = os.listdir(folder)
        image_files = [entry for entry in entries if os.path.isfile(os.path.join(folder, entry)) and entry.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
        if not image_files:
            raise FileNotFoundError("No image files found in the specified folder.")
        return os.path.join(folder, random.choice(image_files))

    def __subfolders(self,save_dir):
        return [entry for entry in os.listdir(save_dir) if os.path.isdir(os.path.join(save_dir, entry))]

    def save_faces(self,image, bboxes, image_path):
        faces_dir = r"D:\\PES_Classes\\CIDInternship_2024\\ImageProcessing\\Face_Detection\\Faces"
        save_dir = r"D:\\PES_Classes\\CIDInternship_2024\\ImageProcessing\\Face_Detection\\Output2"
        
        if not os.path.exists(faces_dir):
            os.makedirs(faces_dir)
        
        existing_subfolders = self.__subfolders(save_dir)
        
        for i, box in enumerate(bboxes):
            if len(bboxes) > 1:
                x1, y1, w, h = box['box']
                face = image[y1:y1 + h, x1:x1 + w]
                face_path = os.path.join(faces_dir, f"face_{i + 1}.jpg")
                rem = face_path
                cv2.imwrite(face_path, cv2.cvtColor(face, cv2.COLOR_RGB2BGR))
                face1 = face_recognition.load_image_file(face_path)
                face1 = face_recognition.face_encodings(face1)[0]
            else:
                face_path = os.path.join(faces_dir, "image.jpg")
                cv2.imwrite(face_path, image)
                face1 = face_recognition.load_image_file(face_path)
                face1 = face_recognition.face_encodings(face1)[0]
                rem = face_path
                face = image  
            
            saved = False

            for sub in existing_subfolders:
                try:
                    random_image_path = self.__get_random_image(os.path.join(save_dir, os.path.join(sub, "Face")))
                    tempimg = face_recognition.load_image_file(random_image_path)
                    tempimg = face_recognition.face_encodings(tempimg)[0]
                    if self.__check_match(face1, tempimg):
                        img_path = os.path.join(save_dir, os.path.join(sub, "Image"))
                        if not os.path.exists(img_path):
                            os.makedirs(img_path)
                        face_dir = os.path.join(save_dir, sub, "Face")
                        if not os.path.exists(face_dir):
                            os.makedirs(face_dir)
                        i = int(sorted([int(file.split('_')[1].split('.')[0]) for file in os.listdir(face_dir) if file.endswith('.jpg')])[-1])
                        face_save_path = os.path.join(face_dir, f"face_{i + 1}.jpg")
                        cv2.imwrite(face_save_path, cv2.cvtColor(face, cv2.COLOR_RGB2BGR))
                        i = int(sorted([int(file.split('_')[1].split('.')[0]) for file in os.listdir(img_path) if file.endswith('.jpg')])[-1])
                        newimg_path = os.path.join(img_path, f"img_{i + 1}.jpg")
                        cv2.imwrite(newimg_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
                        print(f"Saved: face_{i + 1}.jpg in {face_save_path}")
                        saved = True
                        break
                except Exception as e:
                    print(f"Error processing subfolder {sub}: {e}")

            if not saved:
                num = len(existing_subfolders) + 1
                new_folder = os.path.join(save_dir, f"Face_{num}")
                while os.path.exists(new_folder):
                    num += 1
                    new_folder = os.path.join(save_dir, f"Face_{num}")
                os.makedirs(new_folder)
                face_dir = os.path.join(new_folder, "Face")
                if not os.path.exists(face_dir):
                    os.makedirs(face_dir)
                face_save_path = os.path.join(face_dir, f"face_{i + 1}.jpg")
                cv2.imwrite(face_save_path, cv2.cvtColor(face, cv2.COLOR_RGB2BGR))
                img_path = os.path.join(new_folder, "Image")
                if not os.path.exists(img_path):
                    os.makedirs(img_path)
                newimg_path = os.path.join(img_path, f"img_{i + 1}.jpg")
                cv2.imwrite(newimg_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
                print(f"Saved: face_{i + 1}.jpg in {newimg_path}")

            os.remove(rem)

'''input_folder = "D:\\PES_Classes\\CIDInternship_2024\\ImageProcessing\\Face_Detection"
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
print(f"Total time taken: {total_time} seconds")'''
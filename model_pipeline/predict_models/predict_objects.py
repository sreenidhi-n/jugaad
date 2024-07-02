import os
import shutil
import cv2
import numpy as np
import mediapipe as mp

class Predict_Objects:
    __image = None
    __desired_classes = ['backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 
    'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 
    'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 
    'fork', 'knife', 'spoon', 'bowl', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 
    'toaster', 'sink', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 
    'toothbrush']

    def __init__(self):
        pass     
    
    def __points_prediction(self, hands, mp_hands ,image):
        sample_img = np.array(image)
        sample_img = cv2.cvtColor(sample_img, cv2.COLOR_RGB2BGR)

        results = hands.process(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))
        
        image_height, image_width, _ = sample_img.shape

        hands_data = []

        if results.multi_hand_landmarks:

            for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
                hand_data={
                    'hand_number':{hand_no+1},
                    'landmarks':{}
                }

                landmark_names = {
                                0: 'wrist',
                                4: 'thumb_tip',
                                8: 'index_finger_tip',
                                12: 'middle_finger_tip',
                                16: 'ring_finger_tip',
                                20: 'pinky_tip'
                            }

                
                for i in [0, 4, 8, 12, 16, 20]:
                    landmark_name = landmark_names[i]
                    x = hand_landmarks.landmark[mp_hands.HandLandmark(i).value].x * image_width
                    y = hand_landmarks.landmark[mp_hands.HandLandmark(i).value].y * image_height

                    hand_data['landmarks'][landmark_name] = {'x': x, 'y': y}

                hands_data.append(hand_data)
        # print(hands_data)
        return hands_data

    def __is_point_in_bbox(self, point, bbox):
        x, y = point
        x1, y1, x2, y2 = bbox
        return x1 <= x <= x2 and y1 <= y <= y2

    def __get_objects_boxes(self, box):
        x1, y1, x2, y2 = map(int, box.xyxy.cpu().numpy()[0])
        bbox = (x1, y1, x2, y2)
        return bbox
    
    def __get_hand_points(self, hands):
        # return list
        hand_points=[]
    
        for hand in hands:
            for i in ['wrist','thumb_tip','index_finger_tip', 'middle_finger_tip','ring_finger_tip','pinky_tip']:
                x = hand['landmarks'][i]['x']
                y = hand['landmarks'][i]['y']
                hand_points.append((x,y))
        return hand_points
    
    def __check_overlap(self, hand_points, object):
        for point in hand_points:
            if self.__is_point_in_bbox(point, object):
                print(f"Point {point} is inside the bounding box {object}")
                return True
        return False

    def __get_hands(self, image):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=True, max_num_hands=10, min_detection_confidence=0.3)
        hands_data = self.__points_prediction(hands, mp_hands, image)
        return hands_data

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
                            object = self.__get_objects_boxes(box)
                            hands = self.__get_hands(cv2.imread(file_path))
                            hand_points = self.__get_hand_points(hands)
                            print('---------------------------------------------------------')
                            print(hand_points)
                            print(object)
                            print('---------------------------------------------------------')
                            is_hand_held = self.__check_overlap(hand_points, object)
                            if is_hand_held:
                                os.makedirs(new_folder, exist_ok=True)
                                target_path = os.path.join(new_folder, file_name)
                                shutil.copy(file_path, target_path)
                            continue




# from ultralytics import YOLO
# from PIL import Image
# import io


# # Load your trained YOLO model
# model = YOLO('E:/CID-internship/CID-ImageProcessing/Backend_models/jugaad/last.pt') 
# # model.eval()

# def transform_image(image_bytes):
#     image = Image.open(io.BytesIO(image_bytes))
#     return image

# def predict(image):
#     results = model(image)
#     return results



import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from PIL import Image
import io
import json

def transform_image1(image_bytes):
    print('came to ti1')
    image = Image.open(io.BytesIO(image_bytes))
    return image

def predict1(image):
    #  First step is to initialize the Hands class an store it in a variable
    mp_hands = mp.solutions.hands
    # Now second step is to set the hands function which will hold the landmarks points
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=10, min_detection_confidence=0.3)

    # Last step is to set up the drawing function of hands landmarks on the image
    mp_drawing = mp.solutions.drawing_utils


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

            # print(f'HAND NUMBER: {hand_no+1}')
            # print('-----------------------')

            # for i in [0,4,8,12,16,20]:

            #     print(f'{mp_hands.HandLandmark(i).name}:')
            #     print(f'x: {hand_landmarks.landmark[mp_hands.HandLandmark(i).value].x * image_width}')
            #     print(f'y: {hand_landmarks.landmark[mp_hands.HandLandmark(i).value].y * image_height}')
            for i in [0, 4, 8, 12, 16, 20]:
                landmark_name = landmark_names[i]
                x = hand_landmarks.landmark[mp_hands.HandLandmark(i).value].x * image_width
                y = hand_landmarks.landmark[mp_hands.HandLandmark(i).value].y * image_height

                hand_data['landmarks'][landmark_name] = {'x': x, 'y': y}

            hands_data.append(hand_data)
    # print(hands_data)
    return hands_data


# image_path = 'E:/CID-internship/CID-ImageProcessing/Backend_models/jugaad/hands.jpg'
# hands_json = predict(image_path)
# for hand in hands_json:
#     hand_number = hand['hand_number']
#     print(hand_number)
#     landmarks=hand['landmarks']['wrist']['x']
#     print(landmarks)

# print(hands_json)
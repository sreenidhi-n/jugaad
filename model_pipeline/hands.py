import mediapipe as mp
import numpy as np
import cv2

class Hands:
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


    def get_hands(self, image):
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(static_image_mode=True, max_num_hands=10, min_detection_confidence=0.3)
        hands_data = self.__points_prediction(hands, mp_hands, image)
        return hands_data

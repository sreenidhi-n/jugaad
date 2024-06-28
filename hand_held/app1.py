from flask import Flask, request, jsonify
from predict import get_prediction1, get_prediction2

app = Flask(__name__)

# @app.route('/predict1', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     if file:
#         img_bytes = file.read()
#         prediction = get_prediction1(img_bytes)
#         # return jsonify({'prediction': prediction})
#         print(prediction)
#         return ''    
#     return jsonify({'error': 'Error during prediction'}), 500


# @app.route('/predict2', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
    
#     file = request.files['file']
    
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     if file:
#         img_bytes = file.read()
#         prediction = get_prediction2(img_bytes)
#         # return jsonify({'prediction': prediction})
#         print(prediction)
#         return ''    
#     return jsonify({'error': 'Error during prediction'}), 500


@app.route('/compare', methods=['POST'])
def predict_compare():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        img_bytes = file.read()
        predictions1 = get_prediction1(img_bytes)
        predictions2 = get_prediction2(img_bytes)

    def is_point_in_bbox(point, bbox):
        x, y = point
        x1, y1, x2, y2 = bbox
        return x1 <= x <= x2 and y1 <= y <= y2
            
    hand_points=[]
    
    for hand in predictions1:
        for i in ['wrist','thumb_tip','index_finger_tip', 'middle_finger_tip','ring_finger_tip','pinky_tip']:
            x = hand['landmarks'][i]['x']
            y = hand['landmarks'][i]['y']
            hand_points.append((x,y))
    # print(predictions1)
    

    # hand_points = [
    #     (100, 200),  # Wrist
    #     (150, 250),  # Thumb tip
    #     (200, 250),  # Index finger tip
    #     (250, 250),  # Middle finger tip
    #     (300, 250),  # Ring finger tip
    #     (350, 250)   # Pinky tip
    # ]
    print(hand_points)
    for result in predictions2:
        for box in result.boxes:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy.numpy()[0])
            bbox = (x1, y1, x2, y2)
            
            # Check if any hand points are within the bounding box
            hand_held = False
            for point in hand_points:
                if is_point_in_bbox(point, bbox):
                    print(f"Point {point} is inside the bounding box {bbox}")
                    hand_held = True
                    print(point)
                    break  # Stop checking further points if one is found inside
            
            if hand_held:
                print(f"The object at {bbox} is considered hand-held.")
                return ''
            
            return 'bruh'
        # return jsonify({
        #     'model1_predictions': predictions1,
        #     'model2_predictions': predictions2,
        #     'comparison': comparison
        # })
    return jsonify({'error': 'Error during prediction'}), 500

if __name__ == '__main__':
    app.run(port=6888,debug=True)

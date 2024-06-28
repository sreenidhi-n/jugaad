# import cv2
# from ultralytics import YOLO

# # Load the model
# model = YOLO("D:/PES_Classes/CIDInternship_2024/ImageProcessing/Tattoo/runs/runs/detect/train2/weights/best.pt")

# # Run the model on the image
# results = model("D:/PES_Classes/CIDInternship_2024/ImageProcessing/Tattoo/Copy20Untitled20(1).jpg")

# # Load the image using OpenCV
# image = cv2.imread("D:/PES_Classes/CIDInternship_2024/ImageProcessing/Tattoo/Copy20Untitled20(1).jpg")

# # Loop through the results and draw bounding boxes
# for result in results:
#     for box in result.boxes:
#         # Get bounding box coordinates
#         x1, y1, x2, y2 = map(int, box.xyxy.numpy()[0])
#         # Draw the bounding box on the image
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         # Optionally, you can put the confidence score as well
#         label = f"{box.conf.numpy()[0]:.2f}"
#         cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# # Display the image with bounding boxes
# cv2.imshow("Image with Bounding Boxes", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


from ultralytics import YOLO

# Load the model
model = YOLO("E:\CID-internship\CID-ImageProcessing\Backend_models\models_checkpoints\cigarette.pt")

# Run the model on the image
results = model("E:\CID-internship\CID-ImageProcessing\Backend_models\jugaad\crowd_cigarette.jpg")

# Sample coordinates of hand points (wrist, thumb tip, index finger tip, middle finger tip, ring finger tip, pinky tip)
hand_points = [
    (100, 200),  # Wrist
    (150, 250),  # Thumb tip
    (200, 250),  # Index finger tip
    (250, 250),  # Middle finger tip
    (300, 250),  # Ring finger tip
    (350, 250)   # Pinky tip
]

# Function to check if a point is inside a bounding box
def is_point_in_bbox(point, bbox):
    x, y = point
    x1, y1, x2, y2 = bbox
    return x1 <= x <= x2 and y1 <= y <= y2

# Loop through the results to check for hand-held objects
for result in results:
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
                break  # Stop checking further points if one is found inside
        
        if hand_held:
            print(f"The object at {bbox} is considered hand-held.")

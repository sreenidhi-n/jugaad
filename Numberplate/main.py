import cv2
import numpy as np
import easyocr
import os
import imutils

# Function to preprocess and extract number plate
def extract_number_plate(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise using bilateral filter
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)

    # Edge detection using Canny
    edged = cv2.Canny(bfilter, 30, 200)

    # Find contours and sort by area, keep top 10
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # Initialize location variable for the contour
    location = None

    # Iterate over contours to find the best approximate contour of 4 sides (typically for rectangles)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break

    # If contour is found, extract and save number plate
    if location is not None:
        # Extract bounding rectangle coordinates
        (x, y, w, h) = cv2.boundingRect(location)

        # Crop the number plate region
        cropped_image = gray[y:y + h, x:x + w]

        # Perform OCR on the cropped image
        reader = easyocr.Reader(['en'], verbose=False)  # Suppress verbose output
        result = reader.readtext(cropped_image)

        # Check if text is detected
        if result:
            text = result[0][-2]

            # Remove spaces from the detected text
            filename = text.replace(" ", "")

            # Create output folder if it doesn't exist
            output_folder = "Output"
            os.makedirs(output_folder, exist_ok=True)

            # Save the cropped image with the filename as the detected text
            output_path = os.path.join(output_folder, f"{filename}.jpg")
            cv2.imwrite(output_path, cropped_image)

            print(f"Number plate saved as: {output_path}")

            return True

    print("Number plate not detected or could not be saved.")
    return False

# Example usage:
image_path = "103545035-01c3ce00-4ec7-11eb-9ec4-0f31e3bcf608.png"
extract_number_plate(image_path)

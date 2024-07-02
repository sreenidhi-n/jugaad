import streamlit as st
import os
import random
from PIL import Image

def display_images(output_folder_path):
    subfolders = [f.path for f in os.scandir(output_folder_path) if f.is_dir()]
    
    for i, subfolder in enumerate(subfolders):
        face_folder = os.path.join(subfolder, "Face")
        image_folder = os.path.join(subfolder, "Image")
        
        if not os.path.exists(face_folder) or not os.path.exists(image_folder):
            continue

        face_images = [os.path.join(face_folder, f) for f in os.listdir(face_folder) if os.path.isfile(os.path.join(face_folder, f))]
        image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

        if face_images:
            random_face_image = random.choice(face_images)
            st.header(f"Face_{i+1}")
            face_image = Image.open(random_face_image)
            face_image = face_image.resize((100, 100))  # Adjusted size
            st.image(face_image, caption=f"Random Image from {face_folder}", use_column_width=False)
        
        if image_files:
            st.write(f"Images from {image_folder}:")
            cols = st.columns(len(image_files))  # Create columns for each image
            for idx, image_file in enumerate(image_files):
                with cols[idx]:
                    img = Image.open(image_file)
                    img = img.resize((100, 100))  # Adjusted size
                    st.image(img, use_column_width=False)

output_folder_path = r'D:/PES_Classes/CIDInternship_2024/ImageProcessing/Face_Detection/Output2'
if os.path.exists(output_folder_path):
    display_images(output_folder_path)
else:
    st.error("The provided path does not exist. Please enter a valid path.")
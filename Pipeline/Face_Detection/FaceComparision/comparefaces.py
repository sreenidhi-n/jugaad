"""
This file takes input of 2 image paths and gives an output whether both images are similar or not
"""
from deepface import DeepFace

def verify_faces(img1_path, img2_path):
    """
    This function takes the paths of two images and performs face verification using DeepFace.
    
    Parameters:
    img1_path (str): The path to the first image.
    img2_path (str): The path to the second image.
    
    Returns:
    dict: The result of the verification including whether the faces match and the distance between them.
    """
    result = DeepFace.verify(img1_path, img2_path)
    return result


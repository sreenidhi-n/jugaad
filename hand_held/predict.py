from model import transform_image1, predict1
from model2 import transform_image, predict

def get_prediction1(image_bytes):
    # print(image_bytes)
    image = transform_image1(image_bytes)
    results = predict1(image)
    print(results)
    return results

def get_prediction2(image_bytes):
    image = transform_image(image_bytes)
    results = predict(image)
    return results

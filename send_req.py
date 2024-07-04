import requests
import json

def send_image():
    data = [{'model_name' : "Cigarettes",
             'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/cigarette.pt',
             'activate' : True},
             {'model_name' : "Drugs",
             'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/drugs.pt',
             'activate' : True},
             {'model_name' : "Nudity",
             'model_path' : '',
             'activate' : True},
             {'model_name' : "QR_BAR",
             'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/bar_qr.pt',
             'activate' : True},
             {'model_name' : "Hand_Held",
             'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/yolov8l.pt',
             'activate' : True},
             ]
    # categories = {
    # "Flags": False,
    # "Food": False,
    # "Jewelry": False,
    # "Maps": False,
    # "Credit cards": False,
    # "Money": False,
    # "Faces": False,
    # "Gatherings": False,
    # "Hand hold object": True,
    # "Nudity": True,
    # "Tattoos": False,
    # "Beach": False,
    # "Hotel rooms": False,
    # "Pool": False,
    # "Restaurant": False,
    # "Cigarettes": True,
    # "Drugs": False,
    # "Camera": False,
    # "Smartphones": False,
    # "Barcodes and QR codes": True,
    # "Documents": False,
    # "Handwriting": False,
    # "Invoices": False,
    # "Photo IDs": False,
    # "Screenshots": False,
    # "Cars": False,
    # "License plates": False,
    # "Motorcycles": False,
    # "Vehicle dashboards": False,
    # "Fire and Explosion": False,
    # "Weapons": False
    # }

    # model_paths = {
    # "Cigarettes": 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/cigarette.pt',
    # "Drugs": 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/drugs.pt',
    # "Barcodes and QR codes": 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/bar_qr.pt'
    # }
    
    # data = [{'model_name': name, 'model_path': model_paths.get(name, ''), 'activate': True} 
    #     for name in categories]
    

    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:8007/activate'
    # files = {'file': open(image_path, 'rb')}
    response = requests.post(url,headers=headers,data=json.dumps(data))
    # print(data)

if __name__ == "__main__":
    
    prediction = send_image()
    # print(prediction)

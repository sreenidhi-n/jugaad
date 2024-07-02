import requests
import json

def send_image():
    # data = [{'model_name' : "Cigarettes",
    #          'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/cigarette.pt',
    #          'activate' : True},
    #          {'model_name' : "Drugs",
    #          'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/drugs.pt',
    #          'activate' : True},
    #          {'model_name' : "QR_BAR",
    #          'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/bar_qr.pt',
    #          'activate' : True},
    #          ]
    data = [
             {'model_name' : "Hand_Held",
             'model_path' : 'E:/CID-internship/CID-ImageProcessing/Backend_models/models_checkpoints/yolov8l.pt',
             'activate' : True}
             ]

    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:8003/activate'
    # files = {'file': open(image_path, 'rb')}
    response = requests.post(url,headers=headers,data=json.dumps(data))
    print(response)

if __name__ == "__main__":
    
    prediction = send_image()
    # print(prediction)

import requests
import json

def send_image():
    url = 'http://127.0.0.1:8007/predict'
    headers = {'Content-type': 'application/json'}
    data = [{'multi_path': 'E:/CID-internship/CID-ImageProcessing/Backend_models/jugaad/Images'}]
    response = requests.post(url,headers=headers,data=json.dumps(data))
    print(response)

if __name__ == "__main__":
    prediction = send_image()
    # print(prediction)

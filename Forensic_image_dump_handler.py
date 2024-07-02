from predictionManager import PredictionManager
from modelManager import ModelManager
from flask import *
from collections import defaultdict
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import time
import BinProcessor
import E01Processor
import requests
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

model_manager = ModelManager()
predict_manager = PredictionManager()
models_loaded = {}


def func():
    with open("image.txt","rt") as f:
        return f.read()
    



@app.route("/", methods=["GET", "POST"])
def receive_dump():
    if request.method == "POST":
        data = request.get_json()
        # print(data)
        # [{name,content,extension}]

        # print("data = ", data)
        if len(data):
            array = data["result"]  # type is a list
            # print("length of data = ", type(array))
            analyzer = None
            extension = array[0]["extension"]
            # print(array[0],type(array[0]))
            if extension == "E01":
                analyzer = E01Processor.E01Processor(array)
            else:
                # Add more extensions here
                analyzer = BinProcessor.BinProcessor(array)
            print("suksuks")
            analyzer.setupDump()
            analyzer.startAnalysis()

            # analyzer.cleanUp()
            print("processing ....")
            # time.sleep(3)



            processed_files = [
                {"folder_name": "folder1",
                 "number_of_files": 50,
                 "File_array": [
                     {
                         "file_name": "file_name_1",
                         "file_content": func()
                     }
                 ]},

            ]
        socketio.emit('file_processed', {
                      'message': 'File has been processed successfully!', 'files': processed_files})
        return jsonify({'status': 'File processed'}), 200
    return "not Handled request", 400


@app.route("/what_all_models_to_activate",methods=["POST"])
def pipeline():
    get_data = request.get_json()
    print(get_data)
    headers = {'Content-type': 'application/json'}
    url = 'http://127.0.0.1:5000/activate'
    data = []
    for i in get_data.keys():
        if get_data.get(i) == "True":
            d = defaultdict(str)
            d["model_name"] = i
            d["model_path"] = "models/cigarette.pt"
            d["activate"] = True
            data.append(d)
            
    # this is to activate 
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    url = "http://127.0.0.1:5000/predict"
    data = [
        {'multi_path': 'Images'}]
    response = requests.post(url, headers=headers, data=json.dumps(data))

    return "somthing",200


@app.route('/activate', methods=['POST'])
def activate_model():
    data = request.json
    global models_loaded

    if not data or not isinstance(data, list):
        return jsonify({'error': 'Invalid request data'}), 400

    models_loaded = model_manager.activate_models(data)
    for model in models_loaded:

        print(models_loaded.get(model))

    return jsonify({"message": "Models activated successfully!"})


@app.route('/predict', methods=['POST'])
def prediction():
    path = request.json
    multimedia_path = path[0].get('multi_path')
    predict_manager.predict(models_loaded, multimedia_path)

    return "predicted",200



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

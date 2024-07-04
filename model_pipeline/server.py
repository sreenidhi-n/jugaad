from flask import Flask, request, jsonify
from modelManager import ModelManager
from predictionManager import PredictionManager

app = Flask(__name__)
model_manager = ModelManager()
predict_manager = PredictionManager()
models_loaded = {}

@app.route('/activate',methods=['POST'])
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

    return 'something'

if __name__ == '__main__':
    app.run(port=8007,debug=True)

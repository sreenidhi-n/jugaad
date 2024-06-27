from flask import *
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import time
import BinProcessor
import E01Processor
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

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
            # analyzer.setupDump()
            # analyzer.startAnalysis()
            # analyzer.cleanUp()
            print("processing ....")
            time.sleep(3)
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

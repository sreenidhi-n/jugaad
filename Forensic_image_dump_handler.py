from flask import *
from flask_cors import CORS
import BinProcessor
import E01Processor
app = Flask(__name__)
CORS(app)

@app.route("/" ,methods=["GET","POST"])
def receive_dump():
    if request.method == "POST" :
        data = request.get_json()
        # print(data)
        #[{name,content,extension}]
        
        # print("data = ", data)
        if len(data):
            array = data["result"] # type is a list
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
        
        return "Successful",200
    return "not Handled request", 400



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

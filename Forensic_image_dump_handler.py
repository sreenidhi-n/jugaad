from flask import *
import E01Processor
import BinProcessor
app = Flask(__name__)


@app.route("/" ,methods=["GET","POST"])
def receive_dump():
    if request.method == "POST":
        data = request.get_json()
        analyzer = None
        extension = data["extension"]
        if extension == "E01":
            analyzer = E01Processor(data["data"])
        else:
            # Add more extensions here
            analyzer = BinProcessor(data["data"])
        analyzer.setupDump()
        analyzer.startAnalysis()
        analyzer.cleanUp()
        
        return "Successful",200
    return "not Handled request", 400



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

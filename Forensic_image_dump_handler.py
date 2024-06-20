from flask import *

app = Flask(__name__)


@app.route("/" ,methods=["GET","POST"])
def recieve_dump():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        return "Successful",200
    return "not Handled request", 400



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

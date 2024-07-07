from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# # MongoDB connection settings
MONGO_URI = 'mongodb://localhost:27017'
client = AsyncIOMotorClient(MONGO_URI)
db = client["image_urls"]
collection = db["urls"]

@app.route('/')
def index():
    return "getting re baba"

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on("Ready")
def fetch_and_emit_images():
    asyncio.run(trasnmitdata())

async def trasnmitdata():
    async for doc in collection.find():
        url = doc.get("url")
        socketio.emit("image_name",{"url":url})
        # print(url)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
# async def fetch():
#     async for doc in collection.find():
#         print(doc.get("url"))
# asyncio.run(fetch())

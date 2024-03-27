# backend/app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongo:27017/")
db = client["mydatabase"]

# Define route to handle root URL
@app.route('/')
def index():
    return 'Hello, this is the backend server!'

# Define route to handle favicon request
@app.route('/favicon.ico')
def favicon():
    return ''

# Define route to handle storing data
@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    db.my_collection.insert_one(data)
    return jsonify({"message": "Data stored successfully in the database"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

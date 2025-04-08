from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
  return 'Welcome to the Flask Backend!'

@app.route('/api/data', methods=['GET'])
def get_data():
  data = {
    "message": "Hello from Flask Backend!",
    "status": "success"
  }
  return jsonify(data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

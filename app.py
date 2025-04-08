from flask import Flask, jsonify, request

app = Flask(__name__)

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
  app.run(debug=True)

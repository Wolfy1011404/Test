from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import random

app = Flask(__name__)

CORS(app)

@app.route('/maze')
def maze():
  size = 10
  grid = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]
  grid[0][0] = grid[size-1][size-1] = 0
  return jsonify({"grid": grid})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

from flask import Flask
from flask import request
from flask import jsonify

import json
from areas import findNearby

app = Flask(__name__)

@app.route('/areas', methods=['POST'])
def areas():
    input_json = request.get_json(force=True)
    result = findNearby(input_json)
    return jsonify(result)

@app.route('/cached', methods=['POST'])
def cached():
    with open('./cache/heatmaps.json') as f:
      return jsonify(json.load(f))

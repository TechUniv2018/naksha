from flask import Flask
from flask import request
from flask import jsonify

from flask_cors import CORS

import json
from areas import findNearby
from advertisements import addAds

app = Flask(__name__)
CORS(app)

@app.route('/areas', methods=['POST'])
def areas():
    input_json = request.get_json(force=True)
    result = findNearby(input_json)
    result = addAds(result)
    return jsonify(result)

@app.route('/cached', methods=['POST'])
def cached():
    with open('./cache/heatmaps.json') as f:
      return jsonify(json.load(f))

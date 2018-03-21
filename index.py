from flask import Flask
from flask import request
from flask import jsonify
from flask import send_from_directory
from flask import redirect

from flask_cors import CORS

import json
from areas import findNearby
from advertisements import addAds

app = Flask(__name__)
CORS(app)

@app.route('/')
def base():
    return redirect("/index.html", code=302)

@app.route('/<path:path>')
def send_files(path):
    return send_from_directory('./public', path)

@app.route('/areas', methods=['POST'])
def areas():
    input_json = request.get_json(force=True)
    result = findNearby(input_json)
    result = addAds(result)
    return jsonify(result)

@app.route('/cached', methods=['POST'])
def cached():
    with open('./cache/response.json') as f:
      return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

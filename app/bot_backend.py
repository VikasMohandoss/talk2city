import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/respond', methods=["POST"])
def respond():
    return jsonify({})



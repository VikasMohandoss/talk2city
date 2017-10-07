import json

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/respond', methods=["POST"])
def respond():
    return jsonify({})




@app.route('/process_messages', methods=["POST"])
def respond():
    return jsonify({})
"User %s says: %s" % (msg.sender.screen_name, msg.text)


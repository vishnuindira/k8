#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/name')
def index():
    return jsonify({'name': 'vishnu',
                    'email': 'vishnu@outlook.com'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
app.run()



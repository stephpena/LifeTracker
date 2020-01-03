from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import json
import sys
import requests
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/main', methods=['POST'])
def test():
    return render_template('main.html')

@app.route('/test', methods=['POST','GET'])
def answers():
    # user_data = request.json
    # a, b, c = user_data['a'], user_data['b'], user_data['c']
    # root_1, root_2 = _solve_quadratic(a, b, c)
    test_1 = 25
    test_2 = 15
    return jsonify({'test_1': test_1, 'test_2': test_2})


if __name__ == '__main__':
    port = 5000
    app.run(port=port, threaded=True, debug=False)

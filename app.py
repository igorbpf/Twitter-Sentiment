from flask import Flask, jsonify
import numpy as np
from twitter_sent import twitter

app = Flask(__name__)


@app.route('/')
def index():
    return "Digite ao lado do endereco sua busca"


@app.route('/<string:query>')
def queries(query):
    response = twitter(query)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
import numpy as np
from twitter_sent import twitter
from rq import Queue
from worker import conn
import time

q = Queue(connection=conn)

app = Flask(__name__)


@app.route('/')
def index():
    return "Digite ao lado do endereco sua busca"


@app.route('/<string:query>')
def queries(query):
    #response = twitter(query)
    job = q.enqueue(twitter, query)
    time.sleep(25)
    print job.result
    return jsonify(response=job.result)

if __name__ == '__main__':
    app.run(debug=True)

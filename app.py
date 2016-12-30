from flask import Flask, jsonify
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC


app = Flask(__name__)


@app.route('/')
def index():
    iris = load.iris()
    X, y = iris.data, iris.target
    svm = SVC(kernel='linear')
    svm.fit(X)
    y_pred = svm.predict(X)

    return jsonify(target=y_pred)

if __name__ == '__main__':
    app.run(debug=True)
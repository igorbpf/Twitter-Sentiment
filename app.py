from flask import Flask, jsonify
import numpy as np
#from sklearn.datasets import load_iris
from sklearn.svm import SVC


app = Flask(__name__)


@app.route('/')
def index():
    #y_pred = svm.predict(X)
    return "Love"
    #return str(y_pred.tolist())#jsonify(target=y_pred.tolist())

if __name__ == '__main__':
    ##iris = load_iris()
    #X, y = iris.data, iris.target
    #svm = SVC(kernel='linear')
    #svm.fit(X,y)

    app.run(debug=True)
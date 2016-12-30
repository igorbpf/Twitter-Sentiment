from flask import Flask
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    x = np.array([[1., 2.], [3., 2.]])
    y = np.array([[3., 2.], [1., 1.]])
    return str(x * y)

if __name__ == '__main__':
    app.run(debug=True)
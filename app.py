from flask import Flask, jsonify, url_for, request, render_template
from twitter_sent import twitter

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    data = []
    result = False
    error = False
    if request.method == 'POST':
        url = request.form['url']
        reviews, _, data = twitter(url)
        if data == [] and reviews == []:
            error = True
            return render_template('index.html', results=result, cont=data, error=error)
        result = True
        return render_template('index.html', results=result, cont=data, error=error)
    else:
        return render_template('index.html', results=result, cont=data, error=error)


@app.route('/api/<string:query>')
def queries(query):
    response, overall_sentiment, _ = twitter(query)
    keys = response[0].keys()
    return jsonify(sentimento_global=overall_sentiment, response=response)

if __name__ == '__main__':
    app.run(debug=False)

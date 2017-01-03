from flask import Flask, jsonify, url_for, request, render_template
from twitter_sent import twitter

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    data = []
    result = False
    if request.method == 'POST':
        url = request.form['url']
        _, _, data = twitter(url)
        result = True
        print data
        print result
        return render_template('index.html', results=result, cont=data)
    else:
        return render_template('index.html', results=result, cont=data)


@app.route('/api/<string:query>')
def queries(query):
    response, overall_sentiment, _ = twitter(query)
    keys = response[0].keys()
    return jsonify(overall_sentiment=overall_sentiment, response=response)

if __name__ == '__main__':
    app.run(debug=False)

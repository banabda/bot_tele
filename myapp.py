from flask import Flask, render_template, request, Response
import firebaseController

app = Flask(__name__)


@app.route('/webhook', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        resp = request.get_json()
        docName = str(resp['message']['date']) + "_" + \
            str(resp['message']['chat']['id'])
        firebaseController.create(
            'webhook', docName, resp)
        return Response(resp, status=200)
    else:
        return render_template('webhook.html')


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

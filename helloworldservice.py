from flask import Flask
from flask import Response
import json

app = Flask(__name__)

@app.route('/helloworld', methods = ['GET'])
def api_helloworld():
    data = {
        'text'  : 'hello, world!',
    }
    js = json.dumps(data)
    response = Response(js, status=200, mimetype='application/json')
    return response

@app.route('/', methods = ['GET'])
def api_default():
    return "Home Page v1.3_final"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

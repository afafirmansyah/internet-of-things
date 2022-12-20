from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    id = request.args.get('id')
    pwd =  request.args.get('pwd')
    return 'Hello, World'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

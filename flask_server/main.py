from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo, desde Flask.'

app.run(debug=True, port=5001)
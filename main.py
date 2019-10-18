from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def send_root(path):
    return send_from_directory('', path)


@app.route('/hello')
def hello():
    return ("Hola")




@app.route('/adios')
def bye():
    return ("Adiós")
